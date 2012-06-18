$(document).ready(function(){

    $('.bubble').click(function() {
        // C'est laid et ça peut bugger -- todo
        var i = $(this).attr('id').split('e')[1];

        if($(this).hasClass('focus'))
            return;

        $('#flashSnd')[0].play();

        $('.bubble.focus').removeClass('focus');
        $(this).addClass('focus');


        $('.bigPhotoOutContainer.pop').removeClass('pop');
        $('#bigPhotoContainer' + i).addClass('pop');

        $('#smallPhoto' + i).removeClass('hidden');
        $('.smallPhotoOut.print').addClass('out');
        setTimeout(function(){
            $('.smallPhotoOut.print.out').removeClass('print out').addClass('hidden');
            setTimeout(function(){$('.smallPhotoOut.hidden').removeClass('hidden');}, 1000);
        },1200);

        $('#smallPhoto' + i).addClass('print');

        $('#pb1').addClass('flash');
        setTimeout(function(){$('#pb1').removeClass('flash');}, 400);
    });


    $('.bigPhotoOutContainer').click(function(){
        var i = $(this).attr('id').split('Container')[1];
        glassPane(i);
    });
});

function glassPane (i) {
    $('#glassPane').addClass('fadeIn');
    $('#knowMore' + i).addClass('pop');

    $('#glassPane').click(function () {
        // close popup + fadeout
        $('#glassPane').removeClass('fadeIn');
        $('#knowMore' + i).removeClass('pop');

        $('#glassPane').click(function(){}); // reset glassPane click handler
    });

}


function toggleFlash () {
    $('#pb1').toggleClass('flash');
}



function bubbleClick(i) {

}

function enSavoirPlus() {
}