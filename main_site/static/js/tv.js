var tvScreen, tvContext;
var lcdScreen, lcdContext;

window.onload = function ()
{
    defaultDisplay();
    preloadImages();

//    alert('Images loaded');
}

$(document).ready(function () {
    tvScreen = document.getElementById("tvScreen");
    lcdScreen = document.getElementById("tvLcd");
    tvContext = tvScreen.getContext("2d");
    lcdContext = lcdScreen.getContext("2d");
    drawMire();
    defaultDisplay();
//    alert('Mire drawn');
});

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
}

function drawMire()
{
    var mire = new Image();
    mire.src = "http://192.168.1.253/ateliers.media/resources/img.pdf/tvScreen.png";
    mire.onload = function(){
        tvContext.drawImage(mire, 0, 0);
    }
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
//    var step = document.getElementById(cat);
    var images = document.getElementsByClassName('cli-cat' + cat)

    var x = 15;
    var y = -20;
    tvContext.clearRect(0, 0, screen.width, screen.height);
    for (var i = 0; i < images.length; i++)
    {
        tvContext.drawImage(images[i], x, y, 50, 50);
        y += 50;
    }
}
