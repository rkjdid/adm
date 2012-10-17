$(document).ready(function(){

    $('#spritesPreload').load(function(){
        $('.smallPhotoOut.preload').removeClass('preload');
    });

    // Backup in case .load is not fired on #spritesPreload
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 700);

    $('.bubble').click(function() {
        if($(this).hasClass('focus'))
            return;

        var i = $(this).attr('id').split('e')[1];

        $('.bubble.focus').removeClass('focus');
        $(this).addClass('focus');



        // Remove previous active member
        var disappearHandle = $('.smallPhotoOut.print').addClass('fade');
        setTimeout(function() {disappearHandle.removeClass('print fade');}, 200);

        $('#smallPhoto' + i).addClass('print');

        $('#pb1').addClass('flash');
        setTimeout(function(){$('#pb1').removeClass('flash');}, 400);
    });
});
