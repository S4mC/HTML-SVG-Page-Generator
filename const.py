# Note: Style added to the best page 
style_added_page = """
<style>
    html {
        scrollbar-color: #848484 transparent;
        scrollbar-width: thin;
    }

    body {
        background-color: #2c2c2c;
    }
    .nav-thumb {
        margin: 5px auto !important;
        font-family: sans-serif;
    }
    
    .nav-thumb.dragging {
        opacity: 0.5;
        z-index: 1000;
    }

    .nav-thumb img {
        width: 80px;
    }

    #svg-container > div {
        display: block;
        margin-bottom: 0;
        margin: 5px auto !important;
    }

    #svg-container {
        margin: 0 5px !important;
    }
    
    #main-area {
        background-color: #2c2c2c;
    }

    #navBar {
        background-color: #2c2c2c !important;
        color: white !important;
    }

    .nav-thumb > div {
        border: 1px solid #808080 !important;
    }

    #main-content {
        background-color: #2c2c2c !important;
    }

    #navBar::-webkit-scrollbar{
        width: 5px;
        height: 5px;
        background-color: #2c2c2c;
    }
    #navBar::-webkit-scrollbar-track{
        -webkit-box-shadow: inset 0 0 4px rgba(0,0,0,.3);
        border-radius: 5px;
        background-color: #2c2c2c;
    }

    .SVG-viewer {
        background: #1b1b1b;
    }
    
    .SVG-viewer svg {
        width: inherit;
        height: inherit;
    }
    

    @media (min-width: 600px) {
        #main-content {
            margin-bottom: 0px !important;
        }  
    }

    @media (max-width: 600px) {
        #navBar {
            position: fixed;
            left: 0;
            top: auto !important;
            bottom: 0;
        }

        #nav-thumbs {
            display: flex;
        }

        #main-content {
            margin-right: 0px !important;
        }
    }
</style>"""

# Note: SVG pan Zoom min code
svg_pan_zoom = """
(function(){function e(t,n,s){function o(i,r){if(!n[i]){if(!t[i]){var c,l,d="function"==typeof require&&require;if(!r&&d)return d(i,!0);if(a)return a(i,!0);throw l=new Error("Cannot find module '"+i+"'"),(l.code="MODULE_NOT_FOUND",l)}c=n[i]={exports:{}},t[i][0].call(c.exports,function(e){var n=t[i][1][e];return o(n||e)},c,c.exports,e,t,n,s)}return n[i].exports}for(var a="function"==typeof require&&require,i=0;i<s.length;i++)o(s[i]);return o}return e})()({1:[function(e,t){var s=e("./svg-utilities");t.exports={enable:function(e){var t,o,i,n=e.svg.querySelector("defs");n||(n=document.createElementNS(s.svgNS,"defs"),e.svg.appendChild(n)),i=n.querySelector("style#svg-pan-zoom-controls-styles"),i||(o=document.createElementNS(s.svgNS,"style"),o.setAttribute("id","svg-pan-zoom-controls-styles"),o.setAttribute("type","text/css"),o.textContent=".svg-pan-zoom-control { cursor: pointer; fill: black; fill-opacity: 0.333; } .svg-pan-zoom-control:hover { fill-opacity: 0.8; } .svg-pan-zoom-control-background { fill: white; fill-opacity: 0.5; } .svg-pan-zoom-control-background { fill-opacity: 0.8; }",n.appendChild(o)),t=document.createElementNS(s.svgNS,"g"),t.setAttribute("id","svg-pan-zoom-controls"),t.setAttribute("transform","translate("+(e.width-70)+" "+(e.height-76)+") scale(0.75)"),t.setAttribute("class","svg-pan-zoom-control"),t.appendChild(this._createZoomIn(e)),t.appendChild(this._createZoomReset(e)),t.appendChild(this._createZoomOut(e)),e.svg.appendChild(t),e.controlIcons=t},_createZoomIn:function(e){var n,o,t=document.createElementNS(s.svgNS,"g");return t.setAttribute("id","svg-pan-zoom-zoom-in"),t.setAttribute("transform","translate(30.5 5) scale(0.015)"),t.setAttribute("class","svg-pan-zoom-control"),t.addEventListener("click",function(){e.getPublicInstance().zoomIn()},!1),t.addEventListener("touchstart",function(){e.getPublicInstance().zoomIn()},!1),n=document.createElementNS(s.svgNS,"rect"),n.setAttribute("x","0"),n.setAttribute("y","0"),n.setAttribute("width","1500"),n.setAttribute("height","1400"),n.setAttribute("class","svg-pan-zoom-control-background"),t.appendChild(n),o=document.createElementNS(s.svgNS,"path"),o.setAttribute("d","M1280 576v128q0 26 -19 45t-45 19h-320v320q0 26 -19 45t-45 19h-128q-26 0 -45 -19t-19 -45v-320h-320q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h320v-320q0 -26 19 -45t45 -19h128q26 0 45 19t19 45v320h320q26 0 45 19t19 45zM1536 1120v-960 q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5t84.5 -203.5z"),o.setAttribute("class","svg-pan-zoom-control-element"),t.appendChild(o),t},_createZoomReset:function(e){var n,o,i,t=document.createElementNS(s.svgNS,"g");return t.setAttribute("id","svg-pan-zoom-reset-pan-zoom"),t.setAttribute("transform","translate(5 35) scale(0.4)"),t.setAttribute("class","svg-pan-zoom-control"),t.addEventListener("click",function(){e.getPublicInstance().reset()},!1),t.addEventListener("touchstart",function(){e.getPublicInstance().reset()},!1),n=document.createElementNS(s.svgNS,"rect"),n.setAttribute("x","2"),n.setAttribute("y","2"),n.setAttribute("width","182"),n.setAttribute("height","58"),n.setAttribute("class","svg-pan-zoom-control-background"),t.appendChild(n),o=document.createElementNS(s.svgNS,"path"),o.setAttribute("d","M33.051,20.632c-0.742-0.406-1.854-0.609-3.338-0.609h-7.969v9.281h7.769c1.543,0,2.701-0.188,3.473-0.562c1.365-0.656,2.048-1.953,2.048-3.891C35.032,22.757,34.372,21.351,33.051,20.632z"),o.setAttribute("class","svg-pan-zoom-control-element"),t.appendChild(o),i=document.createElementNS(s.svgNS,"path"),i.setAttribute("d","M170.231,0.5H15.847C7.102,0.5,0.5,5.708,0.5,11.84v38.861C0.5,56.833,7.102,61.5,15.847,61.5h154.384c8.745,0,15.269-4.667,15.269-10.798V11.84C185.5,5.708,178.976,0.5,170.231,0.5z M42.837,48.569h-7.969c-0.219-0.766-0.375-1.383-0.469-1.852c-0.188-0.969-0.289-1.961-0.305-2.977l-0.047-3.211c-0.03-2.203-0.41-3.672-1.142-4.406c-0.732-0.734-2.103-1.102-4.113-1.102h-7.05v13.547h-7.055V14.022h16.524c2.361,0.047,4.178,0.344,5.45,0.891c1.272,0.547,2.351,1.352,3.234,2.414c0.731,0.875,1.31,1.844,1.737,2.906s0.64,2.273,0.64,3.633c0,1.641-0.414,3.254-1.242,4.84s-2.195,2.707-4.102,3.363c1.594,0.641,2.723,1.551,3.387,2.73s0.996,2.98,0.996,5.402v2.32c0,1.578,0.063,2.648,0.19,3.211c0.19,0.891,0.635,1.547,1.333,1.969V48.569z M75.579,48.569h-26.18V14.022h25.336v6.117H56.454v7.336h16.781v6H56.454v8.883h19.125V48.569z M104.497,46.331c-2.44,2.086-5.887,3.129-10.34,3.129c-4.548,0-8.125-1.027-10.731-3.082s-3.909-4.879-3.909-8.473h6.891c0.224,1.578,0.662,2.758,1.316,3.539c1.196,1.422,3.246,2.133,6.15,2.133c1.739,0,3.151-0.188,4.236-0.562c2.058-0.719,3.087-2.055,3.087-4.008c0-1.141-0.504-2.023-1.512-2.648c-1.008-0.609-2.607-1.148-4.796-1.617l-3.74-0.82c-3.676-0.812-6.201-1.695-7.576-2.648c-2.328-1.594-3.492-4.086-3.492-7.477c0-3.094,1.139-5.664,3.417-7.711s5.623-3.07,10.036-3.07c3.685,0,6.829,0.965,9.431,2.895c2.602,1.93,3.966,4.73,4.093,8.402h-6.938c-0.128-2.078-1.057-3.555-2.787-4.43c-1.154-0.578-2.587-0.867-4.301-0.867c-1.907,0-3.428,0.375-4.565,1.125c-1.138,0.75-1.706,1.797-1.706,3.141c0,1.234,0.561,2.156,1.682,2.766c0.721,0.406,2.25,0.883,4.589,1.43l6.063,1.43c2.657,0.625,4.648,1.461,5.975,2.508c2.059,1.625,3.089,3.977,3.089,7.055C108.157,41.624,106.937,44.245,104.497,46.331z M139.61,48.569h-26.18V14.022h25.336v6.117h-18.281v7.336h16.781v6h-16.781v8.883h19.125V48.569z M170.337,20.14h-10.336v28.43h-7.266V20.14h-10.383v-6.117h27.984V20.14z"),i.setAttribute("class","svg-pan-zoom-control-element"),t.appendChild(i),t},_createZoomOut:function(e){var n,o,t=document.createElementNS(s.svgNS,"g");return t.setAttribute("id","svg-pan-zoom-zoom-out"),t.setAttribute("transform","translate(30.5 70) scale(0.015)"),t.setAttribute("class","svg-pan-zoom-control"),t.addEventListener("click",function(){e.getPublicInstance().zoomOut()},!1),t.addEventListener("touchstart",function(){e.getPublicInstance().zoomOut()},!1),n=document.createElementNS(s.svgNS,"rect"),n.setAttribute("x","0"),n.setAttribute("y","0"),n.setAttribute("width","1500"),n.setAttribute("height","1400"),n.setAttribute("class","svg-pan-zoom-control-background"),t.appendChild(n),o=document.createElementNS(s.svgNS,"path"),o.setAttribute("d","M1280 576v128q0 26 -19 45t-45 19h-896q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h896q26 0 45 19t19 45zM1536 1120v-960q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5 t84.5 -203.5z"),o.setAttribute("class","svg-pan-zoom-control-element"),t.appendChild(o),t},disable:function(e){e.controlIcons&&(e.controlIcons.parentNode.removeChild(e.controlIcons),e.controlIcons=null)}}},{"./svg-utilities":5}],2:[function(e,t){var i=e("./svg-utilities"),o=e("./utilities"),s=function(e,t){this.init(e,t)};s.prototype.init=function(e,t){this.viewport=e,this.options=t,this.originalState={zoom:1,x:0,y:0},this.activeState={zoom:1,x:0,y:0},this.updateCTMCached=o.proxy(this.updateCTM,this),this.requestAnimationFrame=o.createRequestAnimationFrame(this.options.refreshRate),this.viewBox={x:0,y:0,width:0,height:0},this.cacheViewBox();var n=this.processCTM();this.setCTM(n),this.updateCTM()},s.prototype.cacheViewBox=function(){var e,t,n=this.options.svg.getAttribute("viewBox");n?(e=n.split(/[\s,]/).filter(function(e){return e}).map(parseFloat),this.viewBox.x=e[0],this.viewBox.y=e[1],this.viewBox.width=e[2],this.viewBox.height=e[3],t=Math.min(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height),this.activeState.zoom=t,this.activeState.x=(this.options.width-this.viewBox.width*t)/2,this.activeState.y=(this.options.height-this.viewBox.height*t)/2,this.updateCTMOnNextFrame(),this.options.svg.removeAttribute("viewBox")):this.simpleViewBoxCache()},s.prototype.simpleViewBoxCache=function(){var e=this.viewport.getBBox();this.viewBox.x=e.x,this.viewBox.y=e.y,this.viewBox.width=e.width,this.viewBox.height=e.height},s.prototype.getViewBox=function(){return o.extend({},this.viewBox)},s.prototype.processCTM=function(){if(e=this.getCTM(),(this.options.fit||this.options.contain)&&(this.options.fit?t=Math.min(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height):t=Math.max(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height),e.a=t,e.d=t,e.e=-this.viewBox.x*t,e.f=-this.viewBox.y*t),this.options.center){var e,t,n=(this.options.width-(this.viewBox.width+this.viewBox.x*2)*e.a)*.5,s=(this.options.height-(this.viewBox.height+this.viewBox.y*2)*e.a)*.5;e.e=n,e.f=s}return this.originalState.zoom=e.a,this.originalState.x=e.e,this.originalState.y=e.f,e},s.prototype.getOriginalState=function(){return o.extend({},this.originalState)},s.prototype.getState=function(){return o.extend({},this.activeState)},s.prototype.getZoom=function(){return this.activeState.zoom},s.prototype.getRelativeZoom=function(){return this.activeState.zoom/this.originalState.zoom},s.prototype.computeRelativeZoom=function(e){return e/this.originalState.zoom},s.prototype.getPan=function(){return{x:this.activeState.x,y:this.activeState.y}},s.prototype.getCTM=function(){var e=this.options.svg.createSVGMatrix();return e.a=this.activeState.zoom,e.b=0,e.c=0,e.d=this.activeState.zoom,e.e=this.activeState.x,e.f=this.activeState.y,e},s.prototype.setCTM=function(e){if(n=this.isZoomDifferent(e),s=this.isPanDifferent(e),n||s){if(n&&(this.options.beforeZoom(this.getRelativeZoom(),this.computeRelativeZoom(e.a))===!1?(e.a=e.d=this.activeState.zoom,n=!1):(this.updateCache(e),this.options.onZoom(this.getRelativeZoom()))),s){var n,s,t=this.options.beforePan(this.getPan(),{x:e.e,y:e.f}),i=!1,a=!1;t===!1?(e.e=this.getPan().x,e.f=this.getPan().y,i=a=!0):o.isObject(t)&&(t.x===!1?(e.e=this.getPan().x,i=!0):o.isNumber(t.x)&&(e.e=t.x),t.y===!1?(e.f=this.getPan().y,a=!0):o.isNumber(t.y)&&(e.f=t.y)),i&&a||!this.isPanDifferent(e)?s=!1:(this.updateCache(e),this.options.onPan(this.getPan()))}(n||s)&&this.updateCTMOnNextFrame()}},s.prototype.isZoomDifferent=function(e){return this.activeState.zoom!==e.a},s.prototype.isPanDifferent=function(e){return this.activeState.x!==e.e||this.activeState.y!==e.f},s.prototype.updateCache=function(e){this.activeState.zoom=e.a,this.activeState.x=e.e,this.activeState.y=e.f},s.prototype.pendingUpdate=!1,s.prototype.updateCTMOnNextFrame=function(){this.pendingUpdate||(this.pendingUpdate=!0,this.requestAnimationFrame.call(window,this.updateCTMCached))},s.prototype.updateCTM=function(){var e=this.getCTM();i.setCTM(this.viewport,e,this.defs),this.pendingUpdate=!1,this.options.onUpdatedCTM&&this.options.onUpdatedCTM(e)},t.exports=function(e,t){return new s(e,t)}},{"./svg-utilities":5,"./utilities":7}],3:[function(e,t){var s=e("./svg-pan-zoom.js");(function(e){typeof define=="function"&&define.amd?define("svg-pan-zoom",function(){return s}):typeof t!="undefined"&&t.exports&&(t.exports=s,e.svgPanZoom=s)})(window,document)},{"./svg-pan-zoom.js":4}],4:[function(e,t){var a,d,c=e("./uniwheel"),r=e("./control-icons"),i=e("./utilities"),o=e("./svg-utilities"),u=e("./shadow-viewport"),s=function(e,t){this.init(e,t)},h={viewportSelector:".svg-pan-zoom_viewport",panEnabled:!0,controlIconsEnabled:!1,zoomEnabled:!0,dblClickZoomEnabled:!1,mouseWheelZoomEnabled:!0,preventMouseEventsDefault:!0,zoomScaleSensitivity:.3,minZoom:.5,maxZoom:10,fit:!0,contain:!1,center:!0,refreshRate:"auto",beforeZoom:null,onZoom:null,beforePan:null,onPan:null,customEventsHandler:null,eventsListenerElement:null,onUpdatedCTM:null},l={passive:!0};s.prototype.init=function(e,t){var s,a,n=this;this.svg=e,this.defs=e.querySelector("defs"),o.setupSvgAttributes(this.svg),this.options=i.extend(i.extend({},h),t),this.state="none",this.pinchZoomEnabled=!0,this.lastDistance=0,this.pinchStartDistance=0,this.pinchMidpoint=null,a=o.getBoundingClientRectNormalized(e),this.width=a.width,this.height=a.height,this.viewport=u(o.getOrCreateViewport(this.svg,this.options.viewportSelector),{svg:this.svg,width:this.width,height:this.height,fit:this.options.fit,contain:this.options.contain,center:this.options.center,refreshRate:this.options.refreshRate,beforeZoom:function(e,t){if(n.viewport&&n.options.beforeZoom)return n.options.beforeZoom(e,t)},onZoom:function(e){if(n.viewport&&n.options.onZoom)return n.options.onZoom(e)},beforePan:function(e,t){if(n.viewport&&n.options.beforePan)return n.options.beforePan(e,t)},onPan:function(e){if(n.viewport&&n.options.onPan)return n.options.onPan(e)},onUpdatedCTM:function(e){if(n.viewport&&n.options.onUpdatedCTM)return n.options.onUpdatedCTM(e)}}),s=this.getPublicInstance(),s.setBeforeZoom(this.options.beforeZoom),s.setOnZoom(this.options.onZoom),s.setBeforePan(this.options.beforePan),s.setOnPan(this.options.onPan),s.setOnUpdatedCTM(this.options.onUpdatedCTM),this.options.controlIconsEnabled&&r.enable(this),this.lastMouseWheelEventTime=Date.now(),this.setupHandlers()},s.prototype.setupHandlers=function(){var t,n,o,e=this,s=null;if(this.eventListeners={mousedown:function(t){var n=e.handleMouseDown(t,s);return s=t,n},touchstart:function(t){var n=e.handleMouseDown(t,s);return s=t,n},auxclick:function(t){return e.handleauxclick(t)},mouseup:function(t){return e.handleMouseUp(t)},touchend:function(t){return e.handleMouseUp(t)},mousemove:function(t){return e.handleMouseMove(t)},touchmove:function(t){return e.handleTouchMove(t)},mouseleave:function(t){return e.handleMouseUp(t)},touchleave:function(t){return e.handleMouseUp(t)},touchcancel:function(t){return e.handleMouseUp(t)}},this.options.customEventsHandler!=null&&(this.options.customEventsHandler.init({svgElement:this.svg,eventsListenerElement:this.options.eventsListenerElement,instance:this.getPublicInstance()}),t=this.options.customEventsHandler.haltEventListeners,t&&t.length))for(n=t.length-1;n>=0;n--)this.eventListeners.hasOwnProperty(t[n])&&delete this.eventListeners[t[n]];for(o in this.eventListeners)(this.options.eventsListenerElement||this.svg).addEventListener(o,this.eventListeners[o],!this.options.preventMouseEventsDefault&&l);this.options.mouseWheelZoomEnabled&&(this.options.mouseWheelZoomEnabled=!1,this.enableMouseWheelZoom())},s.prototype.enableMouseWheelZoom=function(){if(!this.options.mouseWheelZoomEnabled){var e,t=this;this.wheelListener=function(e){return t.handleMouseWheel(e)},e=!this.options.preventMouseEventsDefault,c.on(this.options.eventsListenerElement||this.svg,this.wheelListener,e),this.options.mouseWheelZoomEnabled=!0}},s.prototype.disableMouseWheelZoom=function(){if(this.options.mouseWheelZoomEnabled){var e=!this.options.preventMouseEventsDefault;c.off(this.options.eventsListenerElement||this.svg,this.wheelListener,e),this.options.mouseWheelZoomEnabled=!1}},s.prototype.handleMouseWheel=function(e){if(this.state=="pan"&&e.preventDefault(),!this.options.zoomEnabled)return;if(this.state!=="pan"){if(!e.ctrlKey&&!e.shiftKey)return;if(this.state!=="none")return}this.options.preventMouseEventsDefault&&(e.preventDefault?e.preventDefault():e.returnValue=!1);var t=e.deltaY||1,n=Date.now()-this.lastMouseWheelEventTime,s=3+Math.max(0,30-n);this.lastMouseWheelEventTime=Date.now(),"deltaMode"in e&&e.deltaMode===0&&e.wheelDelta&&(t=e.deltaY===0?0:Math.abs(e.wheelDelta)/e.deltaY);var t=-.3<t&&t<.3?t:(t>0?1:-1)*Math.log(Math.abs(t)+10)/s,i=this.svg.getScreenCTM().inverse(),a=o.getEventPoint(e,this.svg).matrixTransform(i),r=(1+this.options.zoomScaleSensitivity)**(-1*t);this.zoomAtPoint(r,a),this.state==="pan"&&(this.firstEventCTM=this.viewport.getCTM(),this.stateOrigin=o.getEventPoint(e,this.svg).matrixTransform(this.firstEventCTM.inverse()))},s.prototype.zoomAtPoint=function(e,t,n){s=this.viewport.getOriginalState(),n?(e=Math.max(this.options.minZoom*s.zoom,Math.min(this.options.maxZoom*s.zoom,e)),e=e/this.getZoom()):this.getZoom()*e<this.options.minZoom*s.zoom?e=this.options.minZoom*s.zoom/this.getZoom():this.getZoom()*e>this.options.maxZoom*s.zoom&&(e=this.options.maxZoom*s.zoom/this.getZoom());var s,i=this.viewport.getCTM(),o=t.matrixTransform(i.inverse()),r=this.svg.createSVGMatrix().translate(o.x,o.y).scale(e).translate(-o.x,-o.y),a=i.multiply(r);a.a!==i.a&&this.viewport.setCTM(a)},s.prototype.zoom=function(e,t){this.zoomAtPoint(e,o.getSvgCenterPoint(this.svg,this.width,this.height),t)},s.prototype.publicZoom=function(e,t){t&&(e=this.computeFromRelativeZoom(e)),this.zoom(e,t)},s.prototype.publicZoomAtPoint=function(e,t,n){if(n&&(e=this.computeFromRelativeZoom(e)),i.getType(t)!=="SVGPoint")if("x"in t&&"y"in t)t=o.createSVGPoint(this.svg,t.x,t.y);else throw new Error("Given point is invalid");this.zoomAtPoint(e,t,n)},s.prototype.getZoom=function(){return this.viewport.getZoom()},s.prototype.getRelativeZoom=function(){return this.viewport.getRelativeZoom()},s.prototype.computeFromRelativeZoom=function(e){return e*this.viewport.getOriginalState().zoom},s.prototype.resetZoom=function(){var e=this.viewport.getOriginalState();this.zoom(e.zoom,!0)},s.prototype.resetPan=function(){this.pan(this.viewport.getOriginalState())},s.prototype.reset=function(){this.resetZoom(),this.resetPan()},s.prototype.handleDblClick=function(e){if(this.options.preventMouseEventsDefault&&(e.preventDefault?e.preventDefault():e.returnValue=!1),this.options.controlIconsEnabled){var t,n,s=e.target.getAttribute("class")||"";if(s.indexOf("svg-pan-zoom-control")>-1)return!1}e.shiftKey?t=1/((1+this.options.zoomScaleSensitivity)*2):t=(1+this.options.zoomScaleSensitivity)*2,n=o.getEventPoint(e,this.svg).matrixTransform(this.svg.getScreenCTM().inverse()),this.zoomAtPoint(t,n)},s.prototype.handleMouseDown=function(e,t){if(e.button===0)return;this.options.preventMouseEventsDefault&&e.preventDefault&&e.type!=="touchstart"&&!(e.touches&&e.touches.length==1)&&e.preventDefault(),i.mouseAndTouchNormalize(e,this.svg),this.options.dblClickZoomEnabled&&i.isDblClick(e,t)?this.handleDblClick(e):(this.state="pan",this.firstEventCTM=this.viewport.getCTM(),this.stateOrigin=o.getEventPoint(e,this.svg).matrixTransform(this.firstEventCTM.inverse()))},s.prototype.handleMouseMove=function(e){if(this.options.preventMouseEventsDefault&&e.preventDefault&&e.preventDefault(),this.state==="pan"&&this.options.panEnabled){var t=o.getEventPoint(e,this.svg).matrixTransform(this.firstEventCTM.inverse()),n=this.firstEventCTM.translate(t.x-this.stateOrigin.x,t.y-this.stateOrigin.y);this.viewport.setCTM(n)}},s.prototype.getTouchDistance=function(e,t){return Math.sqrt((t.clientX-e.clientX)**2+(t.clientY-e.clientY)**2)},s.prototype.getTouchMidpoint=function(e,t){return{x:(e.clientX+t.clientX)/2,y:(e.clientY+t.clientY)/2}},s.prototype.handleTouchMove=function(e){if(this.options.preventMouseEventsDefault&&e.preventDefault&&e.preventDefault(),e.touches&&e.touches.length===2&&this.options.zoomEnabled&&this.pinchZoomEnabled){var t,n,s,i,a,c,l,d,u,h,m,f,p,g,v,b,r=this.getTouchDistance(e.touches[0],e.touches[1]);this.pinchMidpoint||(this.pinchStartDistance=r,this.pinchMidpoint=this.getTouchMidpoint(e.touches[0],e.touches[1]),this.initialTouch1={x:e.touches[0].clientX,y:e.touches[0].clientY},this.initialTouch2={x:e.touches[1].clientX,y:e.touches[1].clientY},s=o.createSVGPoint(this.svg,e.touches[0].clientX,e.touches[0].clientY),i=o.createSVGPoint(this.svg,e.touches[1].clientX,e.touches[1].clientY),this.initialCorner1=s.matrixTransform(this.svg.getScreenCTM().inverse()),this.initialCorner2=i.matrixTransform(this.svg.getScreenCTM().inverse()),this.initialPinchCTM=this.viewport.getCTM(),this.firstEventCTM=this.viewport.getCTM(),this.stateOrigin=o.getEventPoint(e,this.svg).matrixTransform(this.firstEventCTM.inverse())),this.pinchStartDistance>0&&r>0&&(g=r/this.pinchStartDistance,a=this.getTouchMidpoint(e.touches[0],e.touches[1]),h=a.x-this.pinchMidpoint.x,u=a.y-this.pinchMidpoint.y,this.options.panEnabled&&(n=this.viewport.getCTM(),n.e+=h,n.f+=u,this.viewport.setCTM(n)),s=o.createSVGPoint(this.svg,e.touches[0].clientX,e.touches[0].clientY),i=o.createSVGPoint(this.svg,e.touches[1].clientX,e.touches[1].clientY),c=s.matrixTransform(this.svg.getScreenCTM().inverse()),l=i.matrixTransform(this.svg.getScreenCTM().inverse()),m=(c.x+l.x)/2,f=(c.y+l.y)/2,p=o.createSVGPoint(this.svg,m,f),d=this.viewport.getCTM(),t=p.matrixTransform(d.inverse()),v=this.svg.createSVGMatrix().translate(t.x,t.y).scale(g).translate(-t.x,-t.y),b=d.multiply(v),this.viewport.setCTM(b),this.pinchStartDistance=r,this.pinchMidpoint=a,this.firstEventCTM=this.viewport.getCTM(),this.firstEventCTM=this.viewport.getCTM(),this.stateOrigin=o.getEventPoint(e,this.svg).matrixTransform(this.firstEventCTM.inverse()));return}e.touches&&e.touches.length===1&&(this.pinchStartDistance=0,this.pinchMidpoint=null,this.initialCorner1=null,this.initialCorner2=null,this.initialPinchCTM=null,this.initialTouch1=null,this.initialTouch2=null)},s.prototype.handleauxclick=function(e){e.preventDefault()},s.prototype.handleMouseUp=function(e){this.options.preventMouseEventsDefault&&(e.preventDefault?e.type!="touchend"&&e.preventDefault():e.returnValue=!1),this.state==="pan"&&(this.state="none"),this.pinchStartDistance=0,this.pinchMidpoint=null,this.initialCorner1=null,this.initialCorner2=null,this.initialPinchCTM=null,this.initialTouch1=null,this.initialTouch2=null},s.prototype.fit=function(){var e=this.viewport.getViewBox(),t=Math.min(this.width/e.width,this.height/e.height);this.zoom(t,!0)},s.prototype.contain=function(){var e=this.viewport.getViewBox(),t=Math.max(this.width/e.width,this.height/e.height);this.zoom(t,!0)},s.prototype.center=function(){var e=this.viewport.getViewBox(),t=(this.width-(e.width+e.x*2)*this.getZoom())*.5,n=(this.height-(e.height+e.y*2)*this.getZoom())*.5;this.getPublicInstance().pan({x:t,y:n})},s.prototype.updateBBox=function(){this.viewport.simpleViewBoxCache()},s.prototype.pan=function(e){var t=this.viewport.getCTM();t.e=e.x,t.f=e.y,this.viewport.setCTM(t)},s.prototype.panBy=function(e){var t=this.viewport.getCTM();t.e+=e.x,t.f+=e.y,this.viewport.setCTM(t)},s.prototype.getPan=function(){var e=this.viewport.getState();return{x:e.x,y:e.y}},s.prototype.resize=function(){var e,t=o.getBoundingClientRectNormalized(this.svg);this.width=t.width,this.height=t.height,e=this.viewport,e.options.width=this.width,e.options.height=this.height,e.processCTM(),this.options.controlIconsEnabled&&(this.getPublicInstance().disableControlIcons(),this.getPublicInstance().enableControlIcons())},s.prototype.destroy=function(){var e,t=this;this.beforeZoom=null,this.onZoom=null,this.beforePan=null,this.onPan=null,this.onUpdatedCTM=null,this.pinchZoomEnabled=!1,this.lastDistance=0,this.pinchStartDistance=0,this.pinchMidpoint=null,this.initialCorner1=null,this.initialCorner2=null,this.initialPinchCTM=null,this.initialTouch1=null,this.initialTouch2=null,this.options.customEventsHandler!=null&&this.options.customEventsHandler.destroy({svgElement:this.svg,eventsListenerElement:this.options.eventsListenerElement,instance:this.getPublicInstance()});for(e in this.eventListeners)(this.options.eventsListenerElement||this.svg).removeEventListener(e,this.eventListeners[e],!this.options.preventMouseEventsDefault&&l);this.disableMouseWheelZoom(),this.getPublicInstance().disableControlIcons(),this.reset(),a=a.filter(function(e){return e.svg!==t.svg}),delete this.options,delete this.viewport,delete this.publicInstance,delete this.pi,this.getPublicInstance=function(){return null}},s.prototype.getPublicInstance=function(){var e=this;return this.publicInstance||(this.publicInstance=this.pi={enablePan:function(){return e.options.panEnabled=!0,e.pi},disablePan:function(){return e.options.panEnabled=!1,e.pi},enablePinchZoom:function(){return e.pinchZoomEnabled=!0,e.pi},disablePinchZoom:function(){return e.pinchZoomEnabled=!1,e.pi},isPinchZoomEnabled:function(){return!!e.pinchZoomEnabled},isPanEnabled:function(){return!!e.options.panEnabled},pan:function(t){return e.pan(t),e.pi},panBy:function(t){return e.panBy(t),e.pi},getPan:function(){return e.getPan()},setBeforePan:function(t){return e.options.beforePan=t===null?null:i.proxy(t,e.publicInstance),e.pi},setOnPan:function(t){return e.options.onPan=t===null?null:i.proxy(t,e.publicInstance),e.pi},enableZoom:function(){return e.options.zoomEnabled=!0,e.pi},disableZoom:function(){return e.options.zoomEnabled=!1,e.pi},isZoomEnabled:function(){return!!e.options.zoomEnabled},enableControlIcons:function(){return e.options.controlIconsEnabled||(e.options.controlIconsEnabled=!0,r.enable(e)),e.pi},disableControlIcons:function(){return e.options.controlIconsEnabled&&(e.options.controlIconsEnabled=!1,r.disable(e)),e.pi},isControlIconsEnabled:function(){return!!e.options.controlIconsEnabled},enableDblClickZoom:function(){return e.options.dblClickZoomEnabled=!0,e.pi},disableDblClickZoom:function(){return e.options.dblClickZoomEnabled=!1,e.pi},isDblClickZoomEnabled:function(){return!!e.options.dblClickZoomEnabled},enableMouseWheelZoom:function(){return e.enableMouseWheelZoom(),e.pi},disableMouseWheelZoom:function(){return e.disableMouseWheelZoom(),e.pi},isMouseWheelZoomEnabled:function(){return!!e.options.mouseWheelZoomEnabled},setZoomScaleSensitivity:function(t){return e.options.zoomScaleSensitivity=t,e.pi},setMinZoom:function(t){return e.options.minZoom=t,e.pi},setMaxZoom:function(t){return e.options.maxZoom=t,e.pi},setBeforeZoom:function(t){return e.options.beforeZoom=t===null?null:i.proxy(t,e.publicInstance),e.pi},setOnZoom:function(t){return e.options.onZoom=t===null?null:i.proxy(t,e.publicInstance),e.pi},zoom:function(t){return e.publicZoom(t,!0),e.pi},zoomBy:function(t){return e.publicZoom(t,!1),e.pi},zoomAtPoint:function(t,n){return e.publicZoomAtPoint(t,n,!0),e.pi},zoomAtPointBy:function(t,n){return e.publicZoomAtPoint(t,n,!1),e.pi},zoomIn:function(){return this.zoomBy(1+e.options.zoomScaleSensitivity),e.pi},zoomOut:function(){return this.zoomBy(1/(1+e.options.zoomScaleSensitivity)),e.pi},getZoom:function(){return e.getRelativeZoom()},setOnUpdatedCTM:function(t){return e.options.onUpdatedCTM=t===null?null:i.proxy(t,e.publicInstance),e.pi},resetZoom:function(){return e.resetZoom(),e.pi},resetPan:function(){return e.resetPan(),e.pi},reset:function(){return e.reset(),e.pi},fit:function(){return e.fit(),e.pi},contain:function(){return e.contain(),e.pi},center:function(){return e.center(),e.pi},updateBBox:function(){return e.updateBBox(),e.pi},resize:function(){return e.resize(),e.pi},getSizes:function(){return{width:e.width,height:e.height,realZoom:e.getZoom(),viewBox:e.viewport.getViewBox()}},destroy:function(){return e.destroy(),e.pi}}),this.publicInstance},a=[],d=function(e,t){var n,o=i.getSvg(e);if(o===null)return null;for(n=a.length-1;n>=0;n--)if(a[n].svg===o)return a[n].instance.getPublicInstance();return a.push({svg:o,instance:new s(o,t)}),a[a.length-1].instance.getPublicInstance()},t.exports=d},{"./control-icons":1,"./shadow-viewport":2,"./svg-utilities":5,"./uniwheel":6,"./utilities":7}],5:[function(e,t){var s=e("./utilities"),o="unknown";(!1||!!document.documentMode)&&(o="ie"),t.exports={svgNS:"http://www.w3.org/2000/svg",xmlNS:"http://www.w3.org/XML/1998/namespace",xmlnsNS:"http://www.w3.org/2000/xmlns/",xlinkNS:"http://www.w3.org/1999/xlink",evNS:"http://www.w3.org/2001/xml-events",getBoundingClientRectNormalized:function(e){if(e.clientWidth&&e.clientHeight)return{width:e.clientWidth,height:e.clientHeight};if(!e.getBoundingClientRect())throw new Error("Cannot get BoundingClientRect for SVG.");return e.getBoundingClientRect()},getOrCreateViewport:function(e,t){var o,i,a,r,c,n=null;if(s.isElement(t)?n=t:n=e.querySelector(t),n||(i=Array.prototype.slice.call(e.childNodes||e.children).filter(function(e){return e.nodeName!=="defs"&&e.nodeName!=="#text"}),i.length===1&&i[0].nodeName==="g"&&i[0].getAttribute("transform")===null&&(n=i[0])),!n){if(c="viewport-"+(new Date).toISOString().replace(/\D/g,""),n=document.createElementNS(this.svgNS,"g"),n.setAttribute("id",c),o=e.childNodes||e.children,!!o&&o.length>0)for(a=o.length;a>0;a--)o[o.length-a].nodeName!=="defs"&&n.appendChild(o[o.length-a]);e.appendChild(n)}return r=[],n.getAttribute("class")&&(r=n.getAttribute("class").split(" ")),~r.indexOf("svg-pan-zoom_viewport")||(r.push("svg-pan-zoom_viewport"),n.setAttribute("class",r.join(" "))),n},setupSvgAttributes:function(e){if(e.setAttribute("xmlns",this.svgNS),e.setAttributeNS(this.xmlnsNS,"xmlns:xlink",this.xlinkNS),e.setAttributeNS(this.xmlnsNS,"xmlns:ev",this.evNS),e.parentNode!==null){var t=e.getAttribute("style")||"";t.toLowerCase().indexOf("overflow")===-1&&e.setAttribute("style","overflow: hidden; "+t)}},internetExplorerRedisplayInterval:300,refreshDefsGlobal:s.throttle(function(){for(var e,n=document.querySelectorAll("defs"),s=n.length,t=0;t<s;t++)e=n[t],e.parentNode.insertBefore(e,e)},this?this.internetExplorerRedisplayInterval:null),setCTM:function(e,t,n){var i=this,s="matrix("+t.a+","+t.b+","+t.c+","+t.d+","+t.e+","+t.f+")";e.setAttributeNS(null,"transform",s),"transform"in e.style?e.style.transform=s:"-ms-transform"in e.style?e.style["-ms-transform"]=s:"-webkit-transform"in e.style&&(e.style["-webkit-transform"]=s),o==="ie"&&!!n&&(n.parentNode.insertBefore(n,n),window.setTimeout(function(){i.refreshDefsGlobal()},i.internetExplorerRedisplayInterval))},getEventPoint:function(e,t){var n=t.createSVGPoint();return s.mouseAndTouchNormalize(e,t),n.x=e.clientX,n.y=e.clientY,n},getSvgCenterPoint:function(e,t,n){return this.createSVGPoint(e,t/2,n/2)},createSVGPoint:function(e,t,n){var s=e.createSVGPoint();return s.x=t,s.y=n,s}}},{"./utilities":7}],6:[function(e,t){t.exports=function(){var e,s,o,n="",t=[],a={passive:!0},i={passive:!1};window.addEventListener?(s="addEventListener",o="removeEventListener"):(s="attachEvent",o="detachEvent",n="on"),e="onwheel"in document.createElement("div")?"wheel":document.onmousewheel!==0[0]?"mousewheel":"DOMMouseScroll";function l(n,s){var o=function(t){!t&&(t=window.event);var n={originalEvent:t,target:t.target||t.srcElement,type:"wheel",deltaMode:t.type=="MozMousePixelScroll"?0:1,deltaX:0,delatZ:0,preventDefault:function(){t.preventDefault?t.preventDefault():t.returnValue=!1}};return e=="mousewheel"?(n.deltaY=-1/40*t.wheelDelta,t.wheelDeltaX&&(n.deltaX=-1/40*t.wheelDeltaX)):n.deltaY=t.detail,s(n)};return t.push({element:n,fn:o}),o}function d(e){for(var n=0;n<t.length;n++)if(t[n].element===e)return t[n].fn;return function(){}}function u(e){for(var n=0;n<t.length;n++)if(t[n].element===e)return t.splice(n,1)}function r(t,o,r,c){var d;e==="wheel"?d=r:d=l(t,r),t[s](n+o,d,c?a:i)}function c(t,s,r,c){var l;e==="wheel"?l=r:l=d(t),t[o](n+s,l,c?a:i),u(t)}function h(t,n,s){r(t,e,n,s),e=="DOMMouseScroll"&&r(t,"MozMousePixelScroll",n,s)}function m(t,n,s){c(t,e,n,s),e=="DOMMouseScroll"&&c(t,"MozMousePixelScroll",n,s)}return{on:h,off:m}}()},{}],7:[function(e,t){t.exports={extend:function(e,t){e=e||{};for(var n in t)this.isObject(t[n])?e[n]=this.extend(e[n],t[n]):e[n]=t[n];return e},isElement:function(e){return e instanceof HTMLElement||e instanceof SVGElement||e instanceof SVGSVGElement||e&&typeof e=="object"&&e!==null&&e.nodeType===1&&typeof e.nodeName=="string"},isObject:function(e){return Object.prototype.toString.call(e)==="[object Object]"},isNumber:function(e){return!isNaN(parseFloat(e))&&isFinite(e)},getSvg:function(e){var t,n;if(this.isElement(e))t=e;else if(typeof e=="string"||e instanceof String){if(t=document.querySelector(e),!t){throw new Error("Provided selector did not find any elements. Selector: "+e);return null}}else{throw new Error("Provided selector is not an HTML object nor String");return null}if(t.tagName.toLowerCase()==="svg")n=t;else if(t.tagName.toLowerCase()==="object")n=t.contentDocument.documentElement;else if(t.tagName.toLowerCase()==="embed")n=t.getSVGDocument().documentElement;else{throw t.tagName.toLowerCase()==="img"?new Error('Cannot script an SVG in an "img" element. Please use an "object" element or an in-line SVG.'):new Error("Cannot get SVG.");return null}return n},proxy:function(e,t){return function(){return e.apply(t,arguments)}},getType:function(e){return Object.prototype.toString.apply(e).replace(/^\[object\s/,"").replace(/\]$/,"")},mouseAndTouchNormalize:function(e,t){if(e.clientX===0[0]||e.clientX===null)if(e.clientX=0,e.clientY=0,e.touches!==0[0]&&e.touches.length){if(e.touches[0].clientX!==0[0])e.clientX=e.touches[0].clientX,e.clientY=e.touches[0].clientY;else if(e.touches[0].pageX!==0[0]){var n=t.getBoundingClientRect();e.clientX=e.touches[0].pageX-n.left,e.clientY=e.touches[0].pageY-n.top}}else e.originalEvent!==0[0]&&e.originalEvent.clientX!==0[0]&&(e.clientX=e.originalEvent.clientX,e.clientY=e.originalEvent.clientY)},isDblClick:function(e,t){if(e.detail===2)return!0;if(t!=null){var n=e.timeStamp-t.timeStamp,s=Math.sqrt((e.clientX-t.clientX)**2+(e.clientY-t.clientY)**2);return n<250&&s<10}return!1},now:Date.now||function(){return(new Date).getTime()},throttle:function(e,t,n){var o,i,r,l,c=this,s=null,a=0;return n||(n={}),l=function(){a=n.leading===!1?0:c.now(),s=null,r=e.apply(o,i),s||(o=i=null)},function(){var d,u=c.now();return!a&&n.leading===!1&&(a=u),d=t-(u-a),o=this,i=arguments,d<=0||d>t?(clearTimeout(s),s=null,a=u,r=e.apply(o,i),s||(o=i=null)):!s&&n.trailing!==!1&&(s=setTimeout(l,d)),r}},createRequestAnimationFrame:function(e){var t=null;return e!=="auto"&&e<60&&e>1&&(t=Math.floor(1e3/e)),t===null?window.requestAnimationFrame||s(33):s(t)}};function s(e){return function(t){window.setTimeout(t,e)}}},{}]},{},[3])
"""

# Note: Html replaced at the end of better html
var_better_html = "</div></div></div></div><script>"
var_better_html += svg_pan_zoom
var_better_html += """</script>
<script>
    window.addEventListener("load", function () {
        const svgs = document.getElementById("svg-container").children;
        const UA = window.navigator.userAgent;
        const ua = UA.indexOf("rv:11") + UA.indexOf("Firefox") >= 0;
        let svgcount = document.getElementById("svg-container").childElementCount;
        var styleArr = [];
        var heightArr = [];
        var navBar = document.getElementById("navBar");
        var conInfo = document.getElementById("content-info");
        
        function RunAtStartup() {
            for (var i = 0; i < svgcount; i++) {
                styleArr[i] = {
                    width: svgs[i].getAttribute("width"),
                    height: svgs[i].getAttribute("height"),
                };
            }
            
            renavstyle();
            var sideWidth = navBar.offsetWidth;
            var sideHeight = navBar.offsetHeight;
            document.getElementById("content-info").style.marginRight =
                sideWidth + "px";
            document.getElementById("main-content").style.marginRight =
                sideWidth + "px";
            document.getElementById("main-content").style.marginBottom =
                sideHeight + "px";
            resvgstyle();
            doscroll();
        }
        
        RunAtStartup();
        
        let resizeTimeout;
        let resizeTimeoutLate;
        window.addEventListener("resize", function () {{
            clearTimeout(resizeTimeout); // Cancela cualquier timeout anterior
            clearTimeout(resizeTimeoutLate);
            resizeTimeout = setTimeout(function () {{
                RunAtStartup();
            }}, 250); // 250ms después de que termine
            resizeTimeoutLate = setTimeout(function () {{
                RunAtStartup();
            }}, 350); // 350ms después de que termine
        }});
        
        window.onscroll = renavstyle;
        
        //Center SVG inside SVG-viewer
        document.querySelectorAll(".SVG-viewer").forEach((viewer) => {
            // Extraer el número del ID del viewer (asumiendo formato "SVGiewer4", "SVGiewer5", etc.)
            const viewerId = viewer.id;
            const containerNumber = viewerId.replace("SVGiewer", "");
            const zoomContainer = window[`zoomContainer${containerNumber}`];

            if (zoomContainer) {
                const rectElement = viewer.querySelector('svg>g>rect');
                
                if (rectElement) {
                    zoomContainer.zoom(1);
                    zoomContainer.pan({
                        x:
                            (viewer.offsetWidth -
                                zoomContainer.getSizes().viewBox.width *
                                    zoomContainer.getSizes().realZoom) /
                            2,
                        y:
                            (viewer.offsetHeight -
                                zoomContainer.getSizes().viewBox.height *
                                    zoomContainer.getSizes().realZoom) /
                            2,
                    });
                } else {
                    zoomContainer.resetZoom();
                    zoomContainer.fit();
                    zoomContainer.center();
                }
            }
        });
        function recontainstyle() {
            var topHeight = conInfo.clientHeight;
            var svgHeight = 0;
            for (var i = 0; i < svgcount; i++) {
                heightArr[i] = svgs[i].getBoundingClientRect().height + 10;
                svgHeight +=
                    svgs[i].clientHeight || svgs[i].getBoundingClientRect().height;
            }
            var fullHeight = svgHeight + Number(topHeight);
            if (fullHeight < window.innerHeight) {
                document.getElementById("main-content").style.position = "absolute";
                document.getElementById("main-content").style.top =
                    topHeight + "px";
            } else {
                document.getElementById("main-content").style.position = "";
            }
        }
        function resvgstyle() {
            var sideWidth = navBar.offsetWidth + 20;
            for (var i = 0; i < svgcount; i++) {
                var oriWidth = styleArr[i].width;
                var oriHeight = styleArr[i].height;
                var percent = oriHeight / oriWidth;
                var innerWidth = document.body.offsetWidth - sideWidth;
                if (innerWidth <= oriWidth) {
                    svgs[i].removeAttribute("width");
                    svgs[i].removeAttribute("height");
                    if (ua) {
                        svgs[i].setAttribute("height", innerWidth * percent);
                    }
                } else {
                    svgs[i].setAttribute("width", oriWidth);
                    svgs[i].setAttribute("height", oriHeight);
                }
            }
            recontainstyle();
        }
        function renavstyle() {
            var topHeight = conInfo.clientHeight;
            var scrollTop =
                document.body.scrollTop || document.documentElement.scrollTop;
            if (scrollTop > topHeight) {
                document.getElementById("navBar").style.top = 0 + "px";
            } else {
                document.getElementById("navBar").style.top =
                    topHeight - scrollTop + "px";
            }
            doscroll();
        }
        function doscroll() {
            var topHeight = conInfo.clientHeight;
            var scrollTop =
                document.body.scrollTop || document.documentElement.scrollTop;
            if (
                window.innerHeight + window.pageYOffset >=
                document.documentElement.scrollHeight - 5
            ) {
                document
                    .querySelector("#nav-thumbs .selected")
                    ?.classList.remove("selected");
                document
                    .querySelector(".nav-thumb:nth-of-type(" + svgcount + ")")
                    .classList.add("selected");
            } else if (document.body.scrollTop <= 5) {
                document
                    .querySelector("#nav-thumbs .selected")
                    ?.classList.remove("selected");
                document
                    .querySelector(".nav-thumb:nth-of-type(1)")
                    .classList.add("selected");
            } else {
                for (var i = 0; i < svgcount; i++) {
                    var sum = 0;
                    for (var j = 0; j <= i; j++) {
                        sum += heightArr[j];
                    }
                    if (scrollTop + window.innerHeight / 2 - topHeight - sum < 0) {
                        var sub = Number(i) + 1;
                        if (document.querySelector("#nav-thumbs .selected")) {
                            document
                                .querySelector("#nav-thumbs .selected")
                                .classList.remove("selected");
                        }
                        if (
                            document.querySelector(
                                ".nav-thumb:nth-of-type(" + sub + ")"
                            )
                        ) {
                            document
                                .querySelector(
                                    ".nav-thumb:nth-of-type(" + sub + ")"
                                )
                                .classList.add("selected");
                        }
                        break;
                    }
                }
            }
            document.querySelector("#nav-thumbs .selected")?.scrollIntoView({
                behavior: "smooth", // opcional: animado
                block: "center", // centra verticalmente
                inline: "center", // centra horizontalmente
            });
        }
        var navs = document.querySelectorAll(".nav-thumb");
        for (i = 0; i < navs.length; i++) {
            navs[i].children[0].onclick = function () {
                document
                    .querySelector("#nav-thumbs .selected")
                    .classList.remove("selected");
                this.parentNode.classList.add("selected");
            };
        }
        /* Hacer que se desplaze lentamente */
        document.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", function (e) {
                const href = this.getAttribute("href") || this.getAttribute("xlink:href");
                
                // Only process if it is an internal link (starts with #)
                if (href && href.startsWith("#")) {
                    e.preventDefault(); // prevent instant jump

                    const targetId = href.substring(1); // substring removes the "#"
                    const target = document.getElementById(targetId);

                    if (target) {
                        const rect = target.getBoundingClientRect();
                        const scrollTop =
                            window.pageYOffset || document.documentElement.scrollTop;
                        const offset =
                            rect.top +
                            scrollTop -
                            window.innerHeight / 2 +
                            rect.height / 2;

                        window.scrollTo({
                            top: offset,
                            behavior: "smooth",
                        });
                    }
                }
            });
        });
    });
</script>
</body></html>"""

# Note: Default SVG Page
svg_page_default = """
<svg width="1122" height="793" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
    <rect fill="#0b050b" height="794" width="1123" x="0" y="0"/>
</svg>
"""

# Note: Default HTML in html_content
html_content_default = """
<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>Structure</title><style>
        body{
            margin: 0;
        }
        #content-info{
            width: auto;
            margin: 0 auto;
            text-align: center;
        }
        #author-info{
            white-space: nowrap;
            text-overflow: ellipsis;
            overflow: hidden;
        }
        #title{
            text-overflow: ellipsis;
            white-space: nowrap;
            overflow: hidden;
            padding-top: 10px;
            margin-bottom: 2px;
            font-size: 34px;
            color: #505050;
        }
        .text{
            white-space:nowrap;
            text-overflow: ellipsis;
            display: inline-block;
            margin-right: 20px;
            margin-bottom: 2px;
            font-size: 20px;
            color: #8c8c8c;
        }
        #navBar{
            position: fixed;
            right:0;
            bottom: 0;
            background-color: #f0f3f4;
            overflow-y: auto;
            text-align: center;
        }
        #svg-container{
            width: 100%;
            min-width: 0;
            margin: 0 10px;
        }
        #nav-thumbs{
            padding: 0 5px;
        }
        .nav-thumb{
            position: relative;
            margin: 10px auto;
        }
        .nav-thumb >p{
            text-align: center;
            font-size: 12px;
            margin: 4px 0 0 0;
        }
        .nav-thumb >div{
            position: relative;
            display: inline-block;
            border: 1px solid #c6cfd5;
        }
        .nav-thumb img{
            display: block;
        }
        .nav-thumb span{
            pointer-events: none;
        }
        #main-content{
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #d0cfd8;
            display: flex;
            height: auto;
            flex-flow: row wrap;
            text-align:center;
        }
        #svg-container >svg{
            display: block;
            margin:10px auto;
            margin-bottom: 0;
        }
        #copyright{
            bottom: 0;
            left: 50%;
            margin: 5px auto;
            font-size: 16px;
            color: #515151;
        }
        #copyright >a{
            text-decoration: none;
            color: #77C;
        }
        .number{
            position: absolute;
            top:0;
            left:0;
            border-top:22px solid #76838f;
            border-right: 22px solid transparent;
        }
        .pagenum{
            font-size: 12px;
            color: #fff;
            position: absolute;
            top: -23px;
            left: 2px;
        }
        #navBar::-webkit-scrollbar{
            width: 8px;
            background-color: #f5f5f5;
        }
        #navBar::-webkit-scrollbar-track{
            -webkit-box-shadow: inset 0 0 4px rgba(0,0,0,.3);
            border-radius: 8px;
            background-color: #fff;
        }
        #navBar::-webkit-scrollbar-thumb{
            border-radius: 8px;
            -webkit-box-shadow: inset 0 0 4px rgba(0,0,0,.3);
            background-color: #6b6b70;
        }
        #navBar::-webkit-scrollbar-thumb:hover{
            background-color: #4a4a4f;
        }
        .nav-thumb >div:hover{
            box-shadow:1px 1px 4px rgba(0,0,0,.4);
        }
        .selected .number{
            border-color: #08a1ef transparent;
        }
</style>
"""
html_content_default += style_added_page
html_content_default += """
<style type="text/css">body {-webkit-user-select: none; -khtml-user-select: none; -ms-user-select: none; user-select: none; cursor: default;}</style><style type="text/css">body {-webkit-user-select: none; -khtml-user-select: none; -ms-user-select: none; user-select: none; cursor: default;}</style><style type="text/css">body {-webkit-user-select: none; -khtml-user-select: none; -ms-user-select: none; user-select: none; cursor: default;}</style><style type="text/css">body {-webkit-user-select: none; -khtml-user-select: none; -ms-user-select: none; user-select: none; cursor: default;}</style></head><body><div id="main-area"><div id="content-info" style="margin-right: 92px;"></div><div id="main-content" style="margin-right: 92px; margin-bottom: 654px; top: 0px;"><div id="svg-container"><div id="SVGiewer1" class="SVG-viewer" style="width: 100%; height: 523.2px; position: relative;">
            
<svg width="1122" height="793" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" id="page1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ev="http://www.w3.org/2001/xml-events" style="overflow: hidden; " xmlns:ev="http://www.w3.org/2001/xml-events"><g id="viewport-20250819011714902" class="svg-pan-zoom_viewport" transform="matrix(0.6586901763224181,0,0,0.6586901763224181,63.14546599496225,0)" style="transform: matrix(0.65869, 0, 0, 0.65869, 63.1455, 0);">
    <rect fill="#0b050b" height="794" width="1123" x="0" y="0"></rect>
</g></svg>

            <button style="position: absolute; bottom: 10px; right: 10px;background: transparent; border: 0;">
                <svg id="zoom-in1" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M4.929 4.929A10 10 0 1 1 19.07 19.07A10 10 0 0 1 4.93 4.93zM13 9a1 1 0 1 0-2 0v2H9a1 1 0 1 0 0 2h2v2a1 1 0 1 0 2 0v-2h2a1 1 0 1 0 0-2h-2z"></path></svg>
                <svg id="zoom-out1" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34A10 10 0 1 1 2 12l.005-.324A10 10 0 0 1 17 3.34M16.5 11.5H8.5a0.5 0.5 0 0 0-0.5 0.5v1a0.5 0.5 0 0 0 0.5 0.5h8a0.5 0.5 0 0 0 0.5-0.5v-1a0.5 0.5 0 0 0-0.5-0.5"></path></svg>
                <svg id="reset_zoom1" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34a10 10 0 1 1-14.995 8.984L2 12l.005-.324A10 10 0 0 1 17 3.34m-6.489 5.8a1 1 0 0 0-1.218 1.567L10.585 12l-1.292 1.293l-.083.094a1 1 0 0 0 1.497 1.32L12 13.415l1.293 1.292l.094.083a1 1 0 0 0 1.32-1.497L13.415 12l1.292-1.293l.083-.094a1 1 0 0 0-1.497-1.32L12 10.585l-1.293-1.292l-.094-.083z"></path></svg>
            </button>
            <script>
            window.addEventListener('load', function () {
                
                if (!document.getElementById('page1')){
                    return;
                }
                
                window.zoomContainer1 = svgPanZoom("#page1");
                
                let viewer1 = document.getElementById('SVGiewer1');
                let rectElement = viewer1.querySelector('svg>g>rect');
                let lastWidth = viewer1.offsetWidth; // Track the last width

                function proper_height(){
                    rectElement = viewer1.querySelector('svg>g>rect');
                    if (rectElement) {
                        // Get the dimensions of the rect
                        const rectWidth = rectElement.getAttribute('width') || rectElement.width.baseVal.value;
                        const rectHeight = rectElement.getAttribute('height') || rectElement.height.baseVal.value;
                        
                        // Calculate the ratio (height/width)
                        const aspectRatio = rectHeight / rectWidth;
                        
                        // Get the current width of the SVG-viewer
                        const viewerWidth = viewer1.offsetWidth;
                        
                        if (viewerWidth > 0) {
                            // Calculate the proportional height
                            const proportionalHeight = viewerWidth * aspectRatio;
                            
                            // Calculate 80vh in pixels
                            const maxHeight = window.innerHeight * 0.8;
                            
                            // Apply proportional height with limit of 80vh
                            const finalHeight = Math.min(proportionalHeight, maxHeight);
                            viewer1.style.height = finalHeight + 'px';
                        }
                    }
                }
                
                let resizeTimeout;
                window.addEventListener("resize", function () {
                    clearTimeout(resizeTimeout); // Cancel any previous timeout
                    resizeTimeout = setTimeout(function () {
                        viewer1 = document.getElementById('SVGiewer1');
                        const currentWidth = viewer1.offsetWidth;

                        // Only execute if the width has changed
                        if (currentWidth !== lastWidth) {
                            if (window.zoomContainer1) {
                                window.zoomContainer1.destroy();
                            }
                            proper_height();
                            viewer1.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {
                                viewport.replaceWith(...viewport.childNodes);
                            });
                            window.zoomContainer1 = svgPanZoom("#page1");
                            center_svg();
                            lastWidth = currentWidth; // Update the last width
                        }
                    }, 280); // 280ms after finishing
                });
                
                proper_height();

                // Button listeners
                document.getElementById('zoom-in1').addEventListener('click', function(ev){
                    ev.preventDefault()
                    window.zoomContainer1.zoomIn()
                });

                document.getElementById('zoom-out1').addEventListener('click', function(ev){
                    ev.preventDefault()
                    window.zoomContainer1.zoomOut()
                });
                
                function center_svg(){
                    const zoomContainer = window.zoomContainer1;
                    rectElement = viewer1.querySelector('svg>g>rect');
                    
                    if (zoomContainer && rectElement) {
                        zoomContainer.zoom(1);
                        zoomContainer.pan({
                            x: (viewer1.offsetWidth - (zoomContainer.getSizes().viewBox.width * zoomContainer.getSizes().realZoom))/2, 
                            y: (viewer1.offsetHeight - (zoomContainer.getSizes().viewBox.height * zoomContainer.getSizes().realZoom))/2 
                        });
                    }else{
                        window.zoomContainer1.resetZoom();
                        window.zoomContainer1.fit();
                        window.zoomContainer1.center();
                    }
                }

                document.getElementById('reset_zoom1').addEventListener('click', function(ev){
                    ev.preventDefault()
                    center_svg();
                });
                
                center_svg();
            });
            </script>
            </div><div id="SVGiewer2" class="SVG-viewer" style="width: 100%; height: 523.2px; position: relative;">
            <svg width="1122" height="793" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" id="page2" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:ev="http://www.w3.org/2001/xml-events" style="overflow: hidden; " xmlns:ev="http://www.w3.org/2001/xml-events"><g id="viewport-20250819011714902" class="svg-pan-zoom_viewport" transform="matrix(0.6586901763224181,0,0,0.6586901763224181,63.14546599496225,0)" style="transform: matrix(0.65869, 0, 0, 0.65869, 63.1455, 0);">
    <rect fill="#0b050b" height="794" width="1123" x="0" y="0"></rect>
</g></svg>
            <button style="position: absolute; bottom: 10px; right: 10px;background: transparent; border: 0;">
                <svg id="zoom-in2" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M4.929 4.929A10 10 0 1 1 19.07 19.07A10 10 0 0 1 4.93 4.93zM13 9a1 1 0 1 0-2 0v2H9a1 1 0 1 0 0 2h2v2a1 1 0 1 0 2 0v-2h2a1 1 0 1 0 0-2h-2z"></path></svg>
                <svg id="zoom-out2" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34A10 10 0 1 1 2 12l.005-.324A10 10 0 0 1 17 3.34M16.5 11.5H8.5a0.5 0.5 0 0 0-0.5 0.5v1a0.5 0.5 0 0 0 0.5 0.5h8a0.5 0.5 0 0 0 0.5-0.5v-1a0.5 0.5 0 0 0-0.5-0.5"></path></svg>
                <svg id="reset_zoom2" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" style="background: black; border-radius: 50%;"><path fill="#fff" d="M17 3.34a10 10 0 1 1-14.995 8.984L2 12l.005-.324A10 10 0 0 1 17 3.34m-6.489 5.8a1 1 0 0 0-1.218 1.567L10.585 12l-1.292 1.293l-.083.094a1 1 0 0 0 1.497 1.32L12 13.415l1.293 1.292l.094.083a1 1 0 0 0 1.32-1.497L13.415 12l1.292-1.293l.083-.094a1 1 0 0 0-1.497-1.32L12 10.585l-1.293-1.292l-.094-.083z"></path></svg>
            </button>
            <script>
            window.addEventListener('load', function () {
                
                if (!document.getElementById('page2')){
                    return;
                }
                
                window.zoomContainer2 = svgPanZoom("#page2");
                
                let viewer2 = document.getElementById('SVGiewer2');
                let rectElement = viewer2.querySelector('svg>g>rect');
                let lastWidth = viewer2.offsetWidth; // Track the last width

                function proper_height(){
                    rectElement = viewer2.querySelector('svg>g>rect');
                    if (rectElement) {
                        // Get the dimensions of the rect
                        const rectWidth = rectElement.getAttribute('width') || rectElement.width.baseVal.value;
                        const rectHeight = rectElement.getAttribute('height') || rectElement.height.baseVal.value;
                        
                        // Calculate the ratio (height/width)
                        const aspectRatio = rectHeight / rectWidth;
                        
                        // Get the current width of the SVG-viewer
                        const viewerWidth = viewer2.offsetWidth;
                        
                        if (viewerWidth > 0) {
                            // Calculate the proportional height
                            const proportionalHeight = viewerWidth * aspectRatio;
                            
                            // Calculate 80vh in pixels
                            const maxHeight = window.innerHeight * 0.8;
                            
                            // Apply proportional height with limit of 80vh
                            const finalHeight = Math.min(proportionalHeight, maxHeight);
                            viewer2.style.height = finalHeight + 'px';
                        }
                    }
                }
                
                let resizeTimeout;
                window.addEventListener("resize", function () {
                    clearTimeout(resizeTimeout); // Cancel any previous timeout
                    resizeTimeout = setTimeout(function () {
                        viewer2 = document.getElementById('SVGiewer2');
                        const currentWidth = viewer2.offsetWidth;

                        // Only execute if the width has changed
                        if (currentWidth !== lastWidth) {
                            if (window.zoomContainer2) {
                                window.zoomContainer2.destroy();
                            }
                            proper_height();
                            viewer2.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {
                                viewport.replaceWith(...viewport.childNodes);
                            });
                            window.zoomContainer2 = svgPanZoom("#page2");
                            center_svg();
                            lastWidth = currentWidth; // Update the last width
                        }
                    }, 280); // 280ms after finishing
                });
                
                proper_height();

                // Button listeners
                document.getElementById('zoom-in2').addEventListener('click', function(ev){
                    ev.preventDefault()
                    window.zoomContainer2.zoomIn()
                });

                document.getElementById('zoom-out2').addEventListener('click', function(ev){
                    ev.preventDefault()
                    window.zoomContainer2.zoomOut()
                });
                
                function center_svg(){
                    const zoomContainer = window.zoomContainer2;
                    rectElement = viewer2.querySelector('svg>g>rect');
                    
                    if (zoomContainer && rectElement) {
                        zoomContainer.zoom(1);
                        zoomContainer.pan({
                            x: (viewer2.offsetWidth - (zoomContainer.getSizes().viewBox.width * zoomContainer.getSizes().realZoom))/2, 
                            y: (viewer2.offsetHeight - (zoomContainer.getSizes().viewBox.height * zoomContainer.getSizes().realZoom))/2 
                        });
                    }else{
                        window.zoomContainer2.resetZoom();
                        window.zoomContainer2.fit();
                        window.zoomContainer2.center();
                    }
                }

                document.getElementById('reset_zoom2').addEventListener('click', function(ev){
                    ev.preventDefault()
                    center_svg();
                });
                
                center_svg();
            });
            </script>
            </div></div></div><div id="navBar" style="top: 0px;"><div id="nav-thumbs"><div class="nav-thumb" data-original-index="1" draggable="true"><div><span class="number"><span class="pagenum">1</span></span><a href="#page1" draggable="false"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAABqCAYAAABeUaiAAAAC80lEQVR4AeySQWrEMBAETb6y5As57P/vYf+y92SzYHQRgkhySzNdIWaNjTXT1fVx/7r/cMFgtgMfx+vv8f04uGAwy4Hn83m8xXq5xT8EphJArKk4OewkgFgnCX6nEkCsqTg57CSAWCeJ7L/ifIglBu4yDrFcmhbnRCwxcJdxiOXStDgnYomBu4xDLJemxTkRSwy8jMt9h1i5+12WDrGWoc89GLFy97ssHWItQ597MGLl7ndZOsRahj73YMQq/XI3kQBiTYTJUYUAYhUW3E0kgFgTYXJUIYBYhQV3Ewkg1kSYHFUIIFZhwd1EAluLNTEnR4kJIJYYuMs4xHJpWpwTscTAXcYhlkvT4pyIJQbuMg6xXJoW5/yfWOLlGBeXAGLF7W7rzRFr63riLodYcbvbenPE2rqeuMshVtzutt4csbauZ9lyw4MRaxghB9QIIFaNCs+GCSDWMEIOqBFArBoVng0TQKxhhBxQI4BYNSo8GyaAWMMINQdEm4JY0RoLsi9iBSkq2pqIFa2xIPsiVpCioq2JWNEaC7IvYgUpKtqaiNXbGN81CSBWEw8vewkgVi85vmsSQKwmHl72EkCsXnJ81ySAWE08vOwlgFi95PiuSSCRWM2cvBQTQCwxcJdxiOXStDgnYomBu4xDLJemxTkRSwzcZRxiuTQtznmlWOIojNuJAGLt1EaiXRArUZk7RUGsndpItAtiJSpzpyiItVMbiXZBrERlLotSGYxYFSg8GieAWOMMOaFCALEqUHg0TgCxxhlyQoUAYlWg8GicAGKNM+SECgHEqkCJ/2h9AsRa30HKDRArZa3rQyHW+g5SboBYKWtdHwqx1neQcgPESlnr+lCIpenAbgpi2VWuCYxYGs52UxDLrnJNYMTScLabglh2lWsCI5aGs90UW7HsmhYHRiwxcJdxiOXStDgnYomBu4xDLJemxTkRSwzcZRxiuTQtzrmPWOLgjLuWAGJdy9f2dMSyrf7a4G+xbp+3gwsGsxz4U/YXAAD//wSH6KcAAAAGSURBVAMAvfykBV+l+v8AAAAASUVORK5CYII=" draggable="false"></a></div><p title="Double click to edit" style="cursor: pointer; position: relative;">page1</p></div><div class="nav-thumb selected" data-original-index="2"><div><span class="number"><span class="pagenum">2</span></span><a href="#page2" draggable="false"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAABqCAYAAABeUaiAAAAC+ElEQVR4AeySQYrDMBAETT4U9rKHQP5/XPKePewmOVgXIYgltzTTFQgIG2umq+tyv91/b9+3P/4wGOXAy6nL9vw9fh4bfxiMcuCp1PYW63XgD4GRBBBrJE3u2gkg1o6Cw0gCiDWSJnftBBBrR5H8II6HWGLgLuMQy6VpcU7EEgN3GYdYLk2LcyKWGLjLOMRyaVqcE7HEwMu43CfEyt3vtHSINQ197sGIlbvfaekQaxr63IMRK3e/09Ih1jT0uQcjVumX00ACiDUQJlcVAohVWHAaSACxBsLkqkIAsQoLTgMJINZAmFxVCCBWYcFpIIGlxRqYk6vEBBBLDNxlHGK5NC3OiVhi4C7jEMulaXFOxBIDdxmHWC5Ni3N+JpZ4OcbFJYBYcbtbenPEWrqeuMshVtzult4csZauJ+5yiBW3u6U3R6yl65m2XPdgxOpGyAU1AohVo8KzbgKI1Y2QC2oEEKtGhWfdBBCrGyEX1AggVo0Kz7oJIFY3Qs0F0aYgVrTGguyLWEGKirYmYkVrLMi+iBWkqGhrIla0xoLsi1hBioq2JmIdbYzvmgQQq4mHl0cJINZRcnzXJIBYTTy8PEoAsY6S47smAcRq4uHlUQKIdZQc3zUJJBKrmZOXYgKIJQbuMg6xXJoW50QsMXCXcYjl0rQ4J2KJgbuMQyyXpsU5zxRLHIVxKxFArJXaSLQLYiUqc6UoiLVSG4l2QaxEZa4UBbFWaiPRLoiVqMxpUSqDEasChUf9BBCrnyE3VAggVgUKj/oJIFY/Q26oEECsChQe9RNArH6G3FAhgFgVKPEfzU+AWPM7SLkBYqWsdX4oxJrfQcoNECtlrfNDIdb8DlJugFgpa50fCrE0HdhNQSy7yjWBEUvD2W4KYtlVrgmMWBrOdlMQy65yTWDE0nC2m2Irll3T4sCIJQbuMg6xXJoW50QsMXCXcYjl0rQ4J2KJgbuMQyyXpsU51xFLHJxx5xJArHP52t6OWLbVnxv8Ldb167rxh8EoB17K/gMAAP//Lom99gAAAAZJREFUAwCBBrYFJf87MwAAAABJRU5ErkJggg==" draggable="false"></a></div><p title="Double click to edit" style="cursor: pointer;">page2</p></div></div></div></div><script>
"""
html_content_default += svg_pan_zoom
html_content_default += """
</script>
<script>
    window.addEventListener("load", function () {
        const svgs = document.getElementById("svg-container").children;
        const UA = window.navigator.userAgent;
        const ua = UA.indexOf("rv:11") + UA.indexOf("Firefox") >= 0;
        let svgcount = document.getElementById("svg-container").childElementCount;
        var styleArr = [];
        var heightArr = [];
        var navBar = document.getElementById("navBar");
        var conInfo = document.getElementById("content-info");
        
        function RunAtStartup() {
            for (var i = 0; i < svgcount; i++) {
                styleArr[i] = {
                    width: svgs[i].getAttribute("width"),
                    height: svgs[i].getAttribute("height"),
                };
            }
            
            renavstyle();
            var sideWidth = navBar.offsetWidth;
            var sideHeight = navBar.offsetHeight;
            document.getElementById("content-info").style.marginRight =
                sideWidth + "px";
            document.getElementById("main-content").style.marginRight =
                sideWidth + "px";
            document.getElementById("main-content").style.marginBottom =
                sideHeight + "px";
            resvgstyle();
            doscroll();
        }
        
        RunAtStartup();
        
        let resizeTimeout;
        let resizeTimeoutLate;
        window.addEventListener("resize", function () {{
            clearTimeout(resizeTimeout); // Cancel any previous timeouts
            clearTimeout(resizeTimeoutLate);
            resizeTimeout = setTimeout(function () {{
                RunAtStartup();
            }}, 250); // 250ms after it ends
            resizeTimeoutLate = setTimeout(function () {{
                RunAtStartup();
            }}, 350); // 350ms after it ends
        }});
        
        window.onscroll = renavstyle;
        
        //Center SVG inside SVG-viewer
        document.querySelectorAll(".SVG-viewer").forEach((viewer) => {
            // Extraer el número del ID del viewer (asumiendo formato "SVGiewer4", "SVGiewer5", etc.)
            const viewerId = viewer.id;
            const containerNumber = viewerId.replace("SVGiewer", "");
            const zoomContainer = window[`zoomContainer${containerNumber}`];

            if (zoomContainer) {
                const rectElement = viewer.querySelector('svg>g>rect');
                
                if (rectElement) {
                    zoomContainer.zoom(1);
                    zoomContainer.pan({
                        x:
                            (viewer.offsetWidth -
                                zoomContainer.getSizes().viewBox.width *
                                    zoomContainer.getSizes().realZoom) /
                            2,
                        y:
                            (viewer.offsetHeight -
                                zoomContainer.getSizes().viewBox.height *
                                    zoomContainer.getSizes().realZoom) /
                            2,
                    });
                } else {
                    zoomContainer.resetZoom();
                    zoomContainer.fit();
                    zoomContainer.center();
                }
            }
        });
        function recontainstyle() {
            var topHeight = conInfo.clientHeight;
            var svgHeight = 0;
            for (var i = 0; i < svgcount; i++) {
                heightArr[i] = svgs[i].getBoundingClientRect().height + 10;
                svgHeight +=
                    svgs[i].clientHeight || svgs[i].getBoundingClientRect().height;
            }
            var fullHeight = svgHeight + Number(topHeight);
            if (fullHeight < window.innerHeight) {
                document.getElementById("main-content").style.position = "absolute";
                document.getElementById("main-content").style.top =
                    topHeight + "px";
            } else {
                document.getElementById("main-content").style.position = "";
            }
        }
        function resvgstyle() {
            var sideWidth = navBar.offsetWidth + 20;
            for (var i = 0; i < svgcount; i++) {
                var oriWidth = styleArr[i].width;
                var oriHeight = styleArr[i].height;
                var percent = oriHeight / oriWidth;
                var innerWidth = document.body.offsetWidth - sideWidth;
                if (innerWidth <= oriWidth) {
                    svgs[i].removeAttribute("width");
                    svgs[i].removeAttribute("height");
                    if (ua) {
                        svgs[i].setAttribute("height", innerWidth * percent);
                    }
                } else {
                    svgs[i].setAttribute("width", oriWidth);
                    svgs[i].setAttribute("height", oriHeight);
                }
            }
            recontainstyle();
        }
        function renavstyle() {
            var topHeight = conInfo.clientHeight;
            var scrollTop =
                document.body.scrollTop || document.documentElement.scrollTop;
            if (scrollTop > topHeight) {
                document.getElementById("navBar").style.top = 0 + "px";
            } else {
                document.getElementById("navBar").style.top =
                    topHeight - scrollTop + "px";
            }
            doscroll();
        }
        function doscroll() {
            var topHeight = conInfo.clientHeight;
            var scrollTop =
                document.body.scrollTop || document.documentElement.scrollTop;
            if (
                window.innerHeight + window.pageYOffset >=
                document.documentElement.scrollHeight - 5
            ) {
                document
                    .querySelector("#nav-thumbs .selected")
                    ?.classList.remove("selected");
                document
                    .querySelector(".nav-thumb:nth-of-type(" + svgcount + ")")
                    .classList.add("selected");
            } else if (document.body.scrollTop <= 5) {
                document
                    .querySelector("#nav-thumbs .selected")
                    ?.classList.remove("selected");
                document
                    .querySelector(".nav-thumb:nth-of-type(1)")
                    .classList.add("selected");
            } else {
                for (var i = 0; i < svgcount; i++) {
                    var sum = 0;
                    for (var j = 0; j <= i; j++) {
                        sum += heightArr[j];
                    }
                    if (scrollTop + window.innerHeight / 2 - topHeight - sum < 0) {
                        var sub = Number(i) + 1;
                        if (document.querySelector("#nav-thumbs .selected")) {
                            document
                                .querySelector("#nav-thumbs .selected")
                                .classList.remove("selected");
                        }
                        if (
                            document.querySelector(
                                ".nav-thumb:nth-of-type(" + sub + ")"
                            )
                        ) {
                            document
                                .querySelector(
                                    ".nav-thumb:nth-of-type(" + sub + ")"
                                )
                                .classList.add("selected");
                        }
                        break;
                    }
                }
            }
            document.querySelector("#nav-thumbs .selected")?.scrollIntoView({
                behavior: "smooth", // optional: animated scroll
                block: "center", // center vertically
                inline: "center", // center horizontally
            });
        }
        var navs = document.querySelectorAll(".nav-thumb");
        for (i = 0; i < navs.length; i++) {
            navs[i].children[0].onclick = function () {
                document
                    .querySelector("#nav-thumbs .selected")
                    .classList.remove("selected");
                this.parentNode.classList.add("selected");
            };
        }
        /* Hacer que se desplaze lentamente */
        document.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", function (e) {
                const href = this.getAttribute("href") || this.getAttribute("xlink:href");

                // Only process if it's an internal link (starts with #)
                if (href && href.startsWith("#")) {
                    e.preventDefault(); // prevent instant jump

                    const targetId = href.substring(1); // substring removes the "#"
                    const target = document.getElementById(targetId);

                    if (target) {
                        const rect = target.getBoundingClientRect();
                        const scrollTop =
                            window.pageYOffset || document.documentElement.scrollTop;
                        const offset =
                            rect.top +
                            scrollTop -
                            window.innerHeight / 2 +
                            rect.height / 2;

                        window.scrollTo({
                            top: offset,
                            behavior: "smooth",
                        });
                    }
                }
            });
        });
    });
</script>
</body></html>
"""

# Note: Js injected in preview
js_injected_preview = """
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

// Function to make elements editable with double click
function makeElementsEditable() {
    // Select all elements that match the pattern
    const elements = document.querySelectorAll("#nav-thumbs > div > p");
    
    elements.forEach(element => {
        // Add event listener for double click
        element.addEventListener('dblclick', function(e) {
            e.preventDefault();
            startEditing(this);
        });

        // Optional: add pointer cursor to indicate it's editable
        element.style.cursor = 'pointer';
        element.title = 'Double click to edit';
    });
}

function startEditing(element) {
    // Check if it's already being edited
    if (element.querySelector('.edit-input')) {
        return;
    }

    // Get the current text
    const currentText = element.textContent;

    // Create the editing input
    const input = document.createElement('input');
    input.type = 'text';
    input.value = currentText;
    input.className = 'edit-input';

    // Styles for the input
    input.style.cssText = `
        width: 100%;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: inherit;
        font-size: inherit;
        background: white;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        outline: none;
    `;

    // Hide the original text temporarily
    const originalDisplay = element.style.display;
    element.style.position = 'relative';
    
    // Save the original content and clean it
    const originalContent = element.innerHTML;
    element.innerHTML = '';
    element.appendChild(input);

    // Focus and select all text
    input.focus();
    input.select();

    // Function to confirm changes
    function confirmEdit() {
        const newText = input.value.trim();
        element.innerHTML = originalContent;
        if (newText && newText !== currentText) {
            element.textContent = newText;
        }
        element.style.display = originalDisplay;
        
        // Save the changues
        pywebview.api.update_html_content();
    }

    // Function to cancel changes
    function cancelEdit() {
        element.innerHTML = originalContent;
        element.style.display = originalDisplay;
    }

    // Event listeners for the input
    input.addEventListener('keydown', function(e) {
        e.stopPropagation();
        
        if (e.key === 'Enter') {
            e.preventDefault();
            confirmEdit();
        } else if (e.key === 'Escape') {
            e.preventDefault();
            cancelEdit();
        }
    });

    // Confirm on blur (optional)
    input.addEventListener('blur', function(e) {
        // Small delay to allow other events to process first
        setTimeout(() => {
            if (element.querySelector('.edit-input')) {
                confirmEdit();
            }
        }, 100);
    });

    // Prevent clicks on the input from triggering other events
    input.addEventListener('click', function(e) {
        e.stopPropagation();
    });
}

// Functions that allow changing the order of the SVG
let draggedElementNavThumb = null;
let originalOrderNavThumb = [];

function initDragRepositionNavThumb() {
    const container = document.getElementById('nav-thumbs');
    if (!container) return;

    // Initialize indices automatically
    initializeOriginalIndices();
    
    // Save initial order
    saveOriginalOrderNavThumb();

    container.addEventListener('mousedown', (e) => {
        // Find the closest nav-thumb element upwards
        const navThumbElement = e.target.closest('.nav-thumb');
        if (navThumbElement) {
            // RESET: Reassign the original indexes so that the new order is [1,2,3...]
            resetOriginalIndices();
            // Update the original order for future comparisons
            originalOrderNavThumb = Array.from(container.children).map((child, index) => index + 1);
            // Activate draggable only when mouse is pressed
            navThumbElement.draggable = true;
        }
    });

    container.addEventListener('dragstart', (e) => {
        // Find the closest nav-thumb element upwards
        const navThumbElement = e.target.closest('.nav-thumb');
        if (navThumbElement) {
            draggedElementNavThumb = navThumbElement;
            navThumbElement.classList.add('dragging');
        }
    });

    container.addEventListener('dragend', (e) => {
        // Find the closest nav-thumb element upwards
        const navThumbElement = e.target.closest('.nav-thumb');
        if (navThumbElement) {
            navThumbElement.classList.remove('dragging');
            // Deactivate draggable when finished
            navThumbElement.removeAttribute("draggable");
            checkPositionChangeNavThumb();
            draggedElementNavThumb = null;
        }
    });

    container.addEventListener('dragover', (e) => {
        e.preventDefault();
        const afterElement = getDragAfterElementNavThumb(container, e.clientY);
        if (!draggedElementNavThumb) { return; }
        if (afterElement == null) {
            container.appendChild(draggedElementNavThumb);
        } else {
            container.insertBefore(draggedElementNavThumb, afterElement);
        }
    });
}

function saveOriginalOrderNavThumb() {
    const container = document.getElementById('nav-thumbs');
    // Create sequential order [1, 2, 3, 4, 5...]
    originalOrderNavThumb = Array.from(container.children).map((child, index) => index + 1);
}

function getDragAfterElementNavThumb(container, y) {
    const draggableElements = [...container.querySelectorAll('.nav-thumb:not(.dragging)')];
    
    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;
        
        if (offset < 0 && offset > closest.offset) {
            return { offset: offset, element: child };
        } else {
            return closest;
        }
    }, { offset: Number.NEGATIVE_INFINITY }).element;
}

function checkPositionChangeNavThumb() {
    const container = document.getElementById('nav-thumbs');

    // Create numeric array based on the data-original-index of the elements in their current order
    const currentOrder = Array.from(container.children).map(child => {
        return parseInt(child.dataset.originalIndex);
    });

    const hasChanged = !arraysEqual(originalOrderNavThumb, currentOrder);
    
    if (hasChanged) {
        console.log('Repositioning completed - Position changed:', {
            PreviousOrder: originalOrderNavThumb,
            CurrentOrder: currentOrder
        });
        
        // RESET: Reassign the original indexes so that the new order is [1,2,3...]
        resetOriginalIndices();
        // Update the original order for future comparisons
        originalOrderNavThumb = Array.from(container.children).map((child, index) => index + 1);

        // Send new order to the API
        let indexNavThumb = Array.from(draggedElementNavThumb.parentNode.children).indexOf(draggedElementNavThumb);
        pywebview.api.reorder_SVGs(currentOrder, indexNavThumb + 1);
    }
}

function arraysEqual(a, b) {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) return false;
    }
    return true;
}

// Function to initialize the original indexes on the elements
function initializeOriginalIndices() {
    const container = document.getElementById('nav-thumbs');
    if (!container) return;
    
    Array.from(container.children).forEach((child, index) => {
        child.dataset.originalIndex = index + 1;
    });
}

// Function to reset the indexes after a change
function resetOriginalIndices() {
    const container = document.getElementById('nav-thumbs');
    if (!container) return;
    
    // Reassign indexes based on the current order
    Array.from(container.children).forEach((child, index) => {
        child.dataset.originalIndex = index + 1;
    });
}

// Function to be executed when right-clicking on any SVG
function handleRightClickPreview(event) {
    event.preventDefault();

    // Remove any previous menu
    document.querySelectorAll(".context-menu-temp").forEach(menu => menu.remove());

    // Create styles from JS
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

    // Create menu container
    const menu = document.createElement("div");
    menu.className = "context-menu-temp";


    const hrline = document.createElement("hr");
    hrline.style.margin = "0px";
    hrline.style.borderColor= "#000";

    // Create options
    const option1 = document.createElement("div");
    option1.textContent = "Edit";
    option1.onclick = () => {
        menu.remove();
        style.remove();
        let svgHtml = limpiarAtributosDuplicados(this.outerHTML);
        pywebview.api.open_svg_editor(svgHtml, this.id);
    };

    const option2 = document.createElement("div");
    option2.textContent = "Add SVG Above";
    option2.onclick = () => {
        menu.remove();
        style.remove();
                            
        pywebview.api.add_new_SVG(this.id, true, undefined);
    };
    
    const option3 = document.createElement("div");
    option3.textContent = "Add SVG Below";
    option3.onclick = () => {
        menu.remove();
        style.remove();
        
        pywebview.api.add_new_SVG(this.id, undefined, true);
    };
    
    const option4 = document.createElement("div");
    option4.textContent = "Delete";
    option4.onclick = () => {
        menu.remove();
        style.remove();

        if (confirm("Are you sure you want to delete this page?")) {
            // Si el usuario hace clic en "Aceptar", llama a la función de Python
            pywebview.api.delete_this_SVG(this.id);
        }
    };
    
    const option5 = document.createElement("div");
    option5.textContent = "Update Icon";
    option5.onclick = () => {
        menu.remove();
        style.remove();
        
        let clone_svg = this.cloneNode(true);
        
        window.cleanElementSVGAdded(clone_svg);
        
        window.final_svg_edit = clone_svg;
        
        pywebview.api.refresh_svg_icon();
    };
    
    const option6 = document.createElement("div");
    option6.textContent = "Add Empty Page Above";
    option6.onclick = () => {
        menu.remove();
        style.remove();
        
        pywebview.api.add_new_SVG(this.id, true, undefined, true);
    };
    
    const option7 = document.createElement("div");
    option7.textContent = "Add Empty Page Below";
    option7.onclick = () => {
        menu.remove();
        style.remove();
        
        pywebview.api.add_new_SVG(this.id, undefined, true, true);
    };

    menu.appendChild(option1);
    menu.appendChild(hrline.cloneNode());
    menu.appendChild(option2);
    menu.appendChild(option3);
    menu.appendChild(hrline.cloneNode());
    menu.appendChild(option4);
    menu.appendChild(hrline.cloneNode());
    menu.appendChild(option5);
    menu.appendChild(hrline.cloneNode());
    menu.appendChild(option6);
    menu.appendChild(option7);

    // Position menu
    menu.style.left = `${event.pageX}px`;
    menu.style.top = `${event.pageY}px`;

    document.body.appendChild(menu);

    // Close if clicked outside or Escape is pressed
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
            // Assign right-click event
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
        
        // Copy the content inline
        if (oldScript.textContent) {
            newScript.textContent = oldScript.textContent;
        }

        // Copy attributes (src, type, etc.)
        for (let attr of oldScript.attributes) {
            newScript.setAttribute(attr.name, attr.value);
        }

        // Replace the old <script> with the new executable one
        oldScript.parentNode.replaceChild(newScript, oldScript);
    });
}

// Initialize when the DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', makeElementsEditable);
    document.addEventListener('DOMContentLoaded', setupPageElementsPreview);
    document.addEventListener('DOMContentLoaded', initDragRepositionNavThumb);
} else {
    makeElementsEditable();
    setupPageElementsPreview();
    initDragRepositionNavThumb();
}
"""

# Note: HTML for the interface
html_interface = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Editor HTML</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .section {
            margin-bottom: 5px;
        }
        .section h2 {
            color: #555;
            margin-top: 0;
        }
        button {
            background-color: #4f4f4f;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin: 5px;
        }
        button:hover {
            background-color: #575656;
        }
        textarea {
            width: 100%;
            height: 380px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: monospace;
            font-size: 12px;
        }
        .status {
            margin: 10px 0;
            padding: 10px;
            border-radius: 4px;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .filename {
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
            
        <div class="section">
            <button onclick="openFile()">Open HTML file</button>
            <span id="currentFile" class="filename">No file</span>
        </div>
        
        <div class="section">
            <button id="openPreviewButton" onclick="open_preview()">Open editable preview 🖋️🏞️</button>
        </div>
        
        <div class="section">
            <button onclick="saveAs()">Save as</button>
        </div>
        
        <div id="status"></div>
        
        <div class="section">
            <span style="font-family: monospace;">Current content:</span>
            <textarea id="contentArea" readonly></textarea>
        </div>
    </div>

    <script>
        function showStatus(message, isError = false) {
            const statusDiv = document.getElementById('status');
            statusDiv.innerHTML = `<div class="${isError ? 'error' : 'success'}">${message}</div>`;
            setTimeout(() => statusDiv.innerHTML = '', 5000);
        }

        function updateContent(content, filename) {
            document.getElementById('contentArea').value = content;
            if (filename) {
                document.getElementById('currentFile').textContent = filename;
            }
        }
        
        window.addEventListener("updateContent", (e) => {
            updateContent(e.content, null);
        });
        
        function openFile() {
            pywebview.api.open_file().then(result => {
                if (result.success) {
                    updateContent(result.content, result.filename);
                    pywebview.api.do_better_html().then(result => {
                        if (result.success) {
                            updateContent(result.content, document.getElementById('currentFile').textContent);
                            showStatus('File loaded successfully');
                        } else {
                            showStatus(result.error, true);
                        }
                    });
                } else {
                    showStatus(result.error, true);
                }
            });
        }
        
        function open_preview(){
            console.log(document.getElementById('contentArea').value);
            let html_preview = document.getElementById('contentArea').value;
            
            pywebview.api.open_preview_window(html_preview).then(result => {
                if (!result.success) {
                    showStatus(result.error, true);
                }
            });
        }

        function saveAs() {
            const defaultFilename = document.getElementById('currentFile').innerHTML || 'modified.html';
            
            pywebview.api.save_as(defaultFilename).then(result => {
                if (result.success) {
                    showStatus(result.message);
                } else {
                    showStatus(result.error, true);
                }
            });
        }

        // Load current content on startup, pywebview ready fires when the DOM and pywebview api are loaded
        window.addEventListener('pywebviewready', function () {
            pywebview.api.get_current_content().then(result => {
                updateContent(result.content, result.filename);
            });
        });
    </script>
</body>
</html>
"""