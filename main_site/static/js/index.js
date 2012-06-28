var indexCanvas, indexContext;


$(document).ready(function () {
//    $('#rFiller')[0].left = $('#indexbg')[0].lef
//    indexCanvas = $('#index')[0];
//    indexContext = indexCanvas.getContext("2d");
//    drawBG();

    init();
});

function init() {
    $('#bclients').hover(
        function(){

            $('#buisson').addClass("shake");
            $('#flamand').addClass("flampop");
            if (!jQuery.browser.msie)
                $('#uh').addClass("what");
        },
        function(){
            $('#buisson').removeClass("shake");
            $('#uh').removeClass("what");

            $('#flamand').removeClass("flampop");
        }
    );
}


//function animBuisson()
//{
//    $('#buisson')[0].addClass("shake");
//    $('#flamand')[0].addClass("pop");
//}
//
//function animOut()
//{
//    $('#buisson')[0].removeClass("shake");
//    $('#flamand')[0].removeClass("pop");
//}


//function drawBG()
//{
//    var bg = new Image();
//    bg.src = "http://rk.dyndns-server.com/ateliers.media/resources/img.pdf/homepage.png";
//
//    bg.onload = function(){
//        tvContext.drawImage(bg, 0, 0, 40, 40);
//    }
//}