import webview
import os, sys
import time
import json

from SVGEditAPI import SVGEditAPI

# Todo: Allow export button
# Todo: Add the name of the file open for default if exist in save, Review: added save with pywebview api..

# Construir la ruta al archivo HTML relativa al script
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html", "editor", "svg-editor.html")

class SVGEditor():
    def __init__(self, svgToEdit=None, private_mode=False, callback_funct=None, start_main=True):
        self.svgToEdit = svgToEdit
        self.callback_funct = callback_funct
        
        self.window = webview.create_window(
            "SVG Editor", f"file://{html_path}", width=1200, height=800, js_api=SVGEditAPI(self.final_svg)
        )
        self.window.events.loaded += self.open_svg_to_edit
        self.window.events.before_closing = self.before_closing
        
        if (start_main):
            webview.start(debug=True, private_mode=private_mode)
    
    def destroy(self):
        self.window.destroy()

    def open_svg_to_edit(self):
        if (self.svgToEdit):
            # Edit the svg only works before make a better html
            self.window.dispatch_custom_event("openThisSVG", {"svg": self.svgToEdit})

    def before_closing(self):
        # We call the beforeClosing event to save the current configuration and the SVG. This function also calls final_svg.
        self.window.dispatch_custom_event("beforeClosing")

    def final_svg(self, svgContentHtml):
        if (self.callback_funct):
            self.callback_funct(svgContentHtml)

if __name__ == "__main__":
    SVGEditor()