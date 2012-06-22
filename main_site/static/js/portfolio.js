$(document).ready(function(){

    $('.fiche').click(ficheClick0);


});

function ficheClick0() {
    var i = $(this).attr('id').split('iche')[1];

    if ($('#openBook').hasClass('grow')) {
        // todo: redraw canvases
    }

    //        if($(this).hasClass('focus'))
    //            return;

    //        $('#flashSnd')[0].play();

    //        $('.bubble.focus').removeClass('focus');
    //        $(this).addClass('focus');


    $('#book').addClass('shrink');
    $('#openBook').addClass('grow');

    setTimeout(function() {
        $('#book').addClass('loadFade').removeClass('shrink');
//        $('#openBook').addClass('grow');
    }, 1600);
    //        glassPane(i);

    $('#bodyContainer').click(function() {
        $('#openBook').addClass('fadeOut');
        $('#book').addClass('fadeIn');

        setTimeout(function() {
//            $('#book').removeClass('fadeIn loadFade');
            $('#openBook').removeClass('grow fadeOut');
        }, 500);
    });


    $('#openBook').click(function() {return false;});

    return false;

    //        setTimeout(function(){
    //            $('.smallPhotoOut.print.out').removeClass('print out').addClass('hidden');
    //            setTimeout(function(){$('.smallPhotoOut.hidden').removeClass('hidden');}, 1000);
    //        },1200);
}

function glassPane (i) {
    $('#glassPane').addClass('fadeIn');
    $('#bookVierge' + i).addClass('grow');

    $('#glassPane').click(function () {
        // close popup + fadeout
        $('#glassPane').removeClass('fadeIn');
        $('#knowMore' + i).removeClass('grow');
        $('#book').removeClass('shrink');

        $('#glassPane').click(function(){}); // reset glassPane click handler
    });

}