var tvScreen, tvContext;
var lcdScreen, lcdContext;

var contourDrawn = false;

var mireURL =       "/static/img/5.clients.tvMire.png";
var contourURL =    "/static/img/5.clients.tvShade.png";

var runningInterval;

window.onload = function ()
{
    preloadImages();
};

$(document).ready(function () {
    tvScreen = $('#tvScreen')[0];
    lcdScreen = $('#tvLcd')[0];
    tvContext = tvScreen.getContext("2d");
    lcdContext = lcdScreen.getContext("2d");

    $('.tvIndex').click(function() {
        if ($(this).is('.tvIndex.active'))
            return;

        $('.tvIndex.active').removeClass('active');
        $(this).addClass('active');
    });

    drawMire();
    defaultDisplay();
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
    mire.src = mireURL;
    mire.onload = function(){
        tvContext.drawImage(mire, 0, 0);
    };

    contourDrawn = false;
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
        lcdContext.fillText("---------->", 16, 48);
        //        }, 800);
    }, 50);
}

function clearDisplay() {
    lcdContext.clearRect(0, 0, lcdScreen.width, lcdScreen.height);
}

function digitalDisplay(nb, text)
{
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
    drawLogos(nb);
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

function drawLogos (cat) {
    var images = $('.cli-cat' + cat);
    var nbImages = images.length;

    var gapCol, gapLig, nbCol, nbLig, logoH, logoW, ratio;

    logoH = 90;
    logoW = 90;

    if (nbImages <= 3) {
        ratio = 1;

        nbLig = 1;
        nbCol = 3;
        gapLig = 80;
        gapCol = 21;
    } else if (nbImages <= 6) {
        ratio = 80/logoH;
        logoH = 80;
        logoW = 80;

        nbLig = 2;
        nbCol = 3;
        gapLig = 30;
        gapCol = 30;
    } else if (nbImages <= 12) {
        ratio = 65/logoH;
        logoH = logoW = 65;

        nbLig = 3;
        nbCol = 4;
        gapLig = 18;
        gapCol = 19;
    } else if (nbImages <= 20) {
        ratio = 50/logoH;
        logoH = logoW = 50;

        nbLig = 4;
        nbCol = 5;
        gapLig = 12;
        gapCol = 16;
    } else {
        alert('Max logo number = 20');
    }

    // Draw contour ombré (only once)
    if (!contourDrawn) // TODO: fadein
    {
        tvContext.clearRect(0, 0, tvScreen.width, tvScreen.height);
        drawContour();
    } else // TODO: fadeout
        tvContext.clearRect(18, 18, tvScreen.width - 36, tvScreen.height - 36);

    var yOffset = 15;
    var i = 0;

    for (var l = 0; l < nbLig; l++) {
        yOffset += gapLig;
        var xOffset = 15;
        for (var c = 0; c < nbCol; c++) {
            xOffset += gapCol;

            if (i == nbImages)
                break;

            tvContext.drawImage(images[i],
                                xOffset + (logoW - ratio*images[i].naturalWidth)/2,
                                yOffset + (logoH - ratio*images[i].naturalHeight)/2,
                                ratio * images[i].naturalWidth,
                                ratio * images[i].naturalHeight);
            i++;
            xOffset += logoW;
        }

        yOffset += logoH;
    }
}
