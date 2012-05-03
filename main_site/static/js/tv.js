window.onload = function ()
{
    preloadImages()
}

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

function digitalDisplay(text)
{
    var lcd = document.getElementById("tvLcd");
    var lcdContext = lcd.getContext("2d");

    lcdContext.clearRect(0, 0, lcd.width, lcd.height);
    lcdContext.font = "14px digital";
    lcdContext.fillText(text, 2, 12);

}

function zapChannel(id, nom)
{
    digitalDisplay(nom);
    drawLogos(id);
}

function drawLogos(cat)
{
    var screen = document.getElementById("tvScreen");
    var screenContext = screen.getContext("2d");

//    var step = document.getElementById(cat);
    var images = document.getElementsByClassName('cli-cat' + cat)

    var x = 15;
    var y = -20;
    screenContext.clearRect(0, 0, screen.width, screen.height);
    for (var i = 0; i < images.length; i++)
    {
        screenContext.drawImage(images[i], x, y, 50, 50);
        y += 50;
    }

}




