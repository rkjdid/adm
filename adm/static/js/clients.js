var tvScreen, tvContext;
var lcdScreen, lcdContext;

var contourDrawn = false;

var mireURL =       "/static/img/5.clients.tvMire.png";
var contourURL =    "/static/img/5.clients.tvShade.png";

var textInterval, logoInterval, demoInterval;

window.onload = function ()
{
    tvScreen = $('#tvScreen')[0];
    lcdScreen = $('#tvLcd')[0];
//    tvContext = tvScreen.getContext("2d");
//    lcdContext = lcdScreen.getContext("2d");

    $('li.tvIndex').click(function() {

    });

//    drawMire();
//    defaultDisplay();

    preloadImages();
};

var aa, aaCpt, nbLiActive = 0;

function preloadImages()
{
    var menu = document.getElementById("tvIndex");
    aa = new Array(menu.children.length);
    aaCpt = new Array(menu.children.length);

    // Init array
    for (var tmp = 0; tmp < aaCpt.length; tmp++)
        aaCpt[tmp] = 0;

    for (var i=0; i < menu.children.length; i++)
    {
        var li = menu.children[i];
        var div = document.getElementById($(li).find('.dataCat').html());
        aa[i] = new Array(div.children.length);

        for (var j = 0; j < div.children.length; j++)
        {
            var divCont = div.children[j];

            var span = $(divCont).find('span');
            var img = $(divCont).find('img');

            var url = span.html();
            setOnLoad(img[0], i, j, li);
            img[0].setAttribute('src', url);
            img[0].setAttribute('class', 'cli-cat' + $(li).find('.dataChannelId').text());
        }
    }
}

function setOnLoad (img, i, j, li) {
    img.onload = function () {
        aa[i][j] = true;
        if (++aaCpt[i] == aa[i].length) { // All images of li loaded
            $(li).removeClass('loading').click(function(){
                // Add click handler
                if ($(this).is('li.tvIndex.active'))
                    return;

                $('li.tvIndex.active').removeClass('active');
                $(this).addClass('active');

                zapChannel($(li).find('.dataChannelId').text(), $(li).find('.dataChannelName').text());
            });

            if (++nbLiActive == aa.length) { // All images of all li loaded
                // FIRE DEMO (or not ?)
                // Stop demo mode on hover
                $('#tvIndex').hover(
                    function () {
                        clearInterval(demoInterval);
                        $('#tvIndex').hover(function(){});
                });

                // Start démo, channel blinking
                var blinkIndex = -1, nbLoop = 0, tempo = 100;
                demoInterval = setInterval(function() {
                    if (++blinkIndex == $('li.tvIndex').length) {
                        if(++nbLoop == 3)
                            clearInterval(demoInterval);
                        blinkIndex = -1;
                    } else {
                        $('li.tvIndex').eq(blinkIndex).addClass('active');
                        clearActive ($('li.tvIndex').eq(blinkIndex), tempo + 5);
                    }
                }, tempo);
            }
        }
    };
}

function clearActive(elem, tempo) {
    setTimeout (function() {
        elem.removeClass('active')
    }, tempo);
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
    textInterval = setInterval(function() {
        if (cnt > 40) {
            clearInterval(textInterval);
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
        text = text.substring(0, 12) + '-';

    var lcd = $('#tvLcd');
    var channelNb = $('<p class="channelNb">' + nb + '</p>');
    var channelName = $('<p class="channelName">' + text + '</p>');

    $(lcd).empty();
    $(channelNb).appendTo(lcd);
    $(channelName).appendTo(lcd);


//    var cnt = 0;
//    textInterval = setInterval(function() {
//        if (cnt > 40) {
//            clearInterval(textInterval);
//            return;
//        }
//
//        cnt++;
//        lcdContext.clearRect(0, 0, lcdScreen.width, lcdScreen.height);
//        lcdContext.font = "36px digital";
//        lcdContext.fillText(nb, 70, 28);
//        lcdContext.font = "14px digital";
//        lcdContext.fillText(text, 2, 49);
//    }, 50);
}

function zapChannel(nb, nom)
{
    clearInterval(textInterval);
    clearInterval(logoInterval);
    digitalDisplay(nb, nom);
    drawLogos(nb);
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
    if($('#tvScreen.zap').length == 0)
        $('#tvScreen').addClass('zap');

    // Clear tv Screen
    $('#tvScreen').empty();

    var yOffset = 15;
    var i = 0;

    for (var l = 0; l < nbLig; l++) {
        yOffset += gapLig;
        var xOffset = 15;
        for (var c = 0; c < nbCol; c++) {
            xOffset += gapCol;

            if (i == nbImages)
                break;

            var logo = $(images[i]).clone();

            var logoTitle = $(logo).attr('title');
            var split = logoTitle.split("#- -#");
            var cliName = split[0];
            var clientID = split[1];

            $(logo).attr('alt', "logo " + cliName);
            $(logo).attr('title', cliName);
            // While we're holding the actual img for sure, set size
            $(logo).attr('style',
                         'width:'  + (ratio * images[i].naturalWidth) + 'px;' +
                         'height:' + (ratio * images[i].naturalHeight) + 'px;');

            var uri = $('#dataURI' + clientID);

            if ($(uri).length == 1) {
                var a = $('<a href="' + $(uri).text() + '"></a>');
                $(logo).appendTo(a);
                logo = a;
            }

            $(logo).attr('title', cliName);

            // Get current style, set above, and append positionning
            var styleAppend = $(logo).attr('style');
            $(logo).attr('style',
                         'position: absolute; ' +
                         'left:'   + (xOffset + (logoW - ratio*images[i].naturalWidth)/2) + 'px;' +
                         'top:'    + (yOffset + (logoH - ratio*images[i].naturalHeight)/2) + 'px;' +
                         styleAppend);

            $(logo).addClass('drawnLogo');
            $(logo).appendTo('#tvScreen');

//            tvContext.drawImage(images[i],
//                                xOffset + (logoW - ratio*images[i].naturalWidth)/2,
//                                yOffset + (logoH - ratio*images[i].naturalHeight)/2,
//                                ratio * images[i].naturalWidth,
//                                ratio * images[i].naturalHeight);

            i++;

            xOffset += logoW;
        }

        yOffset += logoH;
    }
}