$(document).ready(function(){

    $('#spritesPreload').load(function(){
        $('.smallPhotoOut.preload').removeClass('preload');
    });
    // Backup in case .load is not fired on #spritesPreload
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 200);
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 1000);

    $('.bubble').click(function() {
        if($(this).hasClass('focus'))
            return;

        var i = $(this).attr('id').split('e')[1];

        $('.bubble.focus').removeClass('focus');
        $(this).addClass('focus');

        fluidAnim($('#smallPhoto' + i), $('#desc' + i));

        $('#pb1').addClass('flash');
        setTimeout(function(){$('#pb1').removeClass('flash');}, 400);
    });
});

var nbAnimate = 0;

function fluidAnim (elem, desc) {
    // Avoid scrollbars from popping
    nbAnimate++;
    $('#bodyContainer').css('overflow', 'hidden');

    // Remove previous animated elements
    $('.smallPhotoOut:not(#'+elem.attr('id')+'), .wrapDesc:not(#'+desc.attr('id')+')').stop().animate (
        {opacity: -1 }, 150, 'linear',
        function(){
            $('.smallPhotoOut:not(#'+elem.attr('id')+'), .wrapDesc:not(#'+desc.attr('id')+')').attr('style', '').removeClass('pop');
    });

    setTimeout(function() {
        desc.addClass('pop');
    }, 200);

    var bezier_params = {
        start: {
            x: 402,
            y: 335,
            angle: 45,
            length: 1.2
        },
        end: {
            x:670,
            y:0,
            angle: -100
        }
    };

    elem.animate({
        top: 335
    }, 600, function () {
        // Pass in front of description at the right time
        setTimeout(function(){if (elem.is(':animated')) elem.css('z-index', '99');}, 550);
        elem.animate({
            height: 505,
            width: 95,
            path : new jQuery.path.bezier(bezier_params)
        }, 1000, function() {
            if (--nbAnimate == 0)
                $('#bodyContainer').css('overflow', 'auto');
        });
    });
}
