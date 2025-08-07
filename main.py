# nuitka --msvc=latest --onefile --windows-console-mode=disable --windows-icon-from-ico=icon.ico "main.py"
# Parece que tengo que configurar algun parametro mas en nuitka para que compile correctamente el svg editor

# Todo: Hacer que se pueda crear nuevas página y quitar actuales, además de que documentos vacios

import webview
import os
import re
import json
from pathlib import Path

from const import var_better_html, html_interface
from SVGEditor import SVGEditor


class HTMLpreview:
    # Allows to use a function from the HTMLEditor class that calls HTMLpreview as an API.
    def __init__(self, open_preview_window_editor):
        self.open_preview_window_editor = open_preview_window_editor

class HTMLEditor:
    # Api of the main window
    def __init__(self):
        self.current_file = None
        self.html_content = ""
        self.var_better_html = var_better_html
        self.window_preview = None
        self.window_preview_api = None
        self.window_edit = None

    def open_file(self):
        """Open an HTML file"""
        result = webview.windows[0].create_file_dialog(
            webview.OPEN_DIALOG,
            directory=os.getcwd(),
            file_types=("Archivos HTML (*.html;*.htm)", "Todos los archivos (*.*)"),
        )

        if result and len(result) > 0:
            file_path = result[0]
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.html_content = f.read()
                self.current_file = file_path
                return {
                    "success": True,
                    "content": self.html_content,
                    "filename": os.path.basename(file_path),
                }
            except Exception as e:
                return {"success": False, "error": str(e)}

        return {"success": False, "error": "No se seleccionó archivo"}

    def do_better_html(self):
        # Add device scale
        self.replace_text(
            '<meta charset="utf-8"',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="utf-8"',
        )
        self.replace_text('xlink:href="#', 'class="scroll-link" xlink:href="#')
        self.replace_text('<a href="#page', '<a class="scroll-link" href="#page')

        # Add SVG viewer foreach svg
        svg_pattern = r"<svg[^>]*>.*?</svg>"
        matches = list(re.finditer(svg_pattern, self.html_content, re.DOTALL))

        nuevo_texto = "" # Variable that holds the new content of html_content
        pos_anterior = 0

        for i, match in enumerate(matches):
            start = match.start()
            end = match.end()
            svg_content = match.group()

            # Add the text before the SVG
            nuevo_texto += self.html_content[pos_anterior:start]

            # Create the wrapper with the SVG and its controls
            wrapper = f"""<div id="SVGiewer{i+1}" class="SVG-viewer" style="width: 100%; height: 80vh; position: relative;">
            <button style="position: absolute; bottom: 10px; right: 10px;background: transparent; border: 0;">
                <svg id="zoom-in{i+1}" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M4.929 4.929A10 10 0 1 1 19.07 19.07A10 10 0 0 1 4.93 4.93zM13 9a1 1 0 1 0-2 0v2H9a1 1 0 1 0 0 2h2v2a1 1 0 1 0 2 0v-2h2a1 1 0 1 0 0-2h-2z"></path></svg>
                <svg id="zoom-out{i+1}" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34A10 10 0 1 1 2 12l.005-.324A10 10 0 0 1 17 3.34M16.5 11.5H8.5a0.5 0.5 0 0 0-0.5 0.5v1a0.5 0.5 0 0 0 0.5 0.5h8a0.5 0.5 0 0 0 0.5-0.5v-1a0.5 0.5 0 0 0-0.5-0.5"></path></svg>
                <svg id="reset_zoom{i+1}" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34a10 10 0 1 1-14.995 8.984L2 12l.005-.324A10 10 0 0 1 17 3.34m-6.489 5.8a1 1 0 0 0-1.218 1.567L10.585 12l-1.292 1.293l-.083.094a1 1 0 0 0 1.497 1.32L12 13.415l1.293 1.292l.094.083a1 1 0 0 0 1.32-1.497L13.415 12l1.292-1.293l.083-.094a1 1 0 0 0-1.497-1.32L12 10.585l-1.293-1.292l-.094-.083z"></path></svg>
            </button>
            {svg_content}
            <script>
            window.addEventListener('load', function () {{
                
                window.zoomContainer{i+1} = svgPanZoom("#page{i+1}");
                
                const viewer{i+1} = document.getElementById('SVGiewer{i+1}');
                const rectElement = viewer{i+1}.querySelector('svg g rect');
        
                if (rectElement) {{
                    // Get the dimensions of the rect
                    const rectWidth = rectElement.getAttribute('width') || rectElement.width.baseVal.value;
                    const rectHeight = rectElement.getAttribute('height') || rectElement.height.baseVal.value;
                    
                    // Calculate the ratio (height/width)
                    const aspectRatio = rectHeight / rectWidth;
                    
                    // Get the current width of the SVG-viewer
                    const viewerWidth = viewer{i+1}.offsetWidth;
                    
                    if (viewerWidth > 0) {{
                        // Calculate the proportional height
                        const proportionalHeight = viewerWidth * aspectRatio;
                        
                        // Calculate 80vh in pixels
                        const maxHeight = window.innerHeight * 0.8;
                        
                        // Apply proportional height with limit of 80vh
                        const finalHeight = Math.min(proportionalHeight, maxHeight);
                        viewer{i+1}.style.height = finalHeight + 'px';
                    }}
                }}

                // Button listeners
                document.getElementById('zoom-in{i+1}').addEventListener('click', function(ev){{
                    ev.preventDefault()
                    window.zoomContainer{i+1}.zoomIn()
                }});

                document.getElementById('zoom-out{i+1}').addEventListener('click', function(ev){{
                    ev.preventDefault()
                    window.zoomContainer{i+1}.zoomOut()
                }});

                document.getElementById('reset_zoom{i+1}').addEventListener('click', function(ev){{
                    ev.preventDefault()
                    
                    const zoomContainer = window.zoomContainer{i+1};
                    
                    if (zoomContainer) {{
                        zoomContainer.zoom(1);
                        zoomContainer.pan({{
                            x: (viewer{i+1}.offsetWidth - (zoomContainer.getSizes().viewBox.width * zoomContainer.getSizes().realZoom))/2, 
                            y: (viewer{i+1}.offsetHeight - (zoomContainer.getSizes().viewBox.height * zoomContainer.getSizes().realZoom))/2 
                        }});
                    }}
                }});
            }});
            </script>
            </div>"""

            nuevo_texto += wrapper
            pos_anterior = end

        # Add the rest of the text
        nuevo_texto += self.html_content[pos_anterior:]
        self.html_content = nuevo_texto

        self.replace_text(
            "</div></div></div></div><script>", self.var_better_html, to_final=True
        )
        return {
            "success": True,
            "content": self.html_content,
        }

    def replace_text(self, old_text, new_text, to_final=False):
        """Replace text in content"""
        if not self.html_content:
            return {"success": False, "error": "No content loaded"}

        try:
            if to_final:
                index = self.html_content.find(old_text)
                if index != -1:
                    self.html_content = self.html_content[:index] + new_text
            else:
                self.html_content = self.html_content.replace(old_text, new_text)

            return {
                "success": True,
                "content": self.html_content,
                "message": f"Text replaced successfully",
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def save_as(self, default_filename=""):
        """Save the file with a new name and location"""
        if not self.html_content:
            return {"success": False, "error": "There is no content to save"}

        try:
            # Get default directory (current file directory or working directory)
            default_dir = (
                os.path.dirname(self.current_file) if self.current_file else os.getcwd()
            )

            # Create file save dialog
            result = webview.windows[0].create_file_dialog(
                webview.SAVE_DIALOG,
                directory=default_dir,
                save_filename=default_filename,
                file_types=("Archivos HTML (*.html)", "Todos los archivos (*.*)"),
            )

            if result:
                # Make sure it has a .html extension if it doesn't.
                save_path = result[0]
                if not save_path.lower().endswith((".html", ".htm")):
                    save_path += ".html"

                # Save the file
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(self.html_content)

                return {
                    "success": True,
                    "message": f"File saved as: {save_path}",
                    "path": save_path,
                }
            else:
                return {"success": False, "error": "Saved canceled"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_current_content(self):
        """Gets the current content"""
        return {
            "content": self.html_content,
            "filename": (
                os.path.basename(self.current_file)
                if self.current_file
                else "Sin archivo"
            ),
        }

    def open_preview_window_editor(self, SVGHtml, id_el_preview):
        """Opens the preview of the current html_content"""
        if (self.window_edit):
            # Do not edit again if editing
            self.window_preview.evaluate_js('alert("Termina la edición actual para continuar");')
            return
            
        def callback_funct(FinalSVGHtml):
            """Function that executes when finishing editing"""
            FinalSVGHtml = FinalSVGHtml.replace('<svg', f'<svg id="{id_el_preview}"') # Add the id of the svg
            escaped_svg = json.dumps(FinalSVGHtml)
            
            self.window_edit = None
            
            number_ID_container = id_el_preview.replace("page","")
            
            # Refresh Html visor content
            self.html_content = self.window_preview.evaluate_js(f'''
                let page_var = document.getElementById("{id_el_preview}");

                // Save all attributes of the original SVG
                let originalAttributes = Array.from(page_var.attributes).map(attr => [attr.name, attr.value]);

                // Replace SVG content
                page_var.outerHTML = {escaped_svg};

                // Get the new SVG
                let page_var_edited = document.getElementById("{id_el_preview}");

                // Remove all current attributes from the new SVG
                Array.from(page_var_edited.attributes).forEach(attr => {{
                    page_var_edited.removeAttribute(attr.name);
                }});

                // Restore exactly the original attributes
                originalAttributes.forEach(([name, value]) => {{
                    page_var_edited.setAttribute(name, value);
                }});

                // Remove all IDs from internal elements
                page_var_edited.querySelectorAll("*").forEach(el => {{
                    el.removeAttribute("id");
                    if (el.tagName.toLowerCase() === 'title') {{
                        el.remove();
                    }}
                }});
                
                // Take the content of each layer and put it in the DOM where it was
                let layers = page_var_edited.querySelectorAll('.layer');
                layers.forEach(layer => {{
                    let parent = layer.parentNode;
                    while (layer.firstChild) {{
                        parent.insertBefore(layer.firstChild, layer);
                    }}
                    parent.removeChild(layer);
                }});
                
                if (window.actual_viewport) {{
                    // Refresh the SVG zoomContainer
                    window.zoomContainer{number_ID_container} = svgPanZoom("#page{number_ID_container}");
                }}
                
                // Allow editing again
                page_var_edited.addEventListener('contextmenu', handleRightClickPreview);
                
                // Obtain the full content of the html and delete width="null" and height="null"
                let fullHTML = document.documentElement.outerHTML;
                fullHTML = fullHTML.replace(/\s(width|height)="null"/g, '');
            ''')
            
            # Save in html_content the correct value of width and height
            self.html_content = self.html_content.replace('widthO="','width="').replace('heightO="','height="')
            
            # Update preview
            window.dispatch_custom_event("updateContent", {"content": self.html_content})
            
        # Open editor
        self.window_edit = SVGEditor(SVGHtml, private_mode=True, callback_funct=callback_funct, start_main = False)

    def open_preview_window(self, svg_editr):
        if (self.window_preview):
            if (self.window_edit):
                # Do not preview if editing
                self.window_preview.run_js("alert('Termina la edición actual para abrir una nueva preview')")
                return
            else:
                # If not editing open preview again
                self.window_preview.destroy()
        
        # Creates an instance of HTMLpreview for use in the api of preview
        self.window_preview_api = HTMLpreview(self.open_preview_window_editor)
        
        if (not "svgs[i].setAttribute('widthO', oriWidth);" in svg_editr):
            # This creates a widthO and heightO attribute in SVG to save the original width and height
            svg_editr = svg_editr.replace("svgs[i].removeAttribute('width');","svgs[i].removeAttribute('width');svgs[i].setAttribute('widthO', oriWidth);").replace("svgs[i].removeAttribute('height');","svgs[i].removeAttribute('height');svgs[i].setAttribute('heightO', oriHeight);")
        
        # Create a preview of the current html_content
        self.window_preview = webview.create_window(
            "Preview window",
            html=svg_editr,
            width=1000,
            height=700,
            resizable=True,
            js_api=self.window_preview_api,
        )
        
        # if (not 'content="width=device-width, initial-scale=1.0"' in svg_editr):
        # If the html is not the better html
        def before_closing_preview():
            # Function called when the preview is about to close
            if (self.window_edit):
                # Do not close the preview if something is being edited
                self.window_preview.run_js("alert('Termina la edición actual para cerrar la preview')")
                return False
        
        self.window_preview.events.before_closing = before_closing_preview
        
        self.window_preview.run_js("""
            function limpiarAtributosDuplicados(svgString) {
                // Parse as HTML to avoid errors due to malformed XML
                const doc = new DOMParser().parseFromString(svgString, "text/html");
                const svgEl = doc.body.firstElementChild;

                if (!svgEl || svgEl.tagName.toLowerCase() !== 'svg') {
                    console.warn('No valid SVG element could be found.');
                    return svgString; // Return the original if it fails
                }

                // Use a Map to keep only the first unique attributes
                const seen = new Set();
                const toRemove = [];

                for (const attr of Array.from(svgEl.attributes)) {
                    if (seen.has(attr.name)) {
                        toRemove.push(attr.name);
                    } else {
                        seen.add(attr.name);
                    }
                }

                // Eliminate duplicate attributes
                for (const name of toRemove) {
                    svgEl.removeAttribute(name);
                }
                
                window.actual_viewport = null;
                
                // Takes the contents of the viewport out
                let viewports = svgEl.querySelectorAll('.svg-pan-zoom_viewport');
                viewports.forEach(viewport => {
                    let parent = viewport.parentNode;
                    while (viewport.firstChild) {
                        parent.insertBefore(viewport.firstChild, viewport);
                    }
                    window.actual_viewport = true; // The edited SVG has a viewport
                    parent.removeChild(viewport);
                });

                // Serialize only the clean SVG
                return svgEl.outerHTML;
            }
            
            // Function to be executed when right-clicking on any SVG
            function handleRightClickPreview(event) {
                event.preventDefault();
                let svgHtml = limpiarAtributosDuplicados(this.outerHTML);
                pywebview.api.open_preview_window_editor(svgHtml, this.id);
            }

            // Find and assign events to elements
            function setupPageElementsPreview() {
                let pageNumber = 1;
                let elementExists = true;
                
                while (elementExists) {
                    const elementId = `page${pageNumber}`;
                    const element = document.getElementById(elementId);
                    
                    if (element) {
                        // Asignar el evento de clic derecho
                        element.addEventListener('contextmenu', handleRightClickPreview);
                        pageNumber++;
                    } else {
                        elementExists = false;
                    }
                }
            }

            // Also run in case of dynamic content (optional)
            if (document.readyState === 'complete' || document.readyState === 'interactive') {
                setTimeout(setupPageElementsPreview, 0);
            }""")
        return {
            "success": True,
        }


if __name__ == "__main__":
    # Create window with webview
    window = webview.create_window(
        "Better Html EdrawMax",
        html=html_interface,
        width=1000,
        height=700,
        resizable=True,
        js_api=HTMLEditor(),
    )

    # Start the application
    webview.start(debug=True, private_mode=True)