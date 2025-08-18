# nuitka --msvc=latest --onefile --windows-console-mode=disable --windows-icon-from-ico=icon.ico "main.py"
# Parece que tengo que configurar algun parametro mas en nuitka para que compile correctamente el svg editor

# Todo: Hacer que se pueda crear nuevas página y quitar actuales, además de que documentos vacios (talvez en lugar de vacios permitir añadir archivos svg)
# Todo: Hacer que se puedan importar páginas en formato svg y borrar actuales

import webview
import os
import re
import json
from pathlib import Path

from const import var_better_html, html_interface
from SVGEditor import SVGEditor


class HTMLpreview:
    # Allows to use a function from the HTMLEditor class that calls HTMLpreview as an API.
    def __init__(self, open_preview_window_editor, update_html_content_preview, add_new_SVG, refresh_svg_icon, delete_this_SVG):
        self.open_preview_window_editor = open_preview_window_editor
        self.update_html_content_preview = update_html_content_preview
        self.add_new_SVG = add_new_SVG
        self.refresh_svg_icon = refresh_svg_icon
        self.delete_this_SVG = delete_this_SVG


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

    def get_svg_wraper(self, svg_content, i):
        return f"""<div id="SVGiewer{i}" class="SVG-viewer" style="width: 100%; height: 80vh; position: relative;">
            {svg_content}
            <button style="position: absolute; bottom: 10px; right: 10px;background: transparent; border: 0;">
                <svg id="zoom-in{i}" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M4.929 4.929A10 10 0 1 1 19.07 19.07A10 10 0 0 1 4.93 4.93zM13 9a1 1 0 1 0-2 0v2H9a1 1 0 1 0 0 2h2v2a1 1 0 1 0 2 0v-2h2a1 1 0 1 0 0-2h-2z"></path></svg>
                <svg id="zoom-out{i}" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34A10 10 0 1 1 2 12l.005-.324A10 10 0 0 1 17 3.34M16.5 11.5H8.5a0.5 0.5 0 0 0-0.5 0.5v1a0.5 0.5 0 0 0 0.5 0.5h8a0.5 0.5 0 0 0 0.5-0.5v-1a0.5 0.5 0 0 0-0.5-0.5"></path></svg>
                <svg id="reset_zoom{i}" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34a10 10 0 1 1-14.995 8.984L2 12l.005-.324A10 10 0 0 1 17 3.34m-6.489 5.8a1 1 0 0 0-1.218 1.567L10.585 12l-1.292 1.293l-.083.094a1 1 0 0 0 1.497 1.32L12 13.415l1.293 1.292l.094.083a1 1 0 0 0 1.32-1.497L13.415 12l1.292-1.293l.083-.094a1 1 0 0 0-1.497-1.32L12 10.585l-1.293-1.292l-.094-.083z"></path></svg>
            </button>
            <script>
            window.addEventListener('load', function () {{
                
                if (!document.getElementById('page{i}')){{
                    return;
                }}
                
                window.zoomContainer{i} = svgPanZoom("#page{i}");
                
                const viewer{i} = document.getElementById('SVGiewer{i}');
                const rectElement = viewer{i}.querySelector('svg g rect');
        
                if (rectElement) {{
                    // Get the dimensions of the rect
                    const rectWidth = rectElement.getAttribute('width') || rectElement.width.baseVal.value;
                    const rectHeight = rectElement.getAttribute('height') || rectElement.height.baseVal.value;
                    
                    // Calculate the ratio (height/width)
                    const aspectRatio = rectHeight / rectWidth;
                    
                    // Get the current width of the SVG-viewer
                    const viewerWidth = viewer{i}.offsetWidth;
                    
                    if (viewerWidth > 0) {{
                        // Calculate the proportional height
                        const proportionalHeight = viewerWidth * aspectRatio;
                        
                        // Calculate 80vh in pixels
                        const maxHeight = window.innerHeight * 0.8;
                        
                        // Apply proportional height with limit of 80vh
                        const finalHeight = Math.min(proportionalHeight, maxHeight);
                        viewer{i}.style.height = finalHeight + 'px';
                    }}
                }}

                // Button listeners
                document.getElementById('zoom-in{i}').addEventListener('click', function(ev){{
                    ev.preventDefault()
                    window.zoomContainer{i}.zoomIn()
                }});

                document.getElementById('zoom-out{i}').addEventListener('click', function(ev){{
                    ev.preventDefault()
                    window.zoomContainer{i}.zoomOut()
                }});
                
                function center_svg(){{
                    const zoomContainer = window.zoomContainer{i};
                    
                    if (zoomContainer) {{
                        zoomContainer.zoom(1);
                        zoomContainer.pan({{
                            x: (viewer{i}.offsetWidth - (zoomContainer.getSizes().viewBox.width * zoomContainer.getSizes().realZoom))/2, 
                            y: (viewer{i}.offsetHeight - (zoomContainer.getSizes().viewBox.height * zoomContainer.getSizes().realZoom))/2 
                        }});
                    }}
                }}

                document.getElementById('reset_zoom{i}').addEventListener('click', function(ev){{
                    ev.preventDefault()
                    center_svg();
                }});
                
                center_svg();
            }});
            </script>
            </div>"""
    
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

        nuevo_texto = ""  # Variable that holds the new content of html_content
        pos_anterior = 0

        for i, match in enumerate(matches):
            start = match.start()
            end = match.end()
            svg_content = match.group()

            # Add the text before the SVG
            nuevo_texto += self.html_content[pos_anterior:start]

            # Create the wrapper with the SVG and its controls
            wrapper = self.get_svg_wraper(svg_content, i + 1)

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

    def update_html_content(self):
        # Update preview
        self.html_content = self.window_preview.evaluate_js(
            """
            // Obtain the full content of the html and delete width="null" and height="null"
            let fullHTML = document.documentElement.outerHTML;
            fullHTML = fullHTML.replace(/\s(width|height)="null"/g, '');
        """
        )

        # Save in html_content the correct value of width and height
        self.html_content = self.html_content.replace('width-o="', 'width="').replace(
            'height-o="', 'height="'
        )

        # Update preview
        window.dispatch_custom_event("updateContent", {"content": self.html_content})

    def refresh_svg_icon(self, anchoDeseado = 150):
        """Function that updates the preview of the passed SVG icon. window.final_svg_edit must have a copy of the SVG to create the icon preview. Both the SVG with the same ID as the copy and the nav thumb child must exist."""

        self.window_preview.evaluate_js(
            f"""
            const targetWidth = {anchoDeseado};
            const svgElement = window.final_svg_edit;

            if (svgElement) {{
                try {{
                    // Obtener elemento y calcular dimensiones
                    const elementID = svgElement.id;
                    const svgElementNew = document.getElementById(elementID);
                    
                    // Calcular dimensiones con fallback
                    let bbox;
                    try {{
                        bbox = svgElementNew.getBBox();
                    }} catch (bboxError) {{
                        const viewBox = svgElementNew.viewBox?.baseVal;
                        bbox = viewBox ? 
                            {{ width: viewBox.width, height: viewBox.height }} : 
                            {{ width: svgElementNew.clientWidth || 800, height: svgElementNew.clientHeight || 600 }};
                    }}
                    
                    const targetHeight = Math.round(targetWidth * (bbox.height / bbox.width));
                    
                    // Clonar y limpiar SVG
                    const svgClone = svgElement.cloneNode(true);
                    
                    // Remover elementos problemáticos
                    svgClone.querySelectorAll('image').forEach(img => {{
                        const href = img.getAttribute('xlink:href') || img.getAttribute('href');
                        if (href && (href.startsWith('http') || href === '......' || !href.includes('data:'))) {{
                            img.remove();
                        }}
                    }});
                    svgClone.querySelectorAll('foreignObject').forEach(obj => obj.remove());
                    
                    // Serializar SVG
                    const serializer = new XMLSerializer();
                    let svgString = serializer.serializeToString(svgClone);
                    
                    // Agregar namespace si falta
                    if (!svgString.includes("xmlns")) {{
                        svgString = svgString.replace(/<svg/, '<svg xmlns="http://www.w3.org/2000/svg"');
                    }}
                    
                    // Limpiar caracteres problemáticos
                    svgString = svgString
                        .replace(/[""]/g, '"')      // Smart quotes
                        .replace(/['']/g, "'")      // Smart apostrophes  
                        .replace(/[–—]/g, "-")      // Em/en dashes
                        .replace(/…/g, "...")       // Ellipsis
                        .replace(/[\\u2000-\\u206F]/g, " ")  // Espacios especiales
                        .replace(/[\\u00A0]/g, " ") // Non-breaking space
                        .replace(/draggable="[^"]*"/g, '')   // Atributos problemáticos
                        .replace(/xmlns:ev="[^"]*"/g, '')
                        .replace(/\\s+/g, ' ')
                        .trim();
                    
                    // Crear data URI con fallback
                    function svgToDataUri(svgStr) {{
                        try {{
                            // Método 1: URL encoding (más compatible)
                            const encoded = encodeURIComponent(svgStr).replace(/'/g, "%27").replace(/"/g, "%22");
                            const uri = `data:image/svg+xml,${{encoded}}`;
                            return uri.length > 2000000 ? null : uri;
                        }} catch (error) {{
                            // Método 2: Base64 con limpieza
                            const cleanedSvg = svgStr.replace(/[^\\x00-\\x7F]/g, "").replace(/\\s+/g, ' ').trim();
                            return `data:image/svg+xml;base64,${{btoa(cleanedSvg)}}`;
                        }}
                    }}
                    
                    const svgDataURI = svgToDataUri(svgString);
                    
                    // Convertir a PNG
                    const img = new Image();
                    const timeout = setTimeout(() => {{ img.src = ''; }}, 10000); // Timeout 10s
                    
                    img.onload = function() {{
                        clearTimeout(timeout);
                        
                        // Crear canvas y contexto
                        const canvas = document.createElement("canvas");
                        canvas.width = targetWidth;
                        canvas.height = targetHeight;
                        const ctx = canvas.getContext("2d");
                        
                        // Configurar calidad y dibujar
                        ctx.imageSmoothingEnabled = true;
                        ctx.imageSmoothingQuality = "high";
                        ctx.clearRect(0, 0, targetWidth, targetHeight);
                        ctx.drawImage(img, 0, 0, targetWidth, targetHeight);
                        
                        const pngBase64 = canvas.toDataURL("image/png");
                        
                        // Actualizar miniatura
                        const pageNum = parseInt(elementID.replace("page", ""));
                        const navThumbs = document.getElementById("nav-thumbs");
                        const parentDiv = navThumbs.children[pageNum - 1];
                        const imgElement = parentDiv?.querySelector("img");
                        
                        if (imgElement) {{
                            imgElement.src = pngBase64;
                            
                            // Callback a Python
                            if (pywebview?.api?.update_html_content_preview) {{
                                pywebview.api.update_html_content_preview();
                            }}
                        }}
                    }};
                    
                    img.onerror = () => clearTimeout(timeout);
                    img.src = svgDataURI;
                    
                }} catch (error) {{
                    // Silenciar errores en producción
                }}
            }}
        """)

    def open_preview_window_editor(self, SVGHtml, id_el_preview):
        """Opens the preview of the current html_content"""
        if self.window_edit:
            # Do not edit again if editing
            self.window_preview.evaluate_js(
                'alert("Termina la edición actual para continuar");'
            )
            return

        def callback_funct(FinalSVGHtml):
            """Function that executes when finishing editing"""
            FinalSVGHtml = FinalSVGHtml.replace(
                "<svg", f'<svg id="{id_el_preview}"'
            )  # Add the id of the svg
            escaped_svg = json.dumps(FinalSVGHtml)

            self.window_edit = None

            number_ID_container = id_el_preview.replace("page", "")

            # Refresh Html visor content
            self.window_preview.evaluate_js(
                f"""
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

                // Remove all IDs from internal elements and take the content of each layer and put it in the DOM where it was
                window.cleanElementSVGAdded(page_var_edited);
                
                window.final_svg_edit = page_var_edited.cloneNode(true);
                
                if (window.actual_viewport) {{
                    // Refresh the SVG zoomContainer
                    window.zoomContainer{number_ID_container} = svgPanZoom("#page{number_ID_container}");
                }}
                
                // Allow editing again
                page_var_edited.addEventListener('contextmenu', handleRightClickPreview);
            """
            )

            self.refresh_svg_icon()

        # Open editor
        self.window_edit = SVGEditor(
            SVGHtml, private_mode=True, callback_funct=callback_funct, start_main=False
        )
    
    def get_SVG_pages_dicts(self):
        pages = self.window_preview.evaluate_js("""
            let svg_container = document.getElementById("svg-container");
            let svg_list = {};
            for (let svg_item_container of svg_container.children) {
                let svg_item = null;
                if (svg_item_container.tagName == "svg") {
                    svg_item = svg_item_container;
                }else{
                    svg_item = svg_item_container.querySelector("svg");
                }
                svg_list[svg_item.id] = svg_item.outerHTML; 
            };svg_list""")
        icons = self.window_preview.evaluate_js("""
            let icon_container = document.getElementById("nav-thumbs");
            let icon_list = {};
            let number_icon = 1;
            for (let icon_item_container of icon_container.children) {
                icon_list[number_icon] = icon_item_container.outerHTML;
                number_icon++;
            };icon_list""")
        return (pages, icons)
    
    def set_SVG_pages_dicts(self, svg_dict, icons_dict, is_better, svg_to_refresh_icon_id):
        if (is_better):
            for item_page_id, item_page_content in svg_dict.items():
                svg_dict[item_page_id] = self.get_svg_wraper(item_page_content, int(item_page_id.replace("page", "")))
                
        svg_dict_json = json.dumps(svg_dict)
        icons_dict_json = json.dumps(icons_dict)

        self.window_preview.evaluate_js(f"""
            let svg_dict = {svg_dict_json};
            let svg_container = document.getElementById("svg-container");

            svg_container.innerHTML = ""
            for (let [id, svgHTML] of Object.entries(svg_dict)) {{
                let temp = document.createElement("div");
                temp.innerHTML = svgHTML.trim();
                let containerElement = temp.firstChild;
                let svg_item = null;
                if (containerElement.tagName == "svg") {{
                    svg_item = containerElement;
                }}else{{
                    svg_item = containerElement.querySelector("svg");
                }}
                if (!svg_item.id || svg_item.id != id) {{ svg_item.id = id; }}
                if (!svg_item.attributes.viewBox) {{
                    const width = svg_item.getAttribute('width') || svg_item.getAttribute('width-o');
                    const height = svg_item.getAttribute('height') || svg_item.getAttribute('height-o');

                    // Calcula los nuevos valores para el viewBox
                    const newViewBoxWidth = parseInt(width) + 1;
                    const newViewBoxHeight = parseInt(height) + 1;

                    // Construye la nueva cadena del viewBox
                    // El viewBox se define como "min-x min-y width height"
                    const newViewBox = `0 0 ${{newViewBoxWidth}} ${{newViewBoxHeight}}`;

                    // Asigna el nuevo valor al viewBox
                    svg_item.setAttribute('viewBox', newViewBox);
                }}
                if (!{str(is_better).lower()} && svg_item.hasAttribute('width')) {{
                    svg_item.setAttribute('width-o', svg_item.getAttribute('width'));
                    svg_item.removeAttribute('width'); // Elimina el atributo original
                }}

                // Comprueba y mueve el atributo 'height'
                if (!{str(is_better).lower()} && svg_item.hasAttribute('height')) {{
                    svg_item.setAttribute('height-o', svg_item.getAttribute('height'));
                    svg_item.removeAttribute('height'); // Elimina el atributo original
                }}
                
                // Remove all IDs from internal elements and take the content of each layer and put it in the DOM where it was
                window.cleanElementSVGAdded(svg_item);
                
                if (id == "{svg_to_refresh_icon_id}") {{
                    window.final_svg_edit = svg_item.cloneNode(true);
                }}
                
                let containerElementNew = svg_container.appendChild(containerElement);
                
                if ({str(is_better).lower()}){{
                    window.runScripts(containerElementNew);
                }}
            }}
            setupPageElementsPreview();
        """)
        
        self.window_preview.evaluate_js(f"""
            let icon_dict = {icons_dict_json};
            let iconContainer = document.getElementById("nav-thumbs");
            iconContainer.innerHTML = "";
            // Obtiene todos los valores (HTML de los iconos), los limpia y los une en una sola cadena.
            for (let [id, iconHTML] of Object.entries(icon_dict)) {{
                let temp = document.createElement("div");
                temp.innerHTML = iconHTML.trim().replace(' selected"','"');
                let containerElement = temp.firstChild;
                containerElement.querySelector(".pagenum").textContent = id;
                (containerElement.querySelector(".scroll-link") || containerElement.querySelector("div > a")).setAttribute("href", "#page" + id);
                iconContainer.appendChild(containerElement);
            }}
        """)
        
        self.refresh_svg_icon()
        self.window_preview.dispatch_custom_event("load")
        self.update_html_content()

    def add_new_SVG(self, id_clicked, before_page = None, after_page = None, is_better = False):
        """Open and add a new svg file to the preview"""
        result = self.window_preview.create_file_dialog(
            webview.OPEN_DIALOG,
            directory=os.getcwd(),
            file_types=("Archivos SVG (*.svg)", "Todos los archivos (*.*)")
        )

        if result and len(result) > 0:
            file_path = result[0]
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    svg_content = f.read()
                    
                    (svg_dict, icons_dict) = self.get_SVG_pages_dicts()
                    
                    id_clicked_number_page = int(id_clicked.replace("page",""))
                    
                    svg_added_id = f"page{id_clicked_number_page}"
                    
                    if (before_page):
                        page_act = len(svg_dict)
                        while (page_act > id_clicked_number_page - 1):
                            svg_dict[f"page{page_act + 1}"] = svg_dict[f"page{page_act}"]
                            icons_dict[str(page_act + 1)] = icons_dict[str(page_act)]
                            page_act-=1
                        svg_dict[svg_added_id] = svg_content
                    
                    if (after_page):
                        page_act = len(svg_dict)
                        svg_added_id = f"page{id_clicked_number_page + 1}"
                        while (page_act > id_clicked_number_page):
                            svg_dict[f"page{page_act + 1}"] = svg_dict[f"page{page_act}"]
                            icons_dict[str(page_act + 1)] = icons_dict[str(page_act)]
                            page_act-=1
                        svg_dict[svg_added_id] = svg_content
                        # For when only exist one page this resolve the problem
                        icons_dict[str(id_clicked_number_page + 1)] = icons_dict["1"]

                    self.set_SVG_pages_dicts(svg_dict, icons_dict, is_better, svg_added_id)
                    
                    return {"success": True}
            except Exception as e:
                return {"success": False, "error": str(e)}
    
    def delete_this_SVG(self, id_clicked, is_better):
        (svg_dict, icons_dict) = self.get_SVG_pages_dicts()
        id_clicked_number_page = int(id_clicked.replace("page",""))

        page_fin = len(svg_dict)
        if (page_fin == 1):
            self.window_preview.evaluate_js("alert('Añade otra página para poder eliminar esta');")
            return
        page_act = id_clicked_number_page

        while (page_fin > page_act):
            svg_dict[f"page{page_act}"] = svg_dict[f"page{page_act + 1}"]
            icons_dict[str(page_act)] = icons_dict[str(page_act + 1)]
            page_act+=1
        
        del svg_dict[f"page{page_fin}"]
        del icons_dict[str(page_fin)]
        self.set_SVG_pages_dicts(svg_dict, icons_dict, is_better, "none")

    def open_preview_window(self, svg_editr):
        if self.window_preview:
            if self.window_edit:
                # Do not preview if editing
                self.window_preview.run_js(
                    "alert('Termina la edición actual para abrir una nueva preview')"
                )
                return
            else:
                # If not editing open preview again
                self.window_preview.destroy()

        # Creates an instance of HTMLpreview for use in the api of preview
        self.window_preview_api = HTMLpreview(
            self.open_preview_window_editor, self.update_html_content, self.add_new_SVG, self.refresh_svg_icon, self.delete_this_SVG
        )

        if not "svgs[i].setAttribute('width-o', oriWidth);" in svg_editr:
            # This creates a width-o and height-o attribute in SVG to save the original width and height
            svg_editr = svg_editr.replace(
                "svgs[i].removeAttribute('width');",
                "svgs[i].removeAttribute('width');svgs[i].setAttribute('width-o', oriWidth);",
            ).replace(
                "svgs[i].removeAttribute('height');",
                "svgs[i].removeAttribute('height');svgs[i].setAttribute('height-o', oriHeight);",
            )

        # Carpeta específica para guardar
        carpeta = os.path.join(os.environ.get("PROGRAMDATA", r"C:\ProgramData"), "HTML-SVG-Page-Generator", "preview")
        os.makedirs(carpeta, exist_ok=True)

        # Nombre del archivo donde guardarás el contenido
        html_path = os.path.join(carpeta, "preview.html")

        # Guardar el contenido en el archivo
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(svg_editr)

        # Create a preview of the current html_content
        self.window_preview = webview.create_window(
            "Preview window",
            f"file://{html_path}",
            width=1000,
            height=700,
            resizable=True,
            js_api=self.window_preview_api,
        )

        # if (not 'content="width=device-width, initial-scale=1.0"' in svg_editr):
        # If the html is not the better html
        def before_closing_preview():
            # Function called when the preview is about to close
            if self.window_edit:
                # Do not close the preview if something is being edited
                self.window_preview.run_js(
                    "alert('Termina la edición actual para cerrar la preview')"
                )
                return False

        self.window_preview.events.before_closing = before_closing_preview

        self.window_preview.run_js(
            """
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
                svgEl.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {
                    viewport.replaceWith(...viewport.childNodes);
                    window.actual_viewport = true; // The edited SVG has a viewport
                });

                // Serialize only the clean SVG
                return svgEl.outerHTML;
            }
            
            // Function to be executed when right-clicking on any SVG
            function handleRightClickPreview(event) {
                event.preventDefault();

                // Eliminar cualquier menú anterior
                document.querySelectorAll(".context-menu-temp").forEach(menu => menu.remove());

                // Crear estilos desde JS
                const style = document.createElement("style");
                style.textContent = `
                    .context-menu-temp {
                        position: absolute;
                        background: #222;
                        color: white;
                        border-radius: 6px;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.4);
                        padding: 5px 0;
                        font-family: sans-serif;
                        min-width: 150px;
                        z-index: 9999;
                    }
                    .context-menu-temp div {
                        padding: 8px 12px;
                        cursor: pointer;
                    }
                    .context-menu-temp div:hover {
                        background: #444;
                    }
                `;
                document.head.appendChild(style);

                // Crear el contenedor del menú
                const menu = document.createElement("div");
                menu.className = "context-menu-temp";

                // Crear opciones
                const option1 = document.createElement("div");
                option1.textContent = "Editar";
                option1.onclick = () => {
                    menu.remove();
                    style.remove();
                    let svgHtml = limpiarAtributosDuplicados(this.outerHTML);
                    pywebview.api.open_preview_window_editor(svgHtml, this.id);
                };

                const option2 = document.createElement("div");
                option2.textContent = "Añadir svg arriba";
                option2.onclick = () => {
                    menu.remove();
                    style.remove();
                    
                    let is_better = false;
                    if (document.getElementById("SVGiewer1")){
                        is_better = true;
                    }
                    
                    pywebview.api.add_new_SVG(this.id, true, undefined, is_better);
                };
                
                const option3 = document.createElement("div");
                option3.textContent = "Añadir svg abajo";
                option3.onclick = () => {
                    menu.remove();
                    style.remove();
                    
                    let is_better = false;
                    if (document.getElementById("SVGiewer1")){
                        is_better = true;
                    }
                    
                    pywebview.api.add_new_SVG(this.id, undefined, true, is_better);
                };
                
                const option4 = document.createElement("div");
                option4.textContent = "Eliminar";
                option4.onclick = () => {
                    menu.remove();
                    style.remove();
                    
                    let is_better = false;
                    if (document.getElementById("SVGiewer1")){
                        is_better = true;
                    }
                    
                    pywebview.api.delete_this_SVG(this.id, is_better);
                };
                
                const option5 = document.createElement("div");
                option5.textContent = "Actualizar icono";
                option5.onclick = () => {
                    menu.remove();
                    style.remove();
                    
                    let is_better = false;
                    if (document.getElementById("SVGiewer1")){
                        is_better = true;
                    }
                    
                    let clone_svg = this.cloneNode(true);
                    
                    window.cleanElementSVGAdded(clone_svg);
                    
                    console.log(clone_svg);
                    
                    window.final_svg_edit = clone_svg;
                    
                    pywebview.api.refresh_svg_icon();
                };

                menu.appendChild(option1);
                menu.appendChild(option2);
                menu.appendChild(option3);
                menu.appendChild(option4);
                menu.appendChild(option5);

                // Posicionar menú
                menu.style.left = `${event.pageX}px`;
                menu.style.top = `${event.pageY}px`;

                document.body.appendChild(menu);

                // Cerrar si se hace clic fuera o se presiona Escape
                const closeMenu = () => {
                    menu.remove();
                    style.remove();
                    document.removeEventListener("click", outsideClick);
                    document.removeEventListener("keydown", escClose);
                };

                const outsideClick = e => {
                    if (!menu.contains(e.target)) closeMenu();
                };

                const escClose = e => {
                    if (e.key === "Escape") closeMenu();
                };

                setTimeout(() => {
                    document.addEventListener("click", outsideClick);
                    document.addEventListener("keydown", escClose);
                }, 0);
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
            
            // Custom functions
            window.cleanElementSVGAdded = function(page_var_edited) {
                // Remove all IDs from internal elements
                page_var_edited.querySelectorAll("*").forEach(el => {
                    el.removeAttribute("id");
                    if (el.tagName.toLowerCase() === 'title') {
                        el.remove();
                    }
                });
                
                // Take the content of each layer and put it in the DOM where it was
                page_var_edited.querySelectorAll('.layer').forEach(layer => {
                    layer.replaceWith(...layer.childNodes);
                });
                
                page_var_edited.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {
                    viewport.replaceWith(...viewport.childNodes);
                });
            }
            
            window.runScripts = function(containerElement) {
                const scripts = containerElement.querySelectorAll("script");
                scripts.forEach(oldScript => {
                    const newScript = document.createElement("script");
                    
                    // Copiar el contenido inline
                    if (oldScript.textContent) {
                        newScript.textContent = oldScript.textContent;
                    }
                    
                    // Copiar atributos (src, type, etc.)
                    for (let attr of oldScript.attributes) {
                        newScript.setAttribute(attr.name, attr.value);
                    }
                    
                    // Reemplazar el viejo <script> por el nuevo ejecutable
                    oldScript.parentNode.replaceChild(newScript, oldScript);
                });
            }

            // Also run in case of dynamic content (optional)
            if (document.readyState === 'complete' || document.readyState === 'interactive') {
                setTimeout(setupPageElementsPreview, 0);
            }"""
        )
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
