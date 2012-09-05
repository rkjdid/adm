var tvScreen, tvContext;
var lcdScreen, lcdContext;

var contourDrawn = false;

var mireURL =       "http://rk.dyndns-server.com/ateliers.media/resources/5.clients.tvMire.png";
var contourURL =    "http://rk.dyndns-server.com/ateliers.media/resources/5.clients.tvShade.png";

var runningInterval;

window.onload = function ()
{
//    defaultDisplay();
    preloadImages();
};

$(document).ready(function () {
    tvScreen = $('#tvScreen')[0];
    lcdScreen = $('#tvLcd')[0];
    tvContext = tvScreen.getContext("2d");
    lcdContext = lcdScreen.getContext("2d");
    drawMire();
    defaultDisplay();
    //TODO: make default display flash (avoid unloaded font and not working default display)
});

//TODO: JQuery this
function preloadImages()
{
    var menu = document.getElementById("tvIndex");
    for (var i=0; i < menu.children.length; i++)
    {
        var li = menu.children[i];

        var div = document.getElementById(li.getAttribute('value'));

        for (var j = 0; j < div.children.length; j++)
        {
            var span_img = div.children[j];
            var spanUrl;
            if (span_img.tagName == 'SPAN')
                spanUrl = span_img.innerHTML;
            if (span_img.tagName == 'IMG')
                if (span_img.getAttribute('src') == '')
                {
                    span_img.setAttribute('src', spanUrl);
                    span_img.setAttribute('class', 'cli-' + li.getAttribute('value'));
                }
        }
    }
//    alert('Images loaded');
}

function drawMire()
{
    var mire = new Image();
    mire.src = mireURL;
    mire.onload = function(){
        tvContext.drawImage(mire, 0, 0);
    };

    contourDrawn = false;
//    alert('Mire drawn');
}


function defaultDisplay ()
{
    var cnt = 0;
    runningInterval = setInterval(function() {
        if (cnt > 40) {
            clearInterval(runningInterval);
            return;
        }

        cnt++;
        clearDisplay();
        lcdContext.font = "14px digital";
        //        setTimeout (function (){
        lcdContext.fillText("/!\\ ERREUR", 17, 28);
        lcdContext.font = "12px";
        lcdContext.fillText("---------->",20, 48);
        //        }, 800);
    }, 50);
}

function clearDisplay() {
    lcdContext.clearRect(0, 0, lcdScreen.width, lcdScreen.height);
}

function digitalDisplay(nb, text)
{
    // font = 14px -> 13char max
    // 10 px hauteur (saut de ligne) minimum

    if (text.length > 12)
    {
        text = text.substring(0, 12) + '-';
    }
    var cnt = 0;
    runningInterval = setInterval(function() {
        if (cnt > 40) {
            clearInterval(runningInterval);
            return;
        }

        cnt++;
        lcdContext.clearRect(0, 0, lcdScreen.width, lcdScreen.height);
        lcdContext.font = "36px digital";
        lcdContext.fillText(nb, 70, 28);
        lcdContext.font = "14px digital";
        lcdContext.fillText(text, 2, 49);
    }, 50);
}

function zapChannel(nb, nom)
{
    clearInterval(runningInterval);
    digitalDisplay(nb, nom);
    drawLogos(nb, 0, false);
}

function drawContour()
{
    var contour = new Image();
    contour.src = contourURL;
    contour.onload = function(){
        tvContext.drawImage(contour, 0, 0);
    };

    contourDrawn = true;
}

function drawLogos(cat, firstIndex, yoffset) {
    var images = $('.cli-cat' + cat);

    var logoW = 110;
    var logoH = 84;

    var x = 25;
    var y = 12 + 30;

    if (yoffset)
        y += logoH + 30;

    // Draw contour ombré (only once)
    if (!contourDrawn) // TODO: fadein
    {
        tvContext.clearRect(0, 0, tvScreen.width, tvScreen.height);
        drawContour();
    } else // TODO: fadeout
        tvContext.clearRect(18, 18, tvScreen.width - 36, tvScreen.height - 36);

    // Draw page number
    if (images.length > 3)
    {
        var totalPNB;
        if (images.length%3 != 0)
            totalPNB = Math.round(images.length/3 + 0.3);
        else
            totalPNB = images.length / 3;
        $('#clientPageNb')[0].innerHTML =  "" + (firstIndex/3 + 1) + "/" + totalPNB;
    }
    else
        $('#clientPageNb')[0].innerHTML =  "1/1";

    var nbLoop = 3;
    for (var i = firstIndex; i < images.length && i < firstIndex + nbLoop; i++)
    {

        // TODO: fadein
        tvContext.drawImage(images[i],
                            x + (logoW - images[i].naturalWidth)/2,
                            y + (logoH - images[i].naturalHeight)/2);
//        // Write brand name below logo
//        tvContext.font("sans-serif 12px");
//        tvContext.fontcolor("green");
//        tvContext.measureText("...")

//        // Debug rect
//        tvContext.fillStyle = "rgb(150,29,28)";
//        tvContext.fillRect(x, y, logoW, logoH);
        x += logoW + 2;

        if (y > logoH)
            y -= (logoH + 30);
        else
            y += (logoH + 30);
    }

    // Set buttons values according to the categorie
    if (images.length > firstIndex + 3)
    {
        $('#tvButton')[0].setAttribute(
            "class",
            "active");
        $('#tvButton')[0].setAttribute(
            "onclick",
            "drawLogos(" + cat + "," + (firstIndex + 3) + "," + (!yoffset) + ");");
        $('#tvButton2')[0].setAttribute(
            "class",
            "active");
        $('#tvButton2')[0].setAttribute(
            "onclick",
            "drawLogos(" + cat + "," + (firstIndex + 3) + "," + (!yoffset) + ");");

    }
    else if (images.length > 3)
    {
        $('#tvButton')[0].setAttribute(
            "class",
            "active");
        $('#tvButton')[0].setAttribute(
            "onclick",
            "drawLogos(" + cat + ",0 ," + (!yoffset) + ");");
        $('#tvButton2')[0].setAttribute(
            "class",
            "active");
        $('#tvButton2')[0].setAttribute(
            "onclick",
            "drawLogos(" + cat + ",0 ," + (!yoffset) + ");");
    }
    else
    {
        $('#tvButton')[0].setAttribute(
            "class",
            "");
        $('#tvButton')[0].setAttribute(
            "onclick",
            "");
        $('#tvButton2')[0].setAttribute(
            "class",
            "");
        $('#tvButton2')[0].setAttribute(
            "onclick",
            "");
    }
}
