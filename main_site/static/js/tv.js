var tvScreen, tvContext;
var lcdScreen, lcdContext;
var displayed;
var imgLoaded = new Array();

window.onload = function ()
{
    defaultDisplay();
    preloadImages();
}

$(document).ready(function () {
    tvScreen = $('#tvScreen')[0];
    lcdScreen = $('#tvLcd')[0];
    tvContext = tvScreen.getContext("2d");
    lcdContext = lcdScreen.getContext("2d");
    drawMire();
    defaultDisplay();
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
    mire.src = "http://rk.dyndns-server.com/ateliers.media/resources/img.pdf/tvScreen.png";
    mire.onload = function(){
        tvContext.drawImage(mire, 0, 0);
    }

//    alert('Mire drawn');
}

function defaultDisplay ()
{
    lcdContext.clearRect(0, 0, lcdScreen.width, lcdScreen.height);
    lcdContext.font = "14px digital";
    lcdContext.fillText("/!\\FATAL ERROR", 2, 22);
    lcdContext.font = "12px digital";
    lcdContext.fillText("select a channel",10, 42);
}

function digitalDisplay(nb, text)
{
    // font = 14px -> 13char max
    // 10 px hauteur (saut de ligne) minimum

    if (text.length > 12)
    {
        text = text.substring(0, 12) + '-';
    }

    lcdContext.clearRect(0, 0, lcdScreen.width, lcdScreen.height);
    lcdContext.font = "36px digital";
    lcdContext.fillText(nb, 70, 28);
    lcdContext.font = "14px digital";
    lcdContext.fillText(text, 2, 49);
}

function zapChannel(nb, nom)
{
    digitalDisplay(nb, nom);
    drawLogos(nb);
}

function drawLogos(cat)
{
    var images = $('.cli-cat' + cat);

    var logoW = 60;
    var logoH = 60;

    var x = 25;
    var y = tvScreen.height / 2 - logoH / 2;
    tvContext.clearRect(0, 0, tvScreen.width, tvScreen.height);
    for (var i = 0; i < images.length; i++)
    {
        tvContext.drawImage(images[i], x, y, logoW, logoH);
//        // Write brand name below logo
//        tvContext.font("sans-serif 12px");
//        tvContext.fontcolor("green");
//        tvContext.measureText("...")
//
        x += logoW*1.5;
    }
}
