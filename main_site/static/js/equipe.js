/** sound urls **/



$(document).ready(function(){

    $('.bubble').click(function() {
        var i = $(this).attr('id').split('e')[1];

        if($(this).hasClass('focus'))
            return;

        $('#flashSnd')[0].src = '/static/snd/click.mp3';
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
        setTimeout(function(){$('#pb1').removeClass('flash');}, 150);
    });
    $('.bigPhotoOutContainer').click(function(){
        alert('test');
    });
});



function toggleFlash () {
    $('#pb1').toggleClass('flash');
}



function bubbleClick(i) {

}

function enSavoirPlus() {
}