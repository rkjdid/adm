function loadjscssfile(filename, filetype){
    var fileref;
    if (filetype=="js"){ //if filename is a external JavaScript file
        fileref=document.createElement('script');
        fileref.setAttribute("type","text/javascript");
        fileref.setAttribute("src", filename);
    }
    else if (filetype=="css"){ //if filename is an external CSS file
        fileref=document.createElement("link");
        fileref.setAttribute("rel", "stylesheet");
        fileref.setAttribute("type", "text/css");
        fileref.setAttribute("href", filename);
    }
    if (typeof fileref!="undefined")
        document.getElementsByTagName("head")[0].appendChild(fileref)
}

//function unloadJs(filename){
//    var targetElement = "script"; // in case of css this will be "link"
//    var targetAttr = "src"; // in case of css this will be "href"
//
//    var allCtrl = document.getElementsByTagName(targetElement);
//    for (var i=allCtrl.length; i>=0; i--)  { //search backwards within nodelist for matching elements to remove
//        if (allCtrl[i] && allCtrl[i].getAttribute(targetAttr)!=null && allCtrl[i].getAttribute(targetAttr).indexOf(filename)!=-1)
//            allCtrl[i].parentNode.removeChild(allCtrl[i]);
//    }
//}

function unloadCss(filename){
    var targetElement = "link"; // in case of css this will be "link"
    var targetAttr = "href"; // in case of css this will be "href"

    var allCtrl = document.getElementsByTagName(targetElement);
    for (var i=allCtrl.length; i>=0; i--)  { //search backwards within nodelist for matching elements to remove
        if (allCtrl[i] && allCtrl[i].getAttribute(targetAttr)!=null && allCtrl[i].getAttribute(targetAttr).indexOf(filename)!=-1)
            allCtrl[i].parentNode.removeChild(allCtrl[i]);
    }
}

var flipped = false;

//function toggleLoadFlip() {
//    if (flipped)
//        loadjscssfile("/static/css/pageflipAdd.css", "css");
//    else
//        unloadCss("/static/css/pageflipAdd.css");
//    flipped = !flipped;
//}

function toggleLoadN(filename, ext) {
    if (flipped)
        loadjscssfile(filename, ext);
    else
        unloadCss(filename);
    flipped = !flipped;
}

//loadjscssfile("myscript.js", "js") //dynamically load and add this .js file
//loadjscssfile("javascript.php", "js") //dynamically load "javascript.php" as a JavaScript file
//loadjscssfile("mystyle.css", "css") ////dynamically load and add this .css file