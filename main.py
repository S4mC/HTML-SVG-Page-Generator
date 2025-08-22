# nuitka --msvc=latest --onefile --onefile-cache-mode=cached --windows-console-mode=disable --windows-icon-from-ico=icon.ico --include-data-dir="html=html" --onefile-tempdir-spec="%CACHE_DIR%\HTML-SVG-Page-Generator\Cache" "main.py"

import webview
import os
import re
import json

from const import var_better_html, html_interface, style_added_page, html_content_default, svg_page_default, js_injected_preview
from SVGEditor import SVGEditor


class HTMLpreview:
    # Allows to use a function from the HTMLEditor class that calls HTMLpreview as an API.
    def __init__(self, open_svg_editor, update_html_content, add_new_SVG, refresh_svg_icon, delete_this_SVG, reorder_SVGs):
        self.open_svg_editor = open_svg_editor
        self.update_html_content = update_html_content
        self.add_new_SVG = add_new_SVG
        self.refresh_svg_icon = refresh_svg_icon
        self.delete_this_SVG = delete_this_SVG
        self.reorder_SVGs = reorder_SVGs


class HTMLEditor:
    # Api of the main window
    def __init__(self):
        self.current_file = None
        self.html_content = html_content_default
        self.var_better_html = var_better_html
        self.window_preview = None
        self.window_preview_api = None
        self.window_edit = None
        self.saved_changes = True
    
    def before_closing_global(self):
        if (not self.saved_changes):
            result = window.evaluate_js('confirm("This cambios sin guardar, cerrar de todos modos?");')
            if not result:
                return False
        if (self.window_edit):
            self.window_edit.destroy()
            self.window_edit = None
        if (self.window_preview):
            self.window_preview.destroy()

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
                self.saved_changes = True
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
                
                let viewer{i} = document.getElementById('SVGiewer{i}');
                let rectElement = viewer{i}.querySelector('svg>g>rect');

                function proper_height(){{
                    rectElement = viewer{i}.querySelector('svg>g>rect');
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
                }}
                
                let resizeTimeout;
                window.addEventListener("resize", function () {{
                    clearTimeout(resizeTimeout); // Cancela cualquier timeout anterior
                    resizeTimeout = setTimeout(function () {{
                        viewer{i} = document.getElementById('SVGiewer{i}');
                        if (window.zoomContainer{i}) {{
                            window.zoomContainer{i}.destroy();
                        }}
                        proper_height();
                        viewer{i}.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {{
                            viewport.replaceWith(...viewport.childNodes);
                        }});
                        window.zoomContainer{i} = svgPanZoom("#page{i}");
                        center_svg();
                    }}, 280); // 280ms después de que termine
                }});
                
                proper_height();

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
                    rectElement = viewer{i}.querySelector('svg>g>rect');
                    
                    if (zoomContainer && rectElement) {{
                        zoomContainer.zoom(1);
                        zoomContainer.pan({{
                            x: (viewer{i}.offsetWidth - (zoomContainer.getSizes().viewBox.width * zoomContainer.getSizes().realZoom))/2, 
                            y: (viewer{i}.offsetHeight - (zoomContainer.getSizes().viewBox.height * zoomContainer.getSizes().realZoom))/2 
                        }});
                    }}else{{
                        window.zoomContainer{i}.resetZoom();
                        window.zoomContainer{i}.fit();
                        window.zoomContainer{i}.center();
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
        if ('<meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="utf-8"' in self.html_content):
            print("Ya esta mejorado")
            return {
                "success": True,
                "content": self.html_content,
            }
        # Add device scale
        self.replace_text(
            '<meta charset="utf-8"',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="utf-8"',
        )
        self.replace_text("</head>", style_added_page + "</head>")

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

                self.saved_changes = True
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
            let saved_html = document.documentElement.cloneNode(true);
            // Trabajar con el documento clonado, no el original
            const childNodes = saved_html.querySelector("#svg-container").childNodes;
            // Iterar sobre cada nodo hijo en el documento clonado
            childNodes.forEach(node => {
                // Verificar que sea un elemento (no texto o comentario)
                if (node.nodeType === Node.ELEMENT_NODE) {
                    // Cambiar la propiedad height a 80vh en el elemento clonado
                    node.style.height = "80vh";
                }
            });
            let fullHTML = saved_html.outerHTML;
            fullHTML = fullHTML.replace(/\s(width|height)="null"/g, '');
        """
        )

        # Save in html_content the correct value of width and height
        self.html_content = self.html_content.replace('width-o="', 'width="').replace(
            'height-o="', 'height="'
        )

        # Update preview
        window.dispatch_custom_event("updateContent", {"content": self.html_content})
        
        self.saved_changes = False

    def refresh_svg_icon(self, anchoDeseado = 150):
        """Function that updates the preview of the passed SVG icon. window.final_svg_edit must have a copy of the SVG to create the icon preview. Both the SVG with the same ID as the copy and the nav thumb child must exist."""

        self.window_preview.evaluate_js(
            f"""
            const targetWidth = {anchoDeseado};
            const svgElement = window.final_svg_edit;

            if (svgElement) {{
                try {{
                    window.final_svg_edit = null;
                    
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
                    
                    // Mejoras de visibilidad
                    svgClone.querySelectorAll('[stroke]').forEach(el => {{
                        const currentStroke = parseFloat(el.getAttribute('stroke-width') || '1');
                        // Aumentar el grosor del borde (mínimo 2px para visibilidad)
                        const newStrokeWidth = Math.max(currentStroke * 1.5, 5);
                        el.setAttribute('stroke-width', newStrokeWidth);
                        
                    }});
                    svgClone.querySelectorAll('path').forEach(path => {{
                        // Aumentar brillo y contraste
                        path.style.filter = 'brightness(1.6) contrast(1) saturate(1)';
                    }});
                    
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
                            if (pywebview?.api?.update_html_content) {{
                                pywebview.api.update_html_content();
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

    def open_svg_editor(self, SVGHtml, id_el_preview):
        """Opens the preview of the current html_content"""
        if self.window_edit:
            # Do not edit again if editing
            self.window_preview.evaluate_js(
                'alert("Termina la edición actual para continuar");'
            )
            return

        def callback_funct(FinalSVGHtml):
            """Function that executes when finishing editing"""
            if not self.window_preview:
                return
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
            
            self.window_preview.dispatch_custom_event("load")

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
    
    def set_SVG_pages_dicts(self, svg_dict, icons_dict, svg_to_refresh_icon_id, page_name = None, svg_page_to_go = None):
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
                
                // Remove all IDs from internal elements and take the content of each layer and put it in the DOM where it was
                window.cleanElementSVGAdded(svg_item);
                
                if (id == "{svg_to_refresh_icon_id}") {{
                    window.final_svg_edit = svg_item.cloneNode(true);
                }}
                
                let containerElementNew = svg_container.appendChild(containerElement);
                
                window.runScripts(containerElementNew);
            }}
            setupPageElementsPreview();
        """)
        
        # icons
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
                containerElement.querySelector("div > a").setAttribute("href", "#page" + id);
                if (id == "{svg_to_refresh_icon_id.replace('page', '')}") {{
                    containerElement.querySelector("p").textContent = {'"' + page_name + '"' if page_name else "'page'+" + "id"
};
                }}
                iconContainer.appendChild(containerElement);
            }}
            makeElementsEditable();
        """)
        
        
        self.refresh_svg_icon()
        self.window_preview.dispatch_custom_event("load")
        self.update_html_content()
        
        if (svg_page_to_go):
            self.window_preview.evaluate_js(f"""document.getElementById('{svg_page_to_go}').scrollIntoView({{
                behavior: 'smooth',  // desplazamiento suave
                block: 'center'      // lo centra en la pantalla
            }});""")

    def add_new_SVG(self, id_clicked, before_page = None, after_page = None, default_page = False):
        """Open and add a new svg file to the preview"""
        result = None
        if (not default_page):
            result = self.window_preview.create_file_dialog(
                webview.OPEN_DIALOG,
                directory=os.getcwd(),
                file_types=("Archivos SVG (*.svg)", "Todos los archivos (*.*)")
            )

        try:
            svg_content = None
            file_path = None
            
            if result and len(result) > 0:
                file_path = result[0]
                with open(file_path, "r", encoding="utf-8") as f:
                    svg_content = f.read()
            
            if default_page:
                svg_content = svg_page_default
            
            if svg_content:
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

                file_name_no_ext = None
                # Nombre de archivo sin extensión
                if (not default_page):
                    file_name_no_ext, _ = os.path.splitext(os.path.basename(file_path) )
                self.set_SVG_pages_dicts(svg_dict, icons_dict, svg_added_id, file_name_no_ext, svg_page_to_go=svg_added_id)
                
                return {"success": True}  
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def delete_this_SVG(self, id_clicked):
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
        self.set_SVG_pages_dicts(svg_dict, icons_dict, "none")
        
    def reorder_SVGs(self, new_order, numer_clicked):
        (svg_dict, icons_dict) = self.get_SVG_pages_dicts()
        
        svg_new_dict = {}
        page_act=1

        for page_number in new_order:
            svg_new_dict[f"page{page_act}"] = svg_dict[f"page{page_number}"]
            page_act+=1

        self.set_SVG_pages_dicts(svg_new_dict, icons_dict, "none", svg_page_to_go=f"page{numer_clicked}")

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
            self.open_svg_editor, self.update_html_content, self.add_new_SVG, self.refresh_svg_icon, self.delete_this_SVG, self.reorder_SVGs
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

        def before_closing_preview():
            # Function called when the preview is about to close
            if self.window_edit:
                # Do not close the preview if something is being edited
                self.window_preview.run_js(
                    "alert('Termina la edición actual para cerrar la preview')"
                )
                return False
            self.window_preview = None

        self.window_preview.events.before_closing = before_closing_preview

        self.window_preview.run_js(js_injected_preview)
        return {
            "success": True,
        }


if __name__ == "__main__":
    # Create window with webview
    api_HtmlEditor = HTMLEditor()
    window = webview.create_window(
        "Better Html EdrawMax",
        html=html_interface,
        width=1000,
        height=700,
        resizable=True,
        js_api=api_HtmlEditor,
    )
    
    window.events.before_closing = api_HtmlEditor.before_closing_global

    # Start the application
    webview.start(debug=True, private_mode=True)
