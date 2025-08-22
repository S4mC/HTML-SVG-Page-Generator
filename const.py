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
(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw((a.code="MODULE_NOT_FOUND"),a)}
var p=(n[i]={exports:{}});e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}
return n[i].exports}
for(var u="function"==typeof require&&require,i=0;i<t.length;i++)
o(t[i]);return o}
return r})()({1:[function(require,module,exports){var SvgUtils=require("./svg-utilities");module.exports={enable:function(instance){var defs=instance.svg.querySelector("defs");if(!defs){defs=document.createElementNS(SvgUtils.svgNS,"defs");instance.svg.appendChild(defs)}
var styleEl=defs.querySelector("style#svg-pan-zoom-controls-styles");if(!styleEl){var style=document.createElementNS(SvgUtils.svgNS,"style");style.setAttribute("id","svg-pan-zoom-controls-styles");style.setAttribute("type","text/css");style.textContent=".svg-pan-zoom-control { cursor: pointer; fill: black; fill-opacity: 0.333; } .svg-pan-zoom-control:hover { fill-opacity: 0.8; } .svg-pan-zoom-control-background { fill: white; fill-opacity: 0.5; } .svg-pan-zoom-control-background { fill-opacity: 0.8; }";defs.appendChild(style)}
var zoomGroup=document.createElementNS(SvgUtils.svgNS,"g");zoomGroup.setAttribute("id","svg-pan-zoom-controls");zoomGroup.setAttribute("transform","translate("+(instance.width-70)+" "+(instance.height-76)+") scale(0.75)");zoomGroup.setAttribute("class","svg-pan-zoom-control");zoomGroup.appendChild(this._createZoomIn(instance));zoomGroup.appendChild(this._createZoomReset(instance));zoomGroup.appendChild(this._createZoomOut(instance));instance.svg.appendChild(zoomGroup);instance.controlIcons=zoomGroup},_createZoomIn:function(instance){var zoomIn=document.createElementNS(SvgUtils.svgNS,"g");zoomIn.setAttribute("id","svg-pan-zoom-zoom-in");zoomIn.setAttribute("transform","translate(30.5 5) scale(0.015)");zoomIn.setAttribute("class","svg-pan-zoom-control");zoomIn.addEventListener("click",function(){instance.getPublicInstance().zoomIn()},!1);zoomIn.addEventListener("touchstart",function(){instance.getPublicInstance().zoomIn()},!1);var zoomInBackground=document.createElementNS(SvgUtils.svgNS,"rect");zoomInBackground.setAttribute("x","0");zoomInBackground.setAttribute("y","0");zoomInBackground.setAttribute("width","1500");zoomInBackground.setAttribute("height","1400");zoomInBackground.setAttribute("class","svg-pan-zoom-control-background");zoomIn.appendChild(zoomInBackground);var zoomInShape=document.createElementNS(SvgUtils.svgNS,"path");zoomInShape.setAttribute("d","M1280 576v128q0 26 -19 45t-45 19h-320v320q0 26 -19 45t-45 19h-128q-26 0 -45 -19t-19 -45v-320h-320q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h320v-320q0 -26 19 -45t45 -19h128q26 0 45 19t19 45v320h320q26 0 45 19t19 45zM1536 1120v-960 q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5t84.5 -203.5z");zoomInShape.setAttribute("class","svg-pan-zoom-control-element");zoomIn.appendChild(zoomInShape);return zoomIn},_createZoomReset:function(instance){var resetPanZoomControl=document.createElementNS(SvgUtils.svgNS,"g");resetPanZoomControl.setAttribute("id","svg-pan-zoom-reset-pan-zoom");resetPanZoomControl.setAttribute("transform","translate(5 35) scale(0.4)");resetPanZoomControl.setAttribute("class","svg-pan-zoom-control");resetPanZoomControl.addEventListener("click",function(){instance.getPublicInstance().reset()},!1);resetPanZoomControl.addEventListener("touchstart",function(){instance.getPublicInstance().reset()},!1);var resetPanZoomControlBackground=document.createElementNS(SvgUtils.svgNS,"rect");resetPanZoomControlBackground.setAttribute("x","2");resetPanZoomControlBackground.setAttribute("y","2");resetPanZoomControlBackground.setAttribute("width","182");resetPanZoomControlBackground.setAttribute("height","58");resetPanZoomControlBackground.setAttribute("class","svg-pan-zoom-control-background");resetPanZoomControl.appendChild(resetPanZoomControlBackground);var resetPanZoomControlShape1=document.createElementNS(SvgUtils.svgNS,"path");resetPanZoomControlShape1.setAttribute("d","M33.051,20.632c-0.742-0.406-1.854-0.609-3.338-0.609h-7.969v9.281h7.769c1.543,0,2.701-0.188,3.473-0.562c1.365-0.656,2.048-1.953,2.048-3.891C35.032,22.757,34.372,21.351,33.051,20.632z");resetPanZoomControlShape1.setAttribute("class","svg-pan-zoom-control-element");resetPanZoomControl.appendChild(resetPanZoomControlShape1);var resetPanZoomControlShape2=document.createElementNS(SvgUtils.svgNS,"path");resetPanZoomControlShape2.setAttribute("d","M170.231,0.5H15.847C7.102,0.5,0.5,5.708,0.5,11.84v38.861C0.5,56.833,7.102,61.5,15.847,61.5h154.384c8.745,0,15.269-4.667,15.269-10.798V11.84C185.5,5.708,178.976,0.5,170.231,0.5z M42.837,48.569h-7.969c-0.219-0.766-0.375-1.383-0.469-1.852c-0.188-0.969-0.289-1.961-0.305-2.977l-0.047-3.211c-0.03-2.203-0.41-3.672-1.142-4.406c-0.732-0.734-2.103-1.102-4.113-1.102h-7.05v13.547h-7.055V14.022h16.524c2.361,0.047,4.178,0.344,5.45,0.891c1.272,0.547,2.351,1.352,3.234,2.414c0.731,0.875,1.31,1.844,1.737,2.906s0.64,2.273,0.64,3.633c0,1.641-0.414,3.254-1.242,4.84s-2.195,2.707-4.102,3.363c1.594,0.641,2.723,1.551,3.387,2.73s0.996,2.98,0.996,5.402v2.32c0,1.578,0.063,2.648,0.19,3.211c0.19,0.891,0.635,1.547,1.333,1.969V48.569z M75.579,48.569h-26.18V14.022h25.336v6.117H56.454v7.336h16.781v6H56.454v8.883h19.125V48.569z M104.497,46.331c-2.44,2.086-5.887,3.129-10.34,3.129c-4.548,0-8.125-1.027-10.731-3.082s-3.909-4.879-3.909-8.473h6.891c0.224,1.578,0.662,2.758,1.316,3.539c1.196,1.422,3.246,2.133,6.15,2.133c1.739,0,3.151-0.188,4.236-0.562c2.058-0.719,3.087-2.055,3.087-4.008c0-1.141-0.504-2.023-1.512-2.648c-1.008-0.609-2.607-1.148-4.796-1.617l-3.74-0.82c-3.676-0.812-6.201-1.695-7.576-2.648c-2.328-1.594-3.492-4.086-3.492-7.477c0-3.094,1.139-5.664,3.417-7.711s5.623-3.07,10.036-3.07c3.685,0,6.829,0.965,9.431,2.895c2.602,1.93,3.966,4.73,4.093,8.402h-6.938c-0.128-2.078-1.057-3.555-2.787-4.43c-1.154-0.578-2.587-0.867-4.301-0.867c-1.907,0-3.428,0.375-4.565,1.125c-1.138,0.75-1.706,1.797-1.706,3.141c0,1.234,0.561,2.156,1.682,2.766c0.721,0.406,2.25,0.883,4.589,1.43l6.063,1.43c2.657,0.625,4.648,1.461,5.975,2.508c2.059,1.625,3.089,3.977,3.089,7.055C108.157,41.624,106.937,44.245,104.497,46.331z M139.61,48.569h-26.18V14.022h25.336v6.117h-18.281v7.336h16.781v6h-16.781v8.883h19.125V48.569z M170.337,20.14h-10.336v28.43h-7.266V20.14h-10.383v-6.117h27.984V20.14z");resetPanZoomControlShape2.setAttribute("class","svg-pan-zoom-control-element");resetPanZoomControl.appendChild(resetPanZoomControlShape2);return resetPanZoomControl},_createZoomOut:function(instance){var zoomOut=document.createElementNS(SvgUtils.svgNS,"g");zoomOut.setAttribute("id","svg-pan-zoom-zoom-out");zoomOut.setAttribute("transform","translate(30.5 70) scale(0.015)");zoomOut.setAttribute("class","svg-pan-zoom-control");zoomOut.addEventListener("click",function(){instance.getPublicInstance().zoomOut()},!1);zoomOut.addEventListener("touchstart",function(){instance.getPublicInstance().zoomOut()},!1);var zoomOutBackground=document.createElementNS(SvgUtils.svgNS,"rect");zoomOutBackground.setAttribute("x","0");zoomOutBackground.setAttribute("y","0");zoomOutBackground.setAttribute("width","1500");zoomOutBackground.setAttribute("height","1400");zoomOutBackground.setAttribute("class","svg-pan-zoom-control-background");zoomOut.appendChild(zoomOutBackground);var zoomOutShape=document.createElementNS(SvgUtils.svgNS,"path");zoomOutShape.setAttribute("d","M1280 576v128q0 26 -19 45t-45 19h-896q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h896q26 0 45 19t19 45zM1536 1120v-960q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5 t84.5 -203.5z");zoomOutShape.setAttribute("class","svg-pan-zoom-control-element");zoomOut.appendChild(zoomOutShape);return zoomOut},disable:function(instance){if(instance.controlIcons){instance.controlIcons.parentNode.removeChild(instance.controlIcons);instance.controlIcons=null}},}},{"./svg-utilities":5},],2:[function(require,module,exports){var SvgUtils=require("./svg-utilities"),Utils=require("./utilities");var ShadowViewport=function(viewport,options){this.init(viewport,options)};ShadowViewport.prototype.init=function(viewport,options){this.viewport=viewport;this.options=options;this.originalState={zoom:1,x:0,y:0};this.activeState={zoom:1,x:0,y:0};this.updateCTMCached=Utils.proxy(this.updateCTM,this);this.requestAnimationFrame=Utils.createRequestAnimationFrame(this.options.refreshRate);this.viewBox={x:0,y:0,width:0,height:0};this.cacheViewBox();var newCTM=this.processCTM();this.setCTM(newCTM);this.updateCTM()};ShadowViewport.prototype.cacheViewBox=function(){var svgViewBox=this.options.svg.getAttribute("viewBox");if(svgViewBox){var viewBoxValues=svgViewBox.split(/[\s\,]/).filter(function(v){return v}).map(parseFloat);this.viewBox.x=viewBoxValues[0];this.viewBox.y=viewBoxValues[1];this.viewBox.width=viewBoxValues[2];this.viewBox.height=viewBoxValues[3];var zoom=Math.min(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height);this.activeState.zoom=zoom;this.activeState.x=(this.options.width-this.viewBox.width*zoom)/2;this.activeState.y=(this.options.height-this.viewBox.height*zoom)/2;this.updateCTMOnNextFrame();this.options.svg.removeAttribute("viewBox")}else{this.simpleViewBoxCache()}};ShadowViewport.prototype.simpleViewBoxCache=function(){var bBox=this.viewport.getBBox();this.viewBox.x=bBox.x;this.viewBox.y=bBox.y;this.viewBox.width=bBox.width;this.viewBox.height=bBox.height};ShadowViewport.prototype.getViewBox=function(){return Utils.extend({},this.viewBox)};ShadowViewport.prototype.processCTM=function(){var newCTM=this.getCTM();if(this.options.fit||this.options.contain){var newScale;if(this.options.fit){newScale=Math.min(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height)}else{newScale=Math.max(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height)}
newCTM.a=newScale;newCTM.d=newScale;newCTM.e=-this.viewBox.x*newScale;newCTM.f=-this.viewBox.y*newScale}
if(this.options.center){var offsetX=(this.options.width-(this.viewBox.width+this.viewBox.x*2)*newCTM.a)*0.5,offsetY=(this.options.height-(this.viewBox.height+this.viewBox.y*2)*newCTM.a)*0.5;newCTM.e=offsetX;newCTM.f=offsetY}
this.originalState.zoom=newCTM.a;this.originalState.x=newCTM.e;this.originalState.y=newCTM.f;return newCTM};ShadowViewport.prototype.getOriginalState=function(){return Utils.extend({},this.originalState)};ShadowViewport.prototype.getState=function(){return Utils.extend({},this.activeState)};ShadowViewport.prototype.getZoom=function(){return this.activeState.zoom};ShadowViewport.prototype.getRelativeZoom=function(){return this.activeState.zoom/this.originalState.zoom};ShadowViewport.prototype.computeRelativeZoom=function(scale){return scale/this.originalState.zoom};ShadowViewport.prototype.getPan=function(){return{x:this.activeState.x,y:this.activeState.y}};ShadowViewport.prototype.getCTM=function(){var safeCTM=this.options.svg.createSVGMatrix();safeCTM.a=this.activeState.zoom;safeCTM.b=0;safeCTM.c=0;safeCTM.d=this.activeState.zoom;safeCTM.e=this.activeState.x;safeCTM.f=this.activeState.y;return safeCTM};ShadowViewport.prototype.setCTM=function(newCTM){var willZoom=this.isZoomDifferent(newCTM),willPan=this.isPanDifferent(newCTM);if(willZoom||willPan){if(willZoom){if(this.options.beforeZoom(this.getRelativeZoom(),this.computeRelativeZoom(newCTM.a))===!1){newCTM.a=newCTM.d=this.activeState.zoom;willZoom=!1}else{this.updateCache(newCTM);this.options.onZoom(this.getRelativeZoom())}}
if(willPan){var preventPan=this.options.beforePan(this.getPan(),{x:newCTM.e,y:newCTM.f,}),preventPanX=!1,preventPanY=!1;if(preventPan===!1){newCTM.e=this.getPan().x;newCTM.f=this.getPan().y;preventPanX=preventPanY=!0}else if(Utils.isObject(preventPan)){if(preventPan.x===!1){newCTM.e=this.getPan().x;preventPanX=!0}else if(Utils.isNumber(preventPan.x)){newCTM.e=preventPan.x}
if(preventPan.y===!1){newCTM.f=this.getPan().y;preventPanY=!0}else if(Utils.isNumber(preventPan.y)){newCTM.f=preventPan.y}}
if((preventPanX&&preventPanY)||!this.isPanDifferent(newCTM)){willPan=!1}else{this.updateCache(newCTM);this.options.onPan(this.getPan())}}
if(willZoom||willPan){this.updateCTMOnNextFrame()}}};ShadowViewport.prototype.isZoomDifferent=function(newCTM){return this.activeState.zoom!==newCTM.a};ShadowViewport.prototype.isPanDifferent=function(newCTM){return(this.activeState.x!==newCTM.e||this.activeState.y!==newCTM.f)};ShadowViewport.prototype.updateCache=function(newCTM){this.activeState.zoom=newCTM.a;this.activeState.x=newCTM.e;this.activeState.y=newCTM.f};ShadowViewport.prototype.pendingUpdate=!1;ShadowViewport.prototype.updateCTMOnNextFrame=function(){if(!this.pendingUpdate){this.pendingUpdate=!0;this.requestAnimationFrame.call(window,this.updateCTMCached)}};ShadowViewport.prototype.updateCTM=function(){var ctm=this.getCTM();SvgUtils.setCTM(this.viewport,ctm,this.defs);this.pendingUpdate=!1;if(this.options.onUpdatedCTM){this.options.onUpdatedCTM(ctm)}};module.exports=function(viewport,options){return new ShadowViewport(viewport,options)}},{"./svg-utilities":5,"./utilities":7},],3:[function(require,module,exports){var svgPanZoom=require("./svg-pan-zoom.js");(function(window,document){if(typeof define==="function"&&define.amd){define("svg-pan-zoom",function(){return svgPanZoom})}else if(typeof module!=="undefined"&&module.exports){module.exports=svgPanZoom;window.svgPanZoom=svgPanZoom}})(window,document)},{"./svg-pan-zoom.js":4},],4:[function(require,module,exports){var Wheel=require("./uniwheel"),ControlIcons=require("./control-icons"),Utils=require("./utilities"),SvgUtils=require("./svg-utilities"),ShadowViewport=require("./shadow-viewport");var SvgPanZoom=function(svg,options){this.init(svg,options)};var optionsDefaults={viewportSelector:".svg-pan-zoom_viewport",panEnabled:!0,controlIconsEnabled:!1,zoomEnabled:!0,dblClickZoomEnabled:!1,mouseWheelZoomEnabled:!0,preventMouseEventsDefault:!0,zoomScaleSensitivity:0.3,minZoom:0.5,maxZoom:10,fit:!0,contain:!1,center:!0,refreshRate:"auto",beforeZoom:null,onZoom:null,beforePan:null,onPan:null,customEventsHandler:null,eventsListenerElement:null,onUpdatedCTM:null,};var passiveListenerOption={passive:!0};SvgPanZoom.prototype.init=function(svg,options){var that=this;this.svg=svg;this.defs=svg.querySelector("defs");SvgUtils.setupSvgAttributes(this.svg);this.options=Utils.extend(Utils.extend({},optionsDefaults),options);this.state="none";var boundingClientRectNormalized=SvgUtils.getBoundingClientRectNormalized(svg);this.width=boundingClientRectNormalized.width;this.height=boundingClientRectNormalized.height;this.viewport=ShadowViewport(SvgUtils.getOrCreateViewport(this.svg,this.options.viewportSelector),{svg:this.svg,width:this.width,height:this.height,fit:this.options.fit,contain:this.options.contain,center:this.options.center,refreshRate:this.options.refreshRate,beforeZoom:function(oldScale,newScale){if(that.viewport&&that.options.beforeZoom){return that.options.beforeZoom(oldScale,newScale)}},onZoom:function(scale){if(that.viewport&&that.options.onZoom){return that.options.onZoom(scale)}},beforePan:function(oldPoint,newPoint){if(that.viewport&&that.options.beforePan){return that.options.beforePan(oldPoint,newPoint)}},onPan:function(point){if(that.viewport&&that.options.onPan){return that.options.onPan(point)}},onUpdatedCTM:function(ctm){if(that.viewport&&that.options.onUpdatedCTM){return that.options.onUpdatedCTM(ctm)}},});var publicInstance=this.getPublicInstance();publicInstance.setBeforeZoom(this.options.beforeZoom);publicInstance.setOnZoom(this.options.onZoom);publicInstance.setBeforePan(this.options.beforePan);publicInstance.setOnPan(this.options.onPan);publicInstance.setOnUpdatedCTM(this.options.onUpdatedCTM);if(this.options.controlIconsEnabled){ControlIcons.enable(this)}
this.lastMouseWheelEventTime=Date.now();this.setupHandlers()};SvgPanZoom.prototype.setupHandlers=function(){var that=this,prevEvt=null;this.eventListeners={mousedown:function(evt){var result=that.handleMouseDown(evt,prevEvt);prevEvt=evt;return result},touchstart:function(evt){var result=that.handleMouseDown(evt,prevEvt);prevEvt=evt;return result},auxclick:function(evt){return that.handleauxclick(evt)},mouseup:function(evt){return that.handleMouseUp(evt)},touchend:function(evt){return that.handleMouseUp(evt)},mousemove:function(evt){return that.handleMouseMove(evt)},touchmove:function(evt){return that.handleMouseMove(evt)},mouseleave:function(evt){return that.handleMouseUp(evt)},touchleave:function(evt){return that.handleMouseUp(evt)},touchcancel:function(evt){return that.handleMouseUp(evt)},};if(this.options.customEventsHandler!=null){this.options.customEventsHandler.init({svgElement:this.svg,eventsListenerElement:this.options.eventsListenerElement,instance:this.getPublicInstance(),});var haltEventListeners=this.options.customEventsHandler.haltEventListeners;if(haltEventListeners&&haltEventListeners.length){for(var i=haltEventListeners.length-1;i>=0;i--){if(this.eventListeners.hasOwnProperty(haltEventListeners[i])){delete this.eventListeners[haltEventListeners[i]]}}}}
for(var event in this.eventListeners){(this.options.eventsListenerElement||this.svg).addEventListener(event,this.eventListeners[event],!this.options.preventMouseEventsDefault?passiveListenerOption:!1)}
if(this.options.mouseWheelZoomEnabled){this.options.mouseWheelZoomEnabled=!1;this.enableMouseWheelZoom()}};SvgPanZoom.prototype.enableMouseWheelZoom=function(){if(!this.options.mouseWheelZoomEnabled){var that=this;this.wheelListener=function(evt){return that.handleMouseWheel(evt)};var isPassiveListener=!this.options.preventMouseEventsDefault;Wheel.on(this.options.eventsListenerElement||this.svg,this.wheelListener,isPassiveListener);this.options.mouseWheelZoomEnabled=!0}};SvgPanZoom.prototype.disableMouseWheelZoom=function(){if(this.options.mouseWheelZoomEnabled){var isPassiveListener=!this.options.preventMouseEventsDefault;Wheel.off(this.options.eventsListenerElement||this.svg,this.wheelListener,isPassiveListener);this.options.mouseWheelZoomEnabled=!1}};SvgPanZoom.prototype.handleMouseWheel=function(evt){if(this.state=="pan"){evt.preventDefault()}
if(!this.options.zoomEnabled){return}
if(this.state!=="pan"){if(!evt.ctrlKey&&!evt.shiftKey){return}
if(this.state!=="none"){return}}
if(this.options.preventMouseEventsDefault){if(evt.preventDefault){evt.preventDefault()}else{evt.returnValue=!1}}
var delta=evt.deltaY||1,timeDelta=Date.now()-this.lastMouseWheelEventTime,divider=3+Math.max(0,30-timeDelta);this.lastMouseWheelEventTime=Date.now();if("deltaMode" in evt&&evt.deltaMode===0&&evt.wheelDelta){delta=evt.deltaY===0?0:Math.abs(evt.wheelDelta)/evt.deltaY}
delta=-0.3<delta&&delta<0.3?delta:((delta>0?1:-1)*Math.log(Math.abs(delta)+10))/divider;var inversedScreenCTM=this.svg.getScreenCTM().inverse(),relativeMousePoint=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(inversedScreenCTM),zoom=Math.pow(1+this.options.zoomScaleSensitivity,-1*delta);this.zoomAtPoint(zoom,relativeMousePoint);if(this.state==="pan"){this.firstEventCTM=this.viewport.getCTM();this.stateOrigin=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.firstEventCTM.inverse())}};SvgPanZoom.prototype.zoomAtPoint=function(zoomScale,point,zoomAbsolute){var originalState=this.viewport.getOriginalState();if(!zoomAbsolute){if(this.getZoom()*zoomScale<this.options.minZoom*originalState.zoom){zoomScale=(this.options.minZoom*originalState.zoom)/this.getZoom()}else if(this.getZoom()*zoomScale>this.options.maxZoom*originalState.zoom){zoomScale=(this.options.maxZoom*originalState.zoom)/this.getZoom()}}else{zoomScale=Math.max(this.options.minZoom*originalState.zoom,Math.min(this.options.maxZoom*originalState.zoom,zoomScale));zoomScale=zoomScale/this.getZoom()}
var oldCTM=this.viewport.getCTM(),relativePoint=point.matrixTransform(oldCTM.inverse()),modifier=this.svg.createSVGMatrix().translate(relativePoint.x,relativePoint.y).scale(zoomScale).translate(-relativePoint.x,-relativePoint.y),newCTM=oldCTM.multiply(modifier);if(newCTM.a!==oldCTM.a){this.viewport.setCTM(newCTM)}};SvgPanZoom.prototype.zoom=function(scale,absolute){this.zoomAtPoint(scale,SvgUtils.getSvgCenterPoint(this.svg,this.width,this.height),absolute)};SvgPanZoom.prototype.publicZoom=function(scale,absolute){if(absolute){scale=this.computeFromRelativeZoom(scale)}
this.zoom(scale,absolute)};SvgPanZoom.prototype.publicZoomAtPoint=function(scale,point,absolute){if(absolute){scale=this.computeFromRelativeZoom(scale)}
if(Utils.getType(point)!=="SVGPoint"){if("x" in point&&"y" in point){point=SvgUtils.createSVGPoint(this.svg,point.x,point.y)}else{throw new Error("Given point is invalid")}}
this.zoomAtPoint(scale,point,absolute)};SvgPanZoom.prototype.getZoom=function(){return this.viewport.getZoom()};SvgPanZoom.prototype.getRelativeZoom=function(){return this.viewport.getRelativeZoom()};SvgPanZoom.prototype.computeFromRelativeZoom=function(zoom){return zoom*this.viewport.getOriginalState().zoom};SvgPanZoom.prototype.resetZoom=function(){var originalState=this.viewport.getOriginalState();this.zoom(originalState.zoom,!0)};SvgPanZoom.prototype.resetPan=function(){this.pan(this.viewport.getOriginalState())};SvgPanZoom.prototype.reset=function(){this.resetZoom();this.resetPan()};SvgPanZoom.prototype.handleDblClick=function(evt){if(this.options.preventMouseEventsDefault){if(evt.preventDefault){evt.preventDefault()}else{evt.returnValue=!1}}
if(this.options.controlIconsEnabled){var targetClass=evt.target.getAttribute("class")||"";if(targetClass.indexOf("svg-pan-zoom-control")>-1){return!1}}
var zoomFactor;if(evt.shiftKey){zoomFactor=1/((1+this.options.zoomScaleSensitivity)*2)}else{zoomFactor=(1+this.options.zoomScaleSensitivity)*2}
var point=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.svg.getScreenCTM().inverse());this.zoomAtPoint(zoomFactor,point)};SvgPanZoom.prototype.handleMouseDown=function(evt,prevEvt){if(evt.button===0){return}
if(this.options.preventMouseEventsDefault){if(evt.preventDefault){if(evt.type!=="touchstart"&&!(evt.touches&&evt.touches.length==1)){evt.preventDefault()}}}
Utils.mouseAndTouchNormalize(evt,this.svg);if(this.options.dblClickZoomEnabled&&Utils.isDblClick(evt,prevEvt)){this.handleDblClick(evt)}else{this.state="pan";this.firstEventCTM=this.viewport.getCTM();this.stateOrigin=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.firstEventCTM.inverse())}};SvgPanZoom.prototype.handleMouseMove=function(evt){if(this.options.preventMouseEventsDefault){if(evt.touches&&evt.touches.length==1){return}
if(evt.preventDefault){evt.preventDefault()}}
if(this.state==="pan"&&this.options.panEnabled){var point=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.firstEventCTM.inverse()),viewportCTM=this.firstEventCTM.translate(point.x-this.stateOrigin.x,point.y-this.stateOrigin.y);this.viewport.setCTM(viewportCTM)}};SvgPanZoom.prototype.handleauxclick=function(evt){evt.preventDefault()};SvgPanZoom.prototype.handleMouseUp=function(evt){if(this.options.preventMouseEventsDefault){if(evt.preventDefault){if(evt.type!="touchend"){evt.preventDefault()}}else{evt.returnValue=!1}}
if(this.state==="pan"){this.state="none"}};SvgPanZoom.prototype.fit=function(){var viewBox=this.viewport.getViewBox(),newScale=Math.min(this.width/viewBox.width,this.height/viewBox.height);this.zoom(newScale,!0)};SvgPanZoom.prototype.contain=function(){var viewBox=this.viewport.getViewBox(),newScale=Math.max(this.width/viewBox.width,this.height/viewBox.height);this.zoom(newScale,!0)};SvgPanZoom.prototype.center=function(){var viewBox=this.viewport.getViewBox(),offsetX=(this.width-(viewBox.width+viewBox.x*2)*this.getZoom())*0.5,offsetY=(this.height-(viewBox.height+viewBox.y*2)*this.getZoom())*0.5;this.getPublicInstance().pan({x:offsetX,y:offsetY})};SvgPanZoom.prototype.updateBBox=function(){this.viewport.simpleViewBoxCache()};SvgPanZoom.prototype.pan=function(point){var viewportCTM=this.viewport.getCTM();viewportCTM.e=point.x;viewportCTM.f=point.y;this.viewport.setCTM(viewportCTM)};SvgPanZoom.prototype.panBy=function(point){var viewportCTM=this.viewport.getCTM();viewportCTM.e+=point.x;viewportCTM.f+=point.y;this.viewport.setCTM(viewportCTM)};SvgPanZoom.prototype.getPan=function(){var state=this.viewport.getState();return{x:state.x,y:state.y}};SvgPanZoom.prototype.resize=function(){var boundingClientRectNormalized=SvgUtils.getBoundingClientRectNormalized(this.svg);this.width=boundingClientRectNormalized.width;this.height=boundingClientRectNormalized.height;var viewport=this.viewport;viewport.options.width=this.width;viewport.options.height=this.height;viewport.processCTM();if(this.options.controlIconsEnabled){this.getPublicInstance().disableControlIcons();this.getPublicInstance().enableControlIcons()}};SvgPanZoom.prototype.destroy=function(){var that=this;this.beforeZoom=null;this.onZoom=null;this.beforePan=null;this.onPan=null;this.onUpdatedCTM=null;if(this.options.customEventsHandler!=null){this.options.customEventsHandler.destroy({svgElement:this.svg,eventsListenerElement:this.options.eventsListenerElement,instance:this.getPublicInstance(),})}
for(var event in this.eventListeners){(this.options.eventsListenerElement||this.svg).removeEventListener(event,this.eventListeners[event],!this.options.preventMouseEventsDefault?passiveListenerOption:!1)}
this.disableMouseWheelZoom();this.getPublicInstance().disableControlIcons();this.reset();instancesStore=instancesStore.filter(function(instance){return instance.svg!==that.svg});delete this.options;delete this.viewport;delete this.publicInstance;delete this.pi;this.getPublicInstance=function(){return null}};SvgPanZoom.prototype.getPublicInstance=function(){var that=this;if(!this.publicInstance){this.publicInstance=this.pi={enablePan:function(){that.options.panEnabled=!0;return that.pi},disablePan:function(){that.options.panEnabled=!1;return that.pi},isPanEnabled:function(){return!!that.options.panEnabled},pan:function(point){that.pan(point);return that.pi},panBy:function(point){that.panBy(point);return that.pi},getPan:function(){return that.getPan()},setBeforePan:function(fn){that.options.beforePan=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},setOnPan:function(fn){that.options.onPan=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},enableZoom:function(){that.options.zoomEnabled=!0;return that.pi},disableZoom:function(){that.options.zoomEnabled=!1;return that.pi},isZoomEnabled:function(){return!!that.options.zoomEnabled},enableControlIcons:function(){if(!that.options.controlIconsEnabled){that.options.controlIconsEnabled=!0;ControlIcons.enable(that)}
return that.pi},disableControlIcons:function(){if(that.options.controlIconsEnabled){that.options.controlIconsEnabled=!1;ControlIcons.disable(that)}
return that.pi},isControlIconsEnabled:function(){return!!that.options.controlIconsEnabled},enableDblClickZoom:function(){that.options.dblClickZoomEnabled=!0;return that.pi},disableDblClickZoom:function(){that.options.dblClickZoomEnabled=!1;return that.pi},isDblClickZoomEnabled:function(){return!!that.options.dblClickZoomEnabled},enableMouseWheelZoom:function(){that.enableMouseWheelZoom();return that.pi},disableMouseWheelZoom:function(){that.disableMouseWheelZoom();return that.pi},isMouseWheelZoomEnabled:function(){return!!that.options.mouseWheelZoomEnabled},setZoomScaleSensitivity:function(scale){that.options.zoomScaleSensitivity=scale;return that.pi},setMinZoom:function(zoom){that.options.minZoom=zoom;return that.pi},setMaxZoom:function(zoom){that.options.maxZoom=zoom;return that.pi},setBeforeZoom:function(fn){that.options.beforeZoom=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},setOnZoom:function(fn){that.options.onZoom=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},zoom:function(scale){that.publicZoom(scale,!0);return that.pi},zoomBy:function(scale){that.publicZoom(scale,!1);return that.pi},zoomAtPoint:function(scale,point){that.publicZoomAtPoint(scale,point,!0);return that.pi},zoomAtPointBy:function(scale,point){that.publicZoomAtPoint(scale,point,!1);return that.pi},zoomIn:function(){this.zoomBy(1+that.options.zoomScaleSensitivity);return that.pi},zoomOut:function(){this.zoomBy(1/(1+that.options.zoomScaleSensitivity));return that.pi},getZoom:function(){return that.getRelativeZoom()},setOnUpdatedCTM:function(fn){that.options.onUpdatedCTM=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},resetZoom:function(){that.resetZoom();return that.pi},resetPan:function(){that.resetPan();return that.pi},reset:function(){that.reset();return that.pi},fit:function(){that.fit();return that.pi},contain:function(){that.contain();return that.pi},center:function(){that.center();return that.pi},updateBBox:function(){that.updateBBox();return that.pi},resize:function(){that.resize();return that.pi},getSizes:function(){return{width:that.width,height:that.height,realZoom:that.getZoom(),viewBox:that.viewport.getViewBox(),}},destroy:function(){that.destroy();return that.pi},}}
return this.publicInstance};var instancesStore=[];var svgPanZoom=function(elementOrSelector,options){var svg=Utils.getSvg(elementOrSelector);if(svg===null){return null}else{for(var i=instancesStore.length-1;i>=0;i--){if(instancesStore[i].svg===svg){return instancesStore[i].instance.getPublicInstance()}}
instancesStore.push({svg:svg,instance:new SvgPanZoom(svg,options),});return instancesStore[instancesStore.length-1].instance.getPublicInstance()}};module.exports=svgPanZoom},{"./control-icons":1,"./shadow-viewport":2,"./svg-utilities":5,"./uniwheel":6,"./utilities":7,},],5:[function(require,module,exports){var Utils=require("./utilities"),_browser="unknown";if(!1||!!document.documentMode){_browser="ie"}
module.exports={svgNS:"http://www.w3.org/2000/svg",xmlNS:"http://www.w3.org/XML/1998/namespace",xmlnsNS:"http://www.w3.org/2000/xmlns/",xlinkNS:"http://www.w3.org/1999/xlink",evNS:"http://www.w3.org/2001/xml-events",getBoundingClientRectNormalized:function(svg){if(svg.clientWidth&&svg.clientHeight){return{width:svg.clientWidth,height:svg.clientHeight,}}else if(!!svg.getBoundingClientRect()){return svg.getBoundingClientRect()}else{throw new Error("Cannot get BoundingClientRect for SVG.")}},getOrCreateViewport:function(svg,selector){var viewport=null;if(Utils.isElement(selector)){viewport=selector}else{viewport=svg.querySelector(selector)}
if(!viewport){var childNodes=Array.prototype.slice.call(svg.childNodes||svg.children).filter(function(el){return(el.nodeName!=="defs"&&el.nodeName!=="#text")});if(childNodes.length===1&&childNodes[0].nodeName==="g"&&childNodes[0].getAttribute("transform")===null){viewport=childNodes[0]}}
if(!viewport){var viewportId="viewport-"+new Date().toISOString().replace(/\D/g,"");viewport=document.createElementNS(this.svgNS,"g");viewport.setAttribute("id",viewportId);var svgChildren=svg.childNodes||svg.children;if(!!svgChildren&&svgChildren.length>0){for(var i=svgChildren.length;i>0;i--){if(svgChildren[svgChildren.length-i].nodeName!=="defs"){viewport.appendChild(svgChildren[svgChildren.length-i])}}}
svg.appendChild(viewport)}
var classNames=[];if(viewport.getAttribute("class")){classNames=viewport.getAttribute("class").split(" ")}
if(!~classNames.indexOf("svg-pan-zoom_viewport")){classNames.push("svg-pan-zoom_viewport");viewport.setAttribute("class",classNames.join(" "))}
return viewport},setupSvgAttributes:function(svg){svg.setAttribute("xmlns",this.svgNS);svg.setAttributeNS(this.xmlnsNS,"xmlns:xlink",this.xlinkNS);svg.setAttributeNS(this.xmlnsNS,"xmlns:ev",this.evNS);if(svg.parentNode!==null){var style=svg.getAttribute("style")||"";if(style.toLowerCase().indexOf("overflow")===-1){svg.setAttribute("style","overflow: hidden; "+style)}}},internetExplorerRedisplayInterval:300,refreshDefsGlobal:Utils.throttle(function(){var allDefs=document.querySelectorAll("defs");var allDefsCount=allDefs.length;for(var i=0;i<allDefsCount;i++){var thisDefs=allDefs[i];thisDefs.parentNode.insertBefore(thisDefs,thisDefs)}},this?this.internetExplorerRedisplayInterval:null),setCTM:function(element,matrix,defs){var that=this,s="matrix("+matrix.a+","+matrix.b+","+matrix.c+","+matrix.d+","+matrix.e+","+matrix.f+")";element.setAttributeNS(null,"transform",s);if("transform" in element.style){element.style.transform=s}else if("-ms-transform" in element.style){element.style["-ms-transform"]=s}else if("-webkit-transform" in element.style){element.style["-webkit-transform"]=s}
if(_browser==="ie"&&!!defs){defs.parentNode.insertBefore(defs,defs);window.setTimeout(function(){that.refreshDefsGlobal()},that.internetExplorerRedisplayInterval)}},getEventPoint:function(evt,svg){var point=svg.createSVGPoint();Utils.mouseAndTouchNormalize(evt,svg);point.x=evt.clientX;point.y=evt.clientY;return point},getSvgCenterPoint:function(svg,width,height){return this.createSVGPoint(svg,width/2,height/2)},createSVGPoint:function(svg,x,y){var point=svg.createSVGPoint();point.x=x;point.y=y;return point},}},{"./utilities":7},],6:[function(require,module,exports){module.exports=(function(){var prefix="",_addEventListener,_removeEventListener,support,fns=[];var passiveListenerOption={passive:!0};var activeListenerOption={passive:!1};if(window.addEventListener){_addEventListener="addEventListener";_removeEventListener="removeEventListener"}else{_addEventListener="attachEvent";_removeEventListener="detachEvent";prefix="on"}
support="onwheel" in document.createElement("div")?"wheel":document.onmousewheel!==undefined?"mousewheel":"DOMMouseScroll";function createCallback(element,callback){var fn=function(originalEvent){!originalEvent&&(originalEvent=window.event);var event={originalEvent:originalEvent,target:originalEvent.target||originalEvent.srcElement,type:"wheel",deltaMode:originalEvent.type=="MozMousePixelScroll"?0:1,deltaX:0,delatZ:0,preventDefault:function(){originalEvent.preventDefault?originalEvent.preventDefault():(originalEvent.returnValue=!1)},};if(support=="mousewheel"){event.deltaY=(-1/40)*originalEvent.wheelDelta;originalEvent.wheelDeltaX&&(event.deltaX=(-1/40)*originalEvent.wheelDeltaX)}else{event.deltaY=originalEvent.detail}
return callback(event)};fns.push({element:element,fn:fn,});return fn}
function getCallback(element){for(var i=0;i<fns.length;i++){if(fns[i].element===element){return fns[i].fn}}
return function(){}}
function removeCallback(element){for(var i=0;i<fns.length;i++){if(fns[i].element===element){return fns.splice(i,1)}}}
function _addWheelListener(elem,eventName,callback,isPassiveListener){var cb;if(support==="wheel"){cb=callback}else{cb=createCallback(elem,callback)}
elem[_addEventListener](prefix+eventName,cb,isPassiveListener?passiveListenerOption:activeListenerOption)}
function _removeWheelListener(elem,eventName,callback,isPassiveListener){var cb;if(support==="wheel"){cb=callback}else{cb=getCallback(elem)}
elem[_removeEventListener](prefix+eventName,cb,isPassiveListener?passiveListenerOption:activeListenerOption);removeCallback(elem)}
function addWheelListener(elem,callback,isPassiveListener){_addWheelListener(elem,support,callback,isPassiveListener);if(support=="DOMMouseScroll"){_addWheelListener(elem,"MozMousePixelScroll",callback,isPassiveListener)}}
function removeWheelListener(elem,callback,isPassiveListener){_removeWheelListener(elem,support,callback,isPassiveListener);if(support=="DOMMouseScroll"){_removeWheelListener(elem,"MozMousePixelScroll",callback,isPassiveListener)}}
return{on:addWheelListener,off:removeWheelListener,}})()},{},],7:[function(require,module,exports){module.exports={extend:function(target,source){target=target||{};for(var prop in source){if(this.isObject(source[prop])){target[prop]=this.extend(target[prop],source[prop])}else{target[prop]=source[prop]}}
return target},isElement:function(o){return(o instanceof HTMLElement||o instanceof SVGElement||o instanceof SVGSVGElement||(o&&typeof o==="object"&&o!==null&&o.nodeType===1&&typeof o.nodeName==="string"))},isObject:function(o){return(Object.prototype.toString.call(o)==="[object Object]")},isNumber:function(n){return!isNaN(parseFloat(n))&&isFinite(n)},getSvg:function(elementOrSelector){var element,svg;if(!this.isElement(elementOrSelector)){if(typeof elementOrSelector==="string"||elementOrSelector instanceof String){element=document.querySelector(elementOrSelector);if(!element){throw new Error("Provided selector did not find any elements. Selector: "+elementOrSelector);return null}}else{throw new Error("Provided selector is not an HTML object nor String");return null}}else{element=elementOrSelector}
if(element.tagName.toLowerCase()==="svg"){svg=element}else{if(element.tagName.toLowerCase()==="object"){svg=element.contentDocument.documentElement}else{if(element.tagName.toLowerCase()==="embed"){svg=element.getSVGDocument().documentElement}else{if(element.tagName.toLowerCase()==="img"){throw new Error('Cannot script an SVG in an "img" element. Please use an "object" element or an in-line SVG.')}else{throw new Error("Cannot get SVG.")}
return null}}}
return svg},proxy:function(fn,context){return function(){return fn.apply(context,arguments)}},getType:function(o){return Object.prototype.toString.apply(o).replace(/^\[object\s/,"").replace(/\]$/,"")},mouseAndTouchNormalize:function(evt,svg){if(evt.clientX===void 0||evt.clientX===null){evt.clientX=0;evt.clientY=0;if(evt.touches!==void 0&&evt.touches.length){if(evt.touches[0].clientX!==void 0){evt.clientX=evt.touches[0].clientX;evt.clientY=evt.touches[0].clientY}else if(evt.touches[0].pageX!==void 0){var rect=svg.getBoundingClientRect();evt.clientX=evt.touches[0].pageX-rect.left;evt.clientY=evt.touches[0].pageY-rect.top}}else if(evt.originalEvent!==void 0){if(evt.originalEvent.clientX!==void 0){evt.clientX=evt.originalEvent.clientX;evt.clientY=evt.originalEvent.clientY}}}},isDblClick:function(evt,prevEvt){if(evt.detail===2){return!0}else if(prevEvt!==void 0&&prevEvt!==null){var timeStampDiff=evt.timeStamp-prevEvt.timeStamp,touchesDistance=Math.sqrt(Math.pow(evt.clientX-prevEvt.clientX,2)+Math.pow(evt.clientY-prevEvt.clientY,2));return timeStampDiff<250&&touchesDistance<10}
return!1},now:Date.now||function(){return new Date().getTime()},throttle:function(func,wait,options){var that=this;var context,args,result;var timeout=null;var previous=0;if(!options){options={}}
var later=function(){previous=options.leading===!1?0:that.now();timeout=null;result=func.apply(context,args);if(!timeout){context=args=null}};return function(){var now=that.now();if(!previous&&options.leading===!1){previous=now}
var remaining=wait-(now-previous);context=this;args=arguments;if(remaining<=0||remaining>wait){clearTimeout(timeout);timeout=null;previous=now;result=func.apply(context,args);if(!timeout){context=args=null}}else if(!timeout&&options.trailing!==!1){timeout=setTimeout(later,remaining)}
return result}},createRequestAnimationFrame:function(refreshRate){var timeout=null;if(refreshRate!=="auto"&&refreshRate<60&&refreshRate>1){timeout=Math.floor(1000/refreshRate)}
if(timeout===null){return(window.requestAnimationFrame||requestTimeout(33))}else{return requestTimeout(timeout)}},};function requestTimeout(timeout){return function(callback){window.setTimeout(callback,timeout)}}},{},],},{},[3])
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
                
                // Solo procesar si es un enlace interno (empieza con #)
                if (href && href.startsWith("#")) {
                    e.preventDefault(); // evita el salto instantáneo

                    const targetId = href.substring(1); // substring quita el "#"
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
                    clearTimeout(resizeTimeout); // Cancela cualquier timeout anterior
                    resizeTimeout = setTimeout(function () {
                        viewer1 = document.getElementById('SVGiewer1');
                        if (window.zoomContainer1) {
                            window.zoomContainer1.destroy();
                        }
                        proper_height();
                        viewer1.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {
                            viewport.replaceWith(...viewport.childNodes);
                        });
                        window.zoomContainer1 = svgPanZoom("#page1");
                        center_svg();
                    }, 280); // 280ms después de que termine
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
                    clearTimeout(resizeTimeout); // Cancela cualquier timeout anterior
                    resizeTimeout = setTimeout(function () {
                        viewer2 = document.getElementById('SVGiewer2');
                        if (window.zoomContainer2) {
                            window.zoomContainer2.destroy();
                        }
                        proper_height();
                        viewer2.querySelectorAll('.svg-pan-zoom_viewport').forEach(viewport => {
                            viewport.replaceWith(...viewport.childNodes);
                        });
                        window.zoomContainer2 = svgPanZoom("#page2");
                        center_svg();
                    }, 280); // 280ms después de que termine
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
            </div></div></div><div id="navBar" style="top: 0px;"><div id="nav-thumbs"><div class="nav-thumb" data-original-index="1" draggable="true"><div><span class="number"><span class="pagenum">1</span></span><a href="#page1" draggable="false"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAABqCAYAAABeUaiAAAAC80lEQVR4AeySQWrEMBAETb6y5As57P/vYf+y92SzYHQRgkhySzNdIWaNjTXT1fVx/7r/cMFgtgMfx+vv8f04uGAwy4Hn83m8xXq5xT8EphJArKk4OewkgFgnCX6nEkCsqTg57CSAWCeJ7L/ifIglBu4yDrFcmhbnRCwxcJdxiOXStDgnYomBu4xDLJemxTkRSwy8jMt9h1i5+12WDrGWoc89GLFy97ssHWItQ597MGLl7ndZOsRahj73YMQq/XI3kQBiTYTJUYUAYhUW3E0kgFgTYXJUIYBYhQV3Ewkg1kSYHFUIIFZhwd1EAluLNTEnR4kJIJYYuMs4xHJpWpwTscTAXcYhlkvT4pyIJQbuMg6xXJoW5/yfWOLlGBeXAGLF7W7rzRFr63riLodYcbvbenPE2rqeuMshVtzutt4csbauZ9lyw4MRaxghB9QIIFaNCs+GCSDWMEIOqBFArBoVng0TQKxhhBxQI4BYNSo8GyaAWMMINQdEm4JY0RoLsi9iBSkq2pqIFa2xIPsiVpCioq2JWNEaC7IvYgUpKtqaiNXbGN81CSBWEw8vewkgVi85vmsSQKwmHl72EkCsXnJ81ySAWE08vOwlgFi95PiuSSCRWM2cvBQTQCwxcJdxiOXStDgnYomBu4xDLJemxTkRSwzcZRxiuTQtznmlWOIojNuJAGLt1EaiXRArUZk7RUGsndpItAtiJSpzpyiItVMbiXZBrERlLotSGYxYFSg8GieAWOMMOaFCALEqUHg0TgCxxhlyQoUAYlWg8GicAGKNM+SECgHEqkCJ/2h9AsRa30HKDRArZa3rQyHW+g5SboBYKWtdHwqx1neQcgPESlnr+lCIpenAbgpi2VWuCYxYGs52UxDLrnJNYMTScLabglh2lWsCI5aGs90UW7HsmhYHRiwxcJdxiOXStDgnYomBu4xDLJemxTkRSwzcZRxiuTQtzrmPWOLgjLuWAGJdy9f2dMSyrf7a4G+xbp+3gwsGsxz4U/YXAAD//wSH6KcAAAAGSURBVAMAvfykBV+l+v8AAAAASUVORK5CYII=" draggable="false"></a></div><p title="Doble clic para editar" style="cursor: pointer; position: relative;">page1</p></div><div class="nav-thumb selected" data-original-index="2"><div><span class="number"><span class="pagenum">2</span></span><a href="#page2" draggable="false"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAABqCAYAAABeUaiAAAAC+ElEQVR4AeySQYrDMBAETT4U9rKHQP5/XPKePewmOVgXIYgltzTTFQgIG2umq+tyv91/b9+3P/4wGOXAy6nL9vw9fh4bfxiMcuCp1PYW63XgD4GRBBBrJE3u2gkg1o6Cw0gCiDWSJnftBBBrR5H8II6HWGLgLuMQy6VpcU7EEgN3GYdYLk2LcyKWGLjLOMRyaVqcE7HEwMu43CfEyt3vtHSINQ197sGIlbvfaekQaxr63IMRK3e/09Ih1jT0uQcjVumX00ACiDUQJlcVAohVWHAaSACxBsLkqkIAsQoLTgMJINZAmFxVCCBWYcFpIIGlxRqYk6vEBBBLDNxlHGK5NC3OiVhi4C7jEMulaXFOxBIDdxmHWC5Ni3N+JpZ4OcbFJYBYcbtbenPEWrqeuMshVtzult4csZauJ+5yiBW3u6U3R6yl65m2XPdgxOpGyAU1AohVo8KzbgKI1Y2QC2oEEKtGhWfdBBCrGyEX1AggVo0Kz7oJIFY3Qs0F0aYgVrTGguyLWEGKirYmYkVrLMi+iBWkqGhrIla0xoLsi1hBioq2JmIdbYzvmgQQq4mHl0cJINZRcnzXJIBYTTy8PEoAsY6S47smAcRq4uHlUQKIdZQc3zUJJBKrmZOXYgKIJQbuMg6xXJoW50QsMXCXcYjl0rQ4J2KJgbuMQyyXpsU5zxRLHIVxKxFArJXaSLQLYiUqc6UoiLVSG4l2QaxEZa4UBbFWaiPRLoiVqMxpUSqDEasChUf9BBCrnyE3VAggVgUKj/oJIFY/Q26oEECsChQe9RNArH6G3FAhgFgVKPEfzU+AWPM7SLkBYqWsdX4oxJrfQcoNECtlrfNDIdb8DlJugFgpa50fCrE0HdhNQSy7yjWBEUvD2W4KYtlVrgmMWBrOdlMQy65yTWDE0nC2m2Irll3T4sCIJQbuMg6xXJoW50QsMXCXcYjl0rQ4J2KJgbuMQyyXpsU51xFLHJxx5xJArHP52t6OWLbVnxv8Ldb167rxh8EoB17K/gMAAP//Lom99gAAAAZJREFUAwCBBrYFJf87MwAAAABJRU5ErkJggg==" draggable="false"></a></div><p title="Doble clic para editar" style="cursor: pointer;">page2</p></div></div></div></div><script>
(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw((a.code="MODULE_NOT_FOUND"),a)}
var p=(n[i]={exports:{}});e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}
return n[i].exports}
for(var u="function"==typeof require&&require,i=0;i<t.length;i++)
o(t[i]);return o}
return r})()({1:[function(require,module,exports){var SvgUtils=require("./svg-utilities");module.exports={enable:function(instance){var defs=instance.svg.querySelector("defs");if(!defs){defs=document.createElementNS(SvgUtils.svgNS,"defs");instance.svg.appendChild(defs)}
var styleEl=defs.querySelector("style#svg-pan-zoom-controls-styles");if(!styleEl){var style=document.createElementNS(SvgUtils.svgNS,"style");style.setAttribute("id","svg-pan-zoom-controls-styles");style.setAttribute("type","text/css");style.textContent=".svg-pan-zoom-control { cursor: pointer; fill: black; fill-opacity: 0.333; } .svg-pan-zoom-control:hover { fill-opacity: 0.8; } .svg-pan-zoom-control-background { fill: white; fill-opacity: 0.5; } .svg-pan-zoom-control-background { fill-opacity: 0.8; }";defs.appendChild(style)}
var zoomGroup=document.createElementNS(SvgUtils.svgNS,"g");zoomGroup.setAttribute("id","svg-pan-zoom-controls");zoomGroup.setAttribute("transform","translate("+(instance.width-70)+" "+(instance.height-76)+") scale(0.75)");zoomGroup.setAttribute("class","svg-pan-zoom-control");zoomGroup.appendChild(this._createZoomIn(instance));zoomGroup.appendChild(this._createZoomReset(instance));zoomGroup.appendChild(this._createZoomOut(instance));instance.svg.appendChild(zoomGroup);instance.controlIcons=zoomGroup},_createZoomIn:function(instance){var zoomIn=document.createElementNS(SvgUtils.svgNS,"g");zoomIn.setAttribute("id","svg-pan-zoom-zoom-in");zoomIn.setAttribute("transform","translate(30.5 5) scale(0.015)");zoomIn.setAttribute("class","svg-pan-zoom-control");zoomIn.addEventListener("click",function(){instance.getPublicInstance().zoomIn()},!1);zoomIn.addEventListener("touchstart",function(){instance.getPublicInstance().zoomIn()},!1);var zoomInBackground=document.createElementNS(SvgUtils.svgNS,"rect");zoomInBackground.setAttribute("x","0");zoomInBackground.setAttribute("y","0");zoomInBackground.setAttribute("width","1500");zoomInBackground.setAttribute("height","1400");zoomInBackground.setAttribute("class","svg-pan-zoom-control-background");zoomIn.appendChild(zoomInBackground);var zoomInShape=document.createElementNS(SvgUtils.svgNS,"path");zoomInShape.setAttribute("d","M1280 576v128q0 26 -19 45t-45 19h-320v320q0 26 -19 45t-45 19h-128q-26 0 -45 -19t-19 -45v-320h-320q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h320v-320q0 -26 19 -45t45 -19h128q26 0 45 19t19 45v320h320q26 0 45 19t19 45zM1536 1120v-960 q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5t84.5 -203.5z");zoomInShape.setAttribute("class","svg-pan-zoom-control-element");zoomIn.appendChild(zoomInShape);return zoomIn},_createZoomReset:function(instance){var resetPanZoomControl=document.createElementNS(SvgUtils.svgNS,"g");resetPanZoomControl.setAttribute("id","svg-pan-zoom-reset-pan-zoom");resetPanZoomControl.setAttribute("transform","translate(5 35) scale(0.4)");resetPanZoomControl.setAttribute("class","svg-pan-zoom-control");resetPanZoomControl.addEventListener("click",function(){instance.getPublicInstance().reset()},!1);resetPanZoomControl.addEventListener("touchstart",function(){instance.getPublicInstance().reset()},!1);var resetPanZoomControlBackground=document.createElementNS(SvgUtils.svgNS,"rect");resetPanZoomControlBackground.setAttribute("x","2");resetPanZoomControlBackground.setAttribute("y","2");resetPanZoomControlBackground.setAttribute("width","182");resetPanZoomControlBackground.setAttribute("height","58");resetPanZoomControlBackground.setAttribute("class","svg-pan-zoom-control-background");resetPanZoomControl.appendChild(resetPanZoomControlBackground);var resetPanZoomControlShape1=document.createElementNS(SvgUtils.svgNS,"path");resetPanZoomControlShape1.setAttribute("d","M33.051,20.632c-0.742-0.406-1.854-0.609-3.338-0.609h-7.969v9.281h7.769c1.543,0,2.701-0.188,3.473-0.562c1.365-0.656,2.048-1.953,2.048-3.891C35.032,22.757,34.372,21.351,33.051,20.632z");resetPanZoomControlShape1.setAttribute("class","svg-pan-zoom-control-element");resetPanZoomControl.appendChild(resetPanZoomControlShape1);var resetPanZoomControlShape2=document.createElementNS(SvgUtils.svgNS,"path");resetPanZoomControlShape2.setAttribute("d","M170.231,0.5H15.847C7.102,0.5,0.5,5.708,0.5,11.84v38.861C0.5,56.833,7.102,61.5,15.847,61.5h154.384c8.745,0,15.269-4.667,15.269-10.798V11.84C185.5,5.708,178.976,0.5,170.231,0.5z M42.837,48.569h-7.969c-0.219-0.766-0.375-1.383-0.469-1.852c-0.188-0.969-0.289-1.961-0.305-2.977l-0.047-3.211c-0.03-2.203-0.41-3.672-1.142-4.406c-0.732-0.734-2.103-1.102-4.113-1.102h-7.05v13.547h-7.055V14.022h16.524c2.361,0.047,4.178,0.344,5.45,0.891c1.272,0.547,2.351,1.352,3.234,2.414c0.731,0.875,1.31,1.844,1.737,2.906s0.64,2.273,0.64,3.633c0,1.641-0.414,3.254-1.242,4.84s-2.195,2.707-4.102,3.363c1.594,0.641,2.723,1.551,3.387,2.73s0.996,2.98,0.996,5.402v2.32c0,1.578,0.063,2.648,0.19,3.211c0.19,0.891,0.635,1.547,1.333,1.969V48.569z M75.579,48.569h-26.18V14.022h25.336v6.117H56.454v7.336h16.781v6H56.454v8.883h19.125V48.569z M104.497,46.331c-2.44,2.086-5.887,3.129-10.34,3.129c-4.548,0-8.125-1.027-10.731-3.082s-3.909-4.879-3.909-8.473h6.891c0.224,1.578,0.662,2.758,1.316,3.539c1.196,1.422,3.246,2.133,6.15,2.133c1.739,0,3.151-0.188,4.236-0.562c2.058-0.719,3.087-2.055,3.087-4.008c0-1.141-0.504-2.023-1.512-2.648c-1.008-0.609-2.607-1.148-4.796-1.617l-3.74-0.82c-3.676-0.812-6.201-1.695-7.576-2.648c-2.328-1.594-3.492-4.086-3.492-7.477c0-3.094,1.139-5.664,3.417-7.711s5.623-3.07,10.036-3.07c3.685,0,6.829,0.965,9.431,2.895c2.602,1.93,3.966,4.73,4.093,8.402h-6.938c-0.128-2.078-1.057-3.555-2.787-4.43c-1.154-0.578-2.587-0.867-4.301-0.867c-1.907,0-3.428,0.375-4.565,1.125c-1.138,0.75-1.706,1.797-1.706,3.141c0,1.234,0.561,2.156,1.682,2.766c0.721,0.406,2.25,0.883,4.589,1.43l6.063,1.43c2.657,0.625,4.648,1.461,5.975,2.508c2.059,1.625,3.089,3.977,3.089,7.055C108.157,41.624,106.937,44.245,104.497,46.331z M139.61,48.569h-26.18V14.022h25.336v6.117h-18.281v7.336h16.781v6h-16.781v8.883h19.125V48.569z M170.337,20.14h-10.336v28.43h-7.266V20.14h-10.383v-6.117h27.984V20.14z");resetPanZoomControlShape2.setAttribute("class","svg-pan-zoom-control-element");resetPanZoomControl.appendChild(resetPanZoomControlShape2);return resetPanZoomControl},_createZoomOut:function(instance){var zoomOut=document.createElementNS(SvgUtils.svgNS,"g");zoomOut.setAttribute("id","svg-pan-zoom-zoom-out");zoomOut.setAttribute("transform","translate(30.5 70) scale(0.015)");zoomOut.setAttribute("class","svg-pan-zoom-control");zoomOut.addEventListener("click",function(){instance.getPublicInstance().zoomOut()},!1);zoomOut.addEventListener("touchstart",function(){instance.getPublicInstance().zoomOut()},!1);var zoomOutBackground=document.createElementNS(SvgUtils.svgNS,"rect");zoomOutBackground.setAttribute("x","0");zoomOutBackground.setAttribute("y","0");zoomOutBackground.setAttribute("width","1500");zoomOutBackground.setAttribute("height","1400");zoomOutBackground.setAttribute("class","svg-pan-zoom-control-background");zoomOut.appendChild(zoomOutBackground);var zoomOutShape=document.createElementNS(SvgUtils.svgNS,"path");zoomOutShape.setAttribute("d","M1280 576v128q0 26 -19 45t-45 19h-896q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h896q26 0 45 19t19 45zM1536 1120v-960q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5 t84.5 -203.5z");zoomOutShape.setAttribute("class","svg-pan-zoom-control-element");zoomOut.appendChild(zoomOutShape);return zoomOut},disable:function(instance){if(instance.controlIcons){instance.controlIcons.parentNode.removeChild(instance.controlIcons);instance.controlIcons=null}},}},{"./svg-utilities":5},],2:[function(require,module,exports){var SvgUtils=require("./svg-utilities"),Utils=require("./utilities");var ShadowViewport=function(viewport,options){this.init(viewport,options)};ShadowViewport.prototype.init=function(viewport,options){this.viewport=viewport;this.options=options;this.originalState={zoom:1,x:0,y:0};this.activeState={zoom:1,x:0,y:0};this.updateCTMCached=Utils.proxy(this.updateCTM,this);this.requestAnimationFrame=Utils.createRequestAnimationFrame(this.options.refreshRate);this.viewBox={x:0,y:0,width:0,height:0};this.cacheViewBox();var newCTM=this.processCTM();this.setCTM(newCTM);this.updateCTM()};ShadowViewport.prototype.cacheViewBox=function(){var svgViewBox=this.options.svg.getAttribute("viewBox");if(svgViewBox){var viewBoxValues=svgViewBox.split(/[\s\,]/).filter(function(v){return v}).map(parseFloat);this.viewBox.x=viewBoxValues[0];this.viewBox.y=viewBoxValues[1];this.viewBox.width=viewBoxValues[2];this.viewBox.height=viewBoxValues[3];var zoom=Math.min(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height);this.activeState.zoom=zoom;this.activeState.x=(this.options.width-this.viewBox.width*zoom)/2;this.activeState.y=(this.options.height-this.viewBox.height*zoom)/2;this.updateCTMOnNextFrame();this.options.svg.removeAttribute("viewBox")}else{this.simpleViewBoxCache()}};ShadowViewport.prototype.simpleViewBoxCache=function(){var bBox=this.viewport.getBBox();this.viewBox.x=bBox.x;this.viewBox.y=bBox.y;this.viewBox.width=bBox.width;this.viewBox.height=bBox.height};ShadowViewport.prototype.getViewBox=function(){return Utils.extend({},this.viewBox)};ShadowViewport.prototype.processCTM=function(){var newCTM=this.getCTM();if(this.options.fit||this.options.contain){var newScale;if(this.options.fit){newScale=Math.min(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height)}else{newScale=Math.max(this.options.width/this.viewBox.width,this.options.height/this.viewBox.height)}
newCTM.a=newScale;newCTM.d=newScale;newCTM.e=-this.viewBox.x*newScale;newCTM.f=-this.viewBox.y*newScale}
if(this.options.center){var offsetX=(this.options.width-(this.viewBox.width+this.viewBox.x*2)*newCTM.a)*0.5,offsetY=(this.options.height-(this.viewBox.height+this.viewBox.y*2)*newCTM.a)*0.5;newCTM.e=offsetX;newCTM.f=offsetY}
this.originalState.zoom=newCTM.a;this.originalState.x=newCTM.e;this.originalState.y=newCTM.f;return newCTM};ShadowViewport.prototype.getOriginalState=function(){return Utils.extend({},this.originalState)};ShadowViewport.prototype.getState=function(){return Utils.extend({},this.activeState)};ShadowViewport.prototype.getZoom=function(){return this.activeState.zoom};ShadowViewport.prototype.getRelativeZoom=function(){return this.activeState.zoom/this.originalState.zoom};ShadowViewport.prototype.computeRelativeZoom=function(scale){return scale/this.originalState.zoom};ShadowViewport.prototype.getPan=function(){return{x:this.activeState.x,y:this.activeState.y}};ShadowViewport.prototype.getCTM=function(){var safeCTM=this.options.svg.createSVGMatrix();safeCTM.a=this.activeState.zoom;safeCTM.b=0;safeCTM.c=0;safeCTM.d=this.activeState.zoom;safeCTM.e=this.activeState.x;safeCTM.f=this.activeState.y;return safeCTM};ShadowViewport.prototype.setCTM=function(newCTM){var willZoom=this.isZoomDifferent(newCTM),willPan=this.isPanDifferent(newCTM);if(willZoom||willPan){if(willZoom){if(this.options.beforeZoom(this.getRelativeZoom(),this.computeRelativeZoom(newCTM.a))===!1){newCTM.a=newCTM.d=this.activeState.zoom;willZoom=!1}else{this.updateCache(newCTM);this.options.onZoom(this.getRelativeZoom())}}
if(willPan){var preventPan=this.options.beforePan(this.getPan(),{x:newCTM.e,y:newCTM.f,}),preventPanX=!1,preventPanY=!1;if(preventPan===!1){newCTM.e=this.getPan().x;newCTM.f=this.getPan().y;preventPanX=preventPanY=!0}else if(Utils.isObject(preventPan)){if(preventPan.x===!1){newCTM.e=this.getPan().x;preventPanX=!0}else if(Utils.isNumber(preventPan.x)){newCTM.e=preventPan.x}
if(preventPan.y===!1){newCTM.f=this.getPan().y;preventPanY=!0}else if(Utils.isNumber(preventPan.y)){newCTM.f=preventPan.y}}
if((preventPanX&&preventPanY)||!this.isPanDifferent(newCTM)){willPan=!1}else{this.updateCache(newCTM);this.options.onPan(this.getPan())}}
if(willZoom||willPan){this.updateCTMOnNextFrame()}}};ShadowViewport.prototype.isZoomDifferent=function(newCTM){return this.activeState.zoom!==newCTM.a};ShadowViewport.prototype.isPanDifferent=function(newCTM){return(this.activeState.x!==newCTM.e||this.activeState.y!==newCTM.f)};ShadowViewport.prototype.updateCache=function(newCTM){this.activeState.zoom=newCTM.a;this.activeState.x=newCTM.e;this.activeState.y=newCTM.f};ShadowViewport.prototype.pendingUpdate=!1;ShadowViewport.prototype.updateCTMOnNextFrame=function(){if(!this.pendingUpdate){this.pendingUpdate=!0;this.requestAnimationFrame.call(window,this.updateCTMCached)}};ShadowViewport.prototype.updateCTM=function(){var ctm=this.getCTM();SvgUtils.setCTM(this.viewport,ctm,this.defs);this.pendingUpdate=!1;if(this.options.onUpdatedCTM){this.options.onUpdatedCTM(ctm)}};module.exports=function(viewport,options){return new ShadowViewport(viewport,options)}},{"./svg-utilities":5,"./utilities":7},],3:[function(require,module,exports){var svgPanZoom=require("./svg-pan-zoom.js");(function(window,document){if(typeof define==="function"&&define.amd){define("svg-pan-zoom",function(){return svgPanZoom})}else if(typeof module!=="undefined"&&module.exports){module.exports=svgPanZoom;window.svgPanZoom=svgPanZoom}})(window,document)},{"./svg-pan-zoom.js":4},],4:[function(require,module,exports){var Wheel=require("./uniwheel"),ControlIcons=require("./control-icons"),Utils=require("./utilities"),SvgUtils=require("./svg-utilities"),ShadowViewport=require("./shadow-viewport");var SvgPanZoom=function(svg,options){this.init(svg,options)};var optionsDefaults={viewportSelector:".svg-pan-zoom_viewport",panEnabled:!0,controlIconsEnabled:!1,zoomEnabled:!0,dblClickZoomEnabled:!1,mouseWheelZoomEnabled:!0,preventMouseEventsDefault:!0,zoomScaleSensitivity:0.3,minZoom:0.5,maxZoom:10,fit:!0,contain:!1,center:!0,refreshRate:"auto",beforeZoom:null,onZoom:null,beforePan:null,onPan:null,customEventsHandler:null,eventsListenerElement:null,onUpdatedCTM:null,};var passiveListenerOption={passive:!0};SvgPanZoom.prototype.init=function(svg,options){var that=this;this.svg=svg;this.defs=svg.querySelector("defs");SvgUtils.setupSvgAttributes(this.svg);this.options=Utils.extend(Utils.extend({},optionsDefaults),options);this.state="none";var boundingClientRectNormalized=SvgUtils.getBoundingClientRectNormalized(svg);this.width=boundingClientRectNormalized.width;this.height=boundingClientRectNormalized.height;this.viewport=ShadowViewport(SvgUtils.getOrCreateViewport(this.svg,this.options.viewportSelector),{svg:this.svg,width:this.width,height:this.height,fit:this.options.fit,contain:this.options.contain,center:this.options.center,refreshRate:this.options.refreshRate,beforeZoom:function(oldScale,newScale){if(that.viewport&&that.options.beforeZoom){return that.options.beforeZoom(oldScale,newScale)}},onZoom:function(scale){if(that.viewport&&that.options.onZoom){return that.options.onZoom(scale)}},beforePan:function(oldPoint,newPoint){if(that.viewport&&that.options.beforePan){return that.options.beforePan(oldPoint,newPoint)}},onPan:function(point){if(that.viewport&&that.options.onPan){return that.options.onPan(point)}},onUpdatedCTM:function(ctm){if(that.viewport&&that.options.onUpdatedCTM){return that.options.onUpdatedCTM(ctm)}},});var publicInstance=this.getPublicInstance();publicInstance.setBeforeZoom(this.options.beforeZoom);publicInstance.setOnZoom(this.options.onZoom);publicInstance.setBeforePan(this.options.beforePan);publicInstance.setOnPan(this.options.onPan);publicInstance.setOnUpdatedCTM(this.options.onUpdatedCTM);if(this.options.controlIconsEnabled){ControlIcons.enable(this)}
this.lastMouseWheelEventTime=Date.now();this.setupHandlers()};SvgPanZoom.prototype.setupHandlers=function(){var that=this,prevEvt=null;this.eventListeners={mousedown:function(evt){var result=that.handleMouseDown(evt,prevEvt);prevEvt=evt;return result},touchstart:function(evt){var result=that.handleMouseDown(evt,prevEvt);prevEvt=evt;return result},auxclick:function(evt){return that.handleauxclick(evt)},mouseup:function(evt){return that.handleMouseUp(evt)},touchend:function(evt){return that.handleMouseUp(evt)},mousemove:function(evt){return that.handleMouseMove(evt)},touchmove:function(evt){return that.handleMouseMove(evt)},mouseleave:function(evt){return that.handleMouseUp(evt)},touchleave:function(evt){return that.handleMouseUp(evt)},touchcancel:function(evt){return that.handleMouseUp(evt)},};if(this.options.customEventsHandler!=null){this.options.customEventsHandler.init({svgElement:this.svg,eventsListenerElement:this.options.eventsListenerElement,instance:this.getPublicInstance(),});var haltEventListeners=this.options.customEventsHandler.haltEventListeners;if(haltEventListeners&&haltEventListeners.length){for(var i=haltEventListeners.length-1;i>=0;i--){if(this.eventListeners.hasOwnProperty(haltEventListeners[i])){delete this.eventListeners[haltEventListeners[i]]}}}}
for(var event in this.eventListeners){(this.options.eventsListenerElement||this.svg).addEventListener(event,this.eventListeners[event],!this.options.preventMouseEventsDefault?passiveListenerOption:!1)}
if(this.options.mouseWheelZoomEnabled){this.options.mouseWheelZoomEnabled=!1;this.enableMouseWheelZoom()}};SvgPanZoom.prototype.enableMouseWheelZoom=function(){if(!this.options.mouseWheelZoomEnabled){var that=this;this.wheelListener=function(evt){return that.handleMouseWheel(evt)};var isPassiveListener=!this.options.preventMouseEventsDefault;Wheel.on(this.options.eventsListenerElement||this.svg,this.wheelListener,isPassiveListener);this.options.mouseWheelZoomEnabled=!0}};SvgPanZoom.prototype.disableMouseWheelZoom=function(){if(this.options.mouseWheelZoomEnabled){var isPassiveListener=!this.options.preventMouseEventsDefault;Wheel.off(this.options.eventsListenerElement||this.svg,this.wheelListener,isPassiveListener);this.options.mouseWheelZoomEnabled=!1}};SvgPanZoom.prototype.handleMouseWheel=function(evt){if(this.state=="pan"){evt.preventDefault()}
if(!this.options.zoomEnabled){return}
if(this.state!=="pan"){if(!evt.ctrlKey&&!evt.shiftKey){return}
if(this.state!=="none"){return}}
if(this.options.preventMouseEventsDefault){if(evt.preventDefault){evt.preventDefault()}else{evt.returnValue=!1}}
var delta=evt.deltaY||1,timeDelta=Date.now()-this.lastMouseWheelEventTime,divider=3+Math.max(0,30-timeDelta);this.lastMouseWheelEventTime=Date.now();if("deltaMode" in evt&&evt.deltaMode===0&&evt.wheelDelta){delta=evt.deltaY===0?0:Math.abs(evt.wheelDelta)/evt.deltaY}
delta=-0.3<delta&&delta<0.3?delta:((delta>0?1:-1)*Math.log(Math.abs(delta)+10))/divider;var inversedScreenCTM=this.svg.getScreenCTM().inverse(),relativeMousePoint=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(inversedScreenCTM),zoom=Math.pow(1+this.options.zoomScaleSensitivity,-1*delta);this.zoomAtPoint(zoom,relativeMousePoint);if(this.state==="pan"){this.firstEventCTM=this.viewport.getCTM();this.stateOrigin=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.firstEventCTM.inverse())}};SvgPanZoom.prototype.zoomAtPoint=function(zoomScale,point,zoomAbsolute){var originalState=this.viewport.getOriginalState();if(!zoomAbsolute){if(this.getZoom()*zoomScale<this.options.minZoom*originalState.zoom){zoomScale=(this.options.minZoom*originalState.zoom)/this.getZoom()}else if(this.getZoom()*zoomScale>this.options.maxZoom*originalState.zoom){zoomScale=(this.options.maxZoom*originalState.zoom)/this.getZoom()}}else{zoomScale=Math.max(this.options.minZoom*originalState.zoom,Math.min(this.options.maxZoom*originalState.zoom,zoomScale));zoomScale=zoomScale/this.getZoom()}
var oldCTM=this.viewport.getCTM(),relativePoint=point.matrixTransform(oldCTM.inverse()),modifier=this.svg.createSVGMatrix().translate(relativePoint.x,relativePoint.y).scale(zoomScale).translate(-relativePoint.x,-relativePoint.y),newCTM=oldCTM.multiply(modifier);if(newCTM.a!==oldCTM.a){this.viewport.setCTM(newCTM)}};SvgPanZoom.prototype.zoom=function(scale,absolute){this.zoomAtPoint(scale,SvgUtils.getSvgCenterPoint(this.svg,this.width,this.height),absolute)};SvgPanZoom.prototype.publicZoom=function(scale,absolute){if(absolute){scale=this.computeFromRelativeZoom(scale)}
this.zoom(scale,absolute)};SvgPanZoom.prototype.publicZoomAtPoint=function(scale,point,absolute){if(absolute){scale=this.computeFromRelativeZoom(scale)}
if(Utils.getType(point)!=="SVGPoint"){if("x" in point&&"y" in point){point=SvgUtils.createSVGPoint(this.svg,point.x,point.y)}else{throw new Error("Given point is invalid")}}
this.zoomAtPoint(scale,point,absolute)};SvgPanZoom.prototype.getZoom=function(){return this.viewport.getZoom()};SvgPanZoom.prototype.getRelativeZoom=function(){return this.viewport.getRelativeZoom()};SvgPanZoom.prototype.computeFromRelativeZoom=function(zoom){return zoom*this.viewport.getOriginalState().zoom};SvgPanZoom.prototype.resetZoom=function(){var originalState=this.viewport.getOriginalState();this.zoom(originalState.zoom,!0)};SvgPanZoom.prototype.resetPan=function(){this.pan(this.viewport.getOriginalState())};SvgPanZoom.prototype.reset=function(){this.resetZoom();this.resetPan()};SvgPanZoom.prototype.handleDblClick=function(evt){if(this.options.preventMouseEventsDefault){if(evt.preventDefault){evt.preventDefault()}else{evt.returnValue=!1}}
if(this.options.controlIconsEnabled){var targetClass=evt.target.getAttribute("class")||"";if(targetClass.indexOf("svg-pan-zoom-control")>-1){return!1}}
var zoomFactor;if(evt.shiftKey){zoomFactor=1/((1+this.options.zoomScaleSensitivity)*2)}else{zoomFactor=(1+this.options.zoomScaleSensitivity)*2}
var point=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.svg.getScreenCTM().inverse());this.zoomAtPoint(zoomFactor,point)};SvgPanZoom.prototype.handleMouseDown=function(evt,prevEvt){if(evt.button===0){return}
if(this.options.preventMouseEventsDefault){if(evt.preventDefault){if(evt.type!=="touchstart"&&!(evt.touches&&evt.touches.length==1)){evt.preventDefault()}}}
Utils.mouseAndTouchNormalize(evt,this.svg);if(this.options.dblClickZoomEnabled&&Utils.isDblClick(evt,prevEvt)){this.handleDblClick(evt)}else{this.state="pan";this.firstEventCTM=this.viewport.getCTM();this.stateOrigin=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.firstEventCTM.inverse())}};SvgPanZoom.prototype.handleMouseMove=function(evt){if(this.options.preventMouseEventsDefault){if(evt.touches&&evt.touches.length==1){return}
if(evt.preventDefault){evt.preventDefault()}}
if(this.state==="pan"&&this.options.panEnabled){var point=SvgUtils.getEventPoint(evt,this.svg).matrixTransform(this.firstEventCTM.inverse()),viewportCTM=this.firstEventCTM.translate(point.x-this.stateOrigin.x,point.y-this.stateOrigin.y);this.viewport.setCTM(viewportCTM)}};SvgPanZoom.prototype.handleauxclick=function(evt){evt.preventDefault()};SvgPanZoom.prototype.handleMouseUp=function(evt){if(this.options.preventMouseEventsDefault){if(evt.preventDefault){if(evt.type!="touchend"){evt.preventDefault()}}else{evt.returnValue=!1}}
if(this.state==="pan"){this.state="none"}};SvgPanZoom.prototype.fit=function(){var viewBox=this.viewport.getViewBox(),newScale=Math.min(this.width/viewBox.width,this.height/viewBox.height);this.zoom(newScale,!0)};SvgPanZoom.prototype.contain=function(){var viewBox=this.viewport.getViewBox(),newScale=Math.max(this.width/viewBox.width,this.height/viewBox.height);this.zoom(newScale,!0)};SvgPanZoom.prototype.center=function(){var viewBox=this.viewport.getViewBox(),offsetX=(this.width-(viewBox.width+viewBox.x*2)*this.getZoom())*0.5,offsetY=(this.height-(viewBox.height+viewBox.y*2)*this.getZoom())*0.5;this.getPublicInstance().pan({x:offsetX,y:offsetY})};SvgPanZoom.prototype.updateBBox=function(){this.viewport.simpleViewBoxCache()};SvgPanZoom.prototype.pan=function(point){var viewportCTM=this.viewport.getCTM();viewportCTM.e=point.x;viewportCTM.f=point.y;this.viewport.setCTM(viewportCTM)};SvgPanZoom.prototype.panBy=function(point){var viewportCTM=this.viewport.getCTM();viewportCTM.e+=point.x;viewportCTM.f+=point.y;this.viewport.setCTM(viewportCTM)};SvgPanZoom.prototype.getPan=function(){var state=this.viewport.getState();return{x:state.x,y:state.y}};SvgPanZoom.prototype.resize=function(){var boundingClientRectNormalized=SvgUtils.getBoundingClientRectNormalized(this.svg);this.width=boundingClientRectNormalized.width;this.height=boundingClientRectNormalized.height;var viewport=this.viewport;viewport.options.width=this.width;viewport.options.height=this.height;viewport.processCTM();if(this.options.controlIconsEnabled){this.getPublicInstance().disableControlIcons();this.getPublicInstance().enableControlIcons()}};SvgPanZoom.prototype.destroy=function(){var that=this;this.beforeZoom=null;this.onZoom=null;this.beforePan=null;this.onPan=null;this.onUpdatedCTM=null;if(this.options.customEventsHandler!=null){this.options.customEventsHandler.destroy({svgElement:this.svg,eventsListenerElement:this.options.eventsListenerElement,instance:this.getPublicInstance(),})}
for(var event in this.eventListeners){(this.options.eventsListenerElement||this.svg).removeEventListener(event,this.eventListeners[event],!this.options.preventMouseEventsDefault?passiveListenerOption:!1)}
this.disableMouseWheelZoom();this.getPublicInstance().disableControlIcons();this.reset();instancesStore=instancesStore.filter(function(instance){return instance.svg!==that.svg});delete this.options;delete this.viewport;delete this.publicInstance;delete this.pi;this.getPublicInstance=function(){return null}};SvgPanZoom.prototype.getPublicInstance=function(){var that=this;if(!this.publicInstance){this.publicInstance=this.pi={enablePan:function(){that.options.panEnabled=!0;return that.pi},disablePan:function(){that.options.panEnabled=!1;return that.pi},isPanEnabled:function(){return!!that.options.panEnabled},pan:function(point){that.pan(point);return that.pi},panBy:function(point){that.panBy(point);return that.pi},getPan:function(){return that.getPan()},setBeforePan:function(fn){that.options.beforePan=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},setOnPan:function(fn){that.options.onPan=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},enableZoom:function(){that.options.zoomEnabled=!0;return that.pi},disableZoom:function(){that.options.zoomEnabled=!1;return that.pi},isZoomEnabled:function(){return!!that.options.zoomEnabled},enableControlIcons:function(){if(!that.options.controlIconsEnabled){that.options.controlIconsEnabled=!0;ControlIcons.enable(that)}
return that.pi},disableControlIcons:function(){if(that.options.controlIconsEnabled){that.options.controlIconsEnabled=!1;ControlIcons.disable(that)}
return that.pi},isControlIconsEnabled:function(){return!!that.options.controlIconsEnabled},enableDblClickZoom:function(){that.options.dblClickZoomEnabled=!0;return that.pi},disableDblClickZoom:function(){that.options.dblClickZoomEnabled=!1;return that.pi},isDblClickZoomEnabled:function(){return!!that.options.dblClickZoomEnabled},enableMouseWheelZoom:function(){that.enableMouseWheelZoom();return that.pi},disableMouseWheelZoom:function(){that.disableMouseWheelZoom();return that.pi},isMouseWheelZoomEnabled:function(){return!!that.options.mouseWheelZoomEnabled},setZoomScaleSensitivity:function(scale){that.options.zoomScaleSensitivity=scale;return that.pi},setMinZoom:function(zoom){that.options.minZoom=zoom;return that.pi},setMaxZoom:function(zoom){that.options.maxZoom=zoom;return that.pi},setBeforeZoom:function(fn){that.options.beforeZoom=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},setOnZoom:function(fn){that.options.onZoom=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},zoom:function(scale){that.publicZoom(scale,!0);return that.pi},zoomBy:function(scale){that.publicZoom(scale,!1);return that.pi},zoomAtPoint:function(scale,point){that.publicZoomAtPoint(scale,point,!0);return that.pi},zoomAtPointBy:function(scale,point){that.publicZoomAtPoint(scale,point,!1);return that.pi},zoomIn:function(){this.zoomBy(1+that.options.zoomScaleSensitivity);return that.pi},zoomOut:function(){this.zoomBy(1/(1+that.options.zoomScaleSensitivity));return that.pi},getZoom:function(){return that.getRelativeZoom()},setOnUpdatedCTM:function(fn){that.options.onUpdatedCTM=fn===null?null:Utils.proxy(fn,that.publicInstance);return that.pi},resetZoom:function(){that.resetZoom();return that.pi},resetPan:function(){that.resetPan();return that.pi},reset:function(){that.reset();return that.pi},fit:function(){that.fit();return that.pi},contain:function(){that.contain();return that.pi},center:function(){that.center();return that.pi},updateBBox:function(){that.updateBBox();return that.pi},resize:function(){that.resize();return that.pi},getSizes:function(){return{width:that.width,height:that.height,realZoom:that.getZoom(),viewBox:that.viewport.getViewBox(),}},destroy:function(){that.destroy();return that.pi},}}
return this.publicInstance};var instancesStore=[];var svgPanZoom=function(elementOrSelector,options){var svg=Utils.getSvg(elementOrSelector);if(svg===null){return null}else{for(var i=instancesStore.length-1;i>=0;i--){if(instancesStore[i].svg===svg){return instancesStore[i].instance.getPublicInstance()}}
instancesStore.push({svg:svg,instance:new SvgPanZoom(svg,options),});return instancesStore[instancesStore.length-1].instance.getPublicInstance()}};module.exports=svgPanZoom},{"./control-icons":1,"./shadow-viewport":2,"./svg-utilities":5,"./uniwheel":6,"./utilities":7,},],5:[function(require,module,exports){var Utils=require("./utilities"),_browser="unknown";if(!1||!!document.documentMode){_browser="ie"}
module.exports={svgNS:"http://www.w3.org/2000/svg",xmlNS:"http://www.w3.org/XML/1998/namespace",xmlnsNS:"http://www.w3.org/2000/xmlns/",xlinkNS:"http://www.w3.org/1999/xlink",evNS:"http://www.w3.org/2001/xml-events",getBoundingClientRectNormalized:function(svg){if(svg.clientWidth&&svg.clientHeight){return{width:svg.clientWidth,height:svg.clientHeight,}}else if(!!svg.getBoundingClientRect()){return svg.getBoundingClientRect()}else{throw new Error("Cannot get BoundingClientRect for SVG.")}},getOrCreateViewport:function(svg,selector){var viewport=null;if(Utils.isElement(selector)){viewport=selector}else{viewport=svg.querySelector(selector)}
if(!viewport){var childNodes=Array.prototype.slice.call(svg.childNodes||svg.children).filter(function(el){return(el.nodeName!=="defs"&&el.nodeName!=="#text")});if(childNodes.length===1&&childNodes[0].nodeName==="g"&&childNodes[0].getAttribute("transform")===null){viewport=childNodes[0]}}
if(!viewport){var viewportId="viewport-"+new Date().toISOString().replace(/\D/g,"");viewport=document.createElementNS(this.svgNS,"g");viewport.setAttribute("id",viewportId);var svgChildren=svg.childNodes||svg.children;if(!!svgChildren&&svgChildren.length>0){for(var i=svgChildren.length;i>0;i--){if(svgChildren[svgChildren.length-i].nodeName!=="defs"){viewport.appendChild(svgChildren[svgChildren.length-i])}}}
svg.appendChild(viewport)}
var classNames=[];if(viewport.getAttribute("class")){classNames=viewport.getAttribute("class").split(" ")}
if(!~classNames.indexOf("svg-pan-zoom_viewport")){classNames.push("svg-pan-zoom_viewport");viewport.setAttribute("class",classNames.join(" "))}
return viewport},setupSvgAttributes:function(svg){svg.setAttribute("xmlns",this.svgNS);svg.setAttributeNS(this.xmlnsNS,"xmlns:xlink",this.xlinkNS);svg.setAttributeNS(this.xmlnsNS,"xmlns:ev",this.evNS);if(svg.parentNode!==null){var style=svg.getAttribute("style")||"";if(style.toLowerCase().indexOf("overflow")===-1){svg.setAttribute("style","overflow: hidden; "+style)}}},internetExplorerRedisplayInterval:300,refreshDefsGlobal:Utils.throttle(function(){var allDefs=document.querySelectorAll("defs");var allDefsCount=allDefs.length;for(var i=0;i<allDefsCount;i++){var thisDefs=allDefs[i];thisDefs.parentNode.insertBefore(thisDefs,thisDefs)}},this?this.internetExplorerRedisplayInterval:null),setCTM:function(element,matrix,defs){var that=this,s="matrix("+matrix.a+","+matrix.b+","+matrix.c+","+matrix.d+","+matrix.e+","+matrix.f+")";element.setAttributeNS(null,"transform",s);if("transform" in element.style){element.style.transform=s}else if("-ms-transform" in element.style){element.style["-ms-transform"]=s}else if("-webkit-transform" in element.style){element.style["-webkit-transform"]=s}
if(_browser==="ie"&&!!defs){defs.parentNode.insertBefore(defs,defs);window.setTimeout(function(){that.refreshDefsGlobal()},that.internetExplorerRedisplayInterval)}},getEventPoint:function(evt,svg){var point=svg.createSVGPoint();Utils.mouseAndTouchNormalize(evt,svg);point.x=evt.clientX;point.y=evt.clientY;return point},getSvgCenterPoint:function(svg,width,height){return this.createSVGPoint(svg,width/2,height/2)},createSVGPoint:function(svg,x,y){var point=svg.createSVGPoint();point.x=x;point.y=y;return point},}},{"./utilities":7},],6:[function(require,module,exports){module.exports=(function(){var prefix="",_addEventListener,_removeEventListener,support,fns=[];var passiveListenerOption={passive:!0};var activeListenerOption={passive:!1};if(window.addEventListener){_addEventListener="addEventListener";_removeEventListener="removeEventListener"}else{_addEventListener="attachEvent";_removeEventListener="detachEvent";prefix="on"}
support="onwheel" in document.createElement("div")?"wheel":document.onmousewheel!==undefined?"mousewheel":"DOMMouseScroll";function createCallback(element,callback){var fn=function(originalEvent){!originalEvent&&(originalEvent=window.event);var event={originalEvent:originalEvent,target:originalEvent.target||originalEvent.srcElement,type:"wheel",deltaMode:originalEvent.type=="MozMousePixelScroll"?0:1,deltaX:0,delatZ:0,preventDefault:function(){originalEvent.preventDefault?originalEvent.preventDefault():(originalEvent.returnValue=!1)},};if(support=="mousewheel"){event.deltaY=(-1/40)*originalEvent.wheelDelta;originalEvent.wheelDeltaX&&(event.deltaX=(-1/40)*originalEvent.wheelDeltaX)}else{event.deltaY=originalEvent.detail}
return callback(event)};fns.push({element:element,fn:fn,});return fn}
function getCallback(element){for(var i=0;i<fns.length;i++){if(fns[i].element===element){return fns[i].fn}}
return function(){}}
function removeCallback(element){for(var i=0;i<fns.length;i++){if(fns[i].element===element){return fns.splice(i,1)}}}
function _addWheelListener(elem,eventName,callback,isPassiveListener){var cb;if(support==="wheel"){cb=callback}else{cb=createCallback(elem,callback)}
elem[_addEventListener](prefix+eventName,cb,isPassiveListener?passiveListenerOption:activeListenerOption)}
function _removeWheelListener(elem,eventName,callback,isPassiveListener){var cb;if(support==="wheel"){cb=callback}else{cb=getCallback(elem)}
elem[_removeEventListener](prefix+eventName,cb,isPassiveListener?passiveListenerOption:activeListenerOption);removeCallback(elem)}
function addWheelListener(elem,callback,isPassiveListener){_addWheelListener(elem,support,callback,isPassiveListener);if(support=="DOMMouseScroll"){_addWheelListener(elem,"MozMousePixelScroll",callback,isPassiveListener)}}
function removeWheelListener(elem,callback,isPassiveListener){_removeWheelListener(elem,support,callback,isPassiveListener);if(support=="DOMMouseScroll"){_removeWheelListener(elem,"MozMousePixelScroll",callback,isPassiveListener)}}
return{on:addWheelListener,off:removeWheelListener,}})()},{},],7:[function(require,module,exports){module.exports={extend:function(target,source){target=target||{};for(var prop in source){if(this.isObject(source[prop])){target[prop]=this.extend(target[prop],source[prop])}else{target[prop]=source[prop]}}
return target},isElement:function(o){return(o instanceof HTMLElement||o instanceof SVGElement||o instanceof SVGSVGElement||(o&&typeof o==="object"&&o!==null&&o.nodeType===1&&typeof o.nodeName==="string"))},isObject:function(o){return(Object.prototype.toString.call(o)==="[object Object]")},isNumber:function(n){return!isNaN(parseFloat(n))&&isFinite(n)},getSvg:function(elementOrSelector){var element,svg;if(!this.isElement(elementOrSelector)){if(typeof elementOrSelector==="string"||elementOrSelector instanceof String){element=document.querySelector(elementOrSelector);if(!element){throw new Error("Provided selector did not find any elements. Selector: "+elementOrSelector);return null}}else{throw new Error("Provided selector is not an HTML object nor String");return null}}else{element=elementOrSelector}
if(element.tagName.toLowerCase()==="svg"){svg=element}else{if(element.tagName.toLowerCase()==="object"){svg=element.contentDocument.documentElement}else{if(element.tagName.toLowerCase()==="embed"){svg=element.getSVGDocument().documentElement}else{if(element.tagName.toLowerCase()==="img"){throw new Error('Cannot script an SVG in an "img" element. Please use an "object" element or an in-line SVG.')}else{throw new Error("Cannot get SVG.")}
return null}}}
return svg},proxy:function(fn,context){return function(){return fn.apply(context,arguments)}},getType:function(o){return Object.prototype.toString.apply(o).replace(/^\[object\s/,"").replace(/\]$/,"")},mouseAndTouchNormalize:function(evt,svg){if(evt.clientX===void 0||evt.clientX===null){evt.clientX=0;evt.clientY=0;if(evt.touches!==void 0&&evt.touches.length){if(evt.touches[0].clientX!==void 0){evt.clientX=evt.touches[0].clientX;evt.clientY=evt.touches[0].clientY}else if(evt.touches[0].pageX!==void 0){var rect=svg.getBoundingClientRect();evt.clientX=evt.touches[0].pageX-rect.left;evt.clientY=evt.touches[0].pageY-rect.top}}else if(evt.originalEvent!==void 0){if(evt.originalEvent.clientX!==void 0){evt.clientX=evt.originalEvent.clientX;evt.clientY=evt.originalEvent.clientY}}}},isDblClick:function(evt,prevEvt){if(evt.detail===2){return!0}else if(prevEvt!==void 0&&prevEvt!==null){var timeStampDiff=evt.timeStamp-prevEvt.timeStamp,touchesDistance=Math.sqrt(Math.pow(evt.clientX-prevEvt.clientX,2)+Math.pow(evt.clientY-prevEvt.clientY,2));return timeStampDiff<250&&touchesDistance<10}
return!1},now:Date.now||function(){return new Date().getTime()},throttle:function(func,wait,options){var that=this;var context,args,result;var timeout=null;var previous=0;if(!options){options={}}
var later=function(){previous=options.leading===!1?0:that.now();timeout=null;result=func.apply(context,args);if(!timeout){context=args=null}};return function(){var now=that.now();if(!previous&&options.leading===!1){previous=now}
var remaining=wait-(now-previous);context=this;args=arguments;if(remaining<=0||remaining>wait){clearTimeout(timeout);timeout=null;previous=now;result=func.apply(context,args);if(!timeout){context=args=null}}else if(!timeout&&options.trailing!==!1){timeout=setTimeout(later,remaining)}
return result}},createRequestAnimationFrame:function(refreshRate){var timeout=null;if(refreshRate!=="auto"&&refreshRate<60&&refreshRate>1){timeout=Math.floor(1000/refreshRate)}
if(timeout===null){return(window.requestAnimationFrame||requestTimeout(33))}else{return requestTimeout(timeout)}},};function requestTimeout(timeout){return function(callback){window.setTimeout(callback,timeout)}}},{},],},{},[3])
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
                
                // Solo procesar si es un enlace interno (empieza con #)
                if (href && href.startsWith("#")) {
                    e.preventDefault(); // evita el salto instantáneo

                    const targetId = href.substring(1); // substring quita el "#"
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

// Función para hacer elementos editables con doble clic
function makeElementsEditable() {
    // Seleccionar todos los elementos que coincidan con el patrón
    const elements = document.querySelectorAll("#nav-thumbs > div > p");
    
    elements.forEach(element => {
        // Agregar event listener para doble clic
        element.addEventListener('dblclick', function(e) {
            e.preventDefault();
            startEditing(this);
        });
        
        // Opcional: agregar cursor pointer para indicar que es editable
        element.style.cursor = 'pointer';
        element.title = 'Doble clic para editar';
    });
}

function startEditing(element) {
    // Verificar si ya está siendo editado
    if (element.querySelector('.edit-input')) {
        return;
    }
    
    // Obtener el texto actual
    const currentText = element.textContent;
    
    // Crear el input de edición
    const input = document.createElement('input');
    input.type = 'text';
    input.value = currentText;
    input.className = 'edit-input';
    
    // Estilos para el input
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
    
    // Ocultar el texto original temporalmente
    const originalDisplay = element.style.display;
    element.style.position = 'relative';
    
    // Guardar el contenido original y limpiarlo
    const originalContent = element.innerHTML;
    element.innerHTML = '';
    element.appendChild(input);
    
    // Enfocar y seleccionar todo el texto
    input.focus();
    input.select();
    
    // Función para confirmar los cambios
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
    
    // Función para cancelar los cambios
    function cancelEdit() {
        element.innerHTML = originalContent;
        element.style.display = originalDisplay;
    }
    
    // Event listeners para el input
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
    
    // Confirmar al perder el foco (opcional)
    input.addEventListener('blur', function(e) {
        // Pequeño delay para permitir que otros eventos se procesen primero
        setTimeout(() => {
            if (element.querySelector('.edit-input')) {
                confirmEdit();
            }
        }, 100);
    });
    
    // Prevenir que el clic en el input active otros eventos
    input.addEventListener('click', function(e) {
        e.stopPropagation();
    });
}

// Funciones que permiten cambiar orden de los SVG
let draggedElementNavThumb = null;
let originalOrderNavThumb = [];

function initDragRepositionNavThumb() {
    const container = document.getElementById('nav-thumbs');
    if (!container) return;

    // Inicializar índices automáticamente
    initializeOriginalIndices();
    
    // Guardar orden inicial
    saveOriginalOrderNavThumb();

    container.addEventListener('mousedown', (e) => {
        // Buscar el elemento nav-thumb más cercano hacia arriba
        const navThumbElement = e.target.closest('.nav-thumb');
        if (navThumbElement) {
            // REINICIAR: Reasignar los índices originales para que el nuevo orden sea [1,2,3...]
            resetOriginalIndices();
            // Actualizar el orden original para futuras comparaciones
            originalOrderNavThumb = Array.from(container.children).map((child, index) => index + 1);
            // Activar draggable solo al presionar mouse
            navThumbElement.draggable = true;
        }
    });

    container.addEventListener('dragstart', (e) => {
        // Buscar el elemento nav-thumb más cercano hacia arriba
        const navThumbElement = e.target.closest('.nav-thumb');
        if (navThumbElement) {
            draggedElementNavThumb = navThumbElement;
            navThumbElement.classList.add('dragging');
        }
    });

    container.addEventListener('dragend', (e) => {
        // Buscar el elemento nav-thumb más cercano hacia arriba
        const navThumbElement = e.target.closest('.nav-thumb');
        if (navThumbElement) {
            navThumbElement.classList.remove('dragging');
            // Desactivar draggable al terminar
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
    // Crear orden secuencial [1, 2, 3, 4, 5...]
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
    
    // Crear array numérico basado en los data-original-index de los elementos en su orden actual
    const currentOrder = Array.from(container.children).map(child => {
        return parseInt(child.dataset.originalIndex);
    });

    const hasChanged = !arraysEqual(originalOrderNavThumb, currentOrder);
    
    if (hasChanged) {
        console.log('Reposicionamiento completado - Posición cambiada:', {
            ordenAnterior: originalOrderNavThumb,
            ordenActual: currentOrder
        });
        
        // REINICIAR: Reasignar los índices originales para que el nuevo orden sea [1,2,3...]
        resetOriginalIndices();
        // Actualizar el orden original para futuras comparaciones
        originalOrderNavThumb = Array.from(container.children).map((child, index) => index + 1);
        
        // Enviar nuevo orden a la API
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

// Función auxiliar para inicializar los índices originales en los elementos
function initializeOriginalIndices() {
    const container = document.getElementById('nav-thumbs');
    if (!container) return;
    
    Array.from(container.children).forEach((child, index) => {
        child.dataset.originalIndex = index + 1;
    });
}

// Función para reiniciar los índices después de un cambio
function resetOriginalIndices() {
    const container = document.getElementById('nav-thumbs');
    if (!container) return;
    
    // Reasignar los índices basándose en el orden actual
    Array.from(container.children).forEach((child, index) => {
        child.dataset.originalIndex = index + 1;
    });
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


    const hrline = document.createElement("hr");
    hrline.style.margin = "0px";
    hrline.style.borderColor= "#000";
    
    // Crear opciones
    const option1 = document.createElement("div");
    option1.textContent = "Editar";
    option1.onclick = () => {
        menu.remove();
        style.remove();
        let svgHtml = limpiarAtributosDuplicados(this.outerHTML);
        pywebview.api.open_svg_editor(svgHtml, this.id);
    };

    const option2 = document.createElement("div");
    option2.textContent = "Añadir svg arriba";
    option2.onclick = () => {
        menu.remove();
        style.remove();
                            
        pywebview.api.add_new_SVG(this.id, true, undefined);
    };
    
    const option3 = document.createElement("div");
    option3.textContent = "Añadir svg abajo";
    option3.onclick = () => {
        menu.remove();
        style.remove();
        
        pywebview.api.add_new_SVG(this.id, undefined, true);
    };
    
    const option4 = document.createElement("div");
    option4.textContent = "Eliminar";
    option4.onclick = () => {
        menu.remove();
        style.remove();
        
        if (confirm("¿Estás seguro de que deseas eliminar esta página?")) {
            // Si el usuario hace clic en "Aceptar", llama a la función de Python
            pywebview.api.delete_this_SVG(this.id);
        }
    };
    
    const option5 = document.createElement("div");
    option5.textContent = "Actualizar icono";
    option5.onclick = () => {
        menu.remove();
        style.remove();
        
        let clone_svg = this.cloneNode(true);
        
        window.cleanElementSVGAdded(clone_svg);
        
        window.final_svg_edit = clone_svg;
        
        pywebview.api.refresh_svg_icon();
    };
    
    const option6 = document.createElement("div");
    option6.textContent = "Añadir página vacia arriba";
    option6.onclick = () => {
        menu.remove();
        style.remove();
        
        pywebview.api.add_new_SVG(this.id, true, undefined, true);
    };
    
    const option7 = document.createElement("div");
    option7.textContent = "Añadir página vacia abajo";
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

// Inicializar cuando el DOM esté listo
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
            <button onclick="openFile()">Abrir archivo HTML</button>
            <span id="currentFile" class="filename">Sin archivo</span>
        </div>
        
        <div class="section">
            <button id="openPreviewButton" onclick="open_preview()">Open editable preview 🖋️🏞️</button>
        </div>
        
        <div class="section">
            <button onclick="saveAs()">Guardar como</button>
        </div>
        
        <div id="status"></div>
        
        <div class="section">
            <span style="font-family: monospace;">Contenido actual:</span>
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
                            showStatus('Archivo cargado correctamente');
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

        // Cargar contenido actual al iniciar, pywebviewready se activa cuando se cargo el DOM y la api de pywebview
        window.addEventListener('pywebviewready', function () {
            pywebview.api.get_current_content().then(result => {
                updateContent(result.content, result.filename);
            });
        });
    </script>
</body>
</html>
"""