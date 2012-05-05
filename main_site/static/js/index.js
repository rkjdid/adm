var indexCanvas, indexContext;


$(document).ready(function () {
    indexCanvas = $('#index')[0];
    indexContext = indexCanvas.getContext("2d");
    drawBG();
});


function drawBG()
{
    var bg = new Image();
    bg.src = "http://rk.dyndns-server.com/ateliers.media/resources/img.pdf/homepage.png";

    bg.onload = function(){
        tvContext.drawImage(bg, 0, 0, 40, 40);
    }
}