var indexCanvas, indexContext;


$(document).ready(function () {
    var rdm = 0;
    var nbPhotos = $('.smallPhotoOut').length;

    var pauseAnimMap = {
        '-webkit-animation-play-state' : 'paused',
        '-moz-animation-play-state' : 'paused',
        '-ms-animation-play-state' : 'paused',
        'animation-play-state' : 'paused'};

    var bclientTimerHandle;

    $('#bclients').hover(
        function(){
            var noTimer = false;

            if (!$('#flamand').is(':animated')) {
                $('#buisson').addClass("shake");
                noTimer = true;
            }


            // Dummy timer to check if flam has started moving (delay .5s)
            if (noTimer)
                bclientTimerHandle = setTimeout(function (){bclientTimerHandle = null;}, 650);

            $('#flamand').stop().removeAttr("style").removeClass('flampop').addClass("flampop");
            if (!jQuery.browser.msie)
                $('#uh').addClass("what");
        },
        function(){
            $('#buisson').removeClass("shake");
            $('#uh').removeClass("what");

            if (bclientTimerHandle) {
                clearTimeout(bclientTimerHandle);
                $('#flamand').removeAttr("style").removeClass('flampop');
            } else {
                $('#flamand').css(pauseAnimMap).animate(
                    {bottom: '-20'},
                    500,
                    function () {$('#flamand').removeAttr("style").removeClass('flampop');}
                );
            }
        }
    );

    $('#bagence').hover(
        function(){
            $("#copyright").addClass("twist");
            setTimeout(function(){
                $("#copyright").removeClass("twist");
            }, 1000);
        },
        function() {
            $("#copyright").removeClass("twist");
        }
    );

    var timeOutHandle;
    $('#bportfolio').hover(
        function(){
            $('#cupcake1').addClass("hidden");
            timeOutHandle = setTimeout(function(){$('#cupcake2').addClass('hidden');}, 900);
        },
        function() {
            clearTimeout(timeOutHandle);
            $('#cupcake1').removeClass("hidden");
            $('#cupcake2').removeClass("hidden");
        }
    );

    $('#bcontact').hover(
        function(){
            $('#cupcopy').addClass("copypop");
        },
        function() {
            $('#cupcopy').removeClass("copypop");
        }
    );

    $('#photoPreload').load(function() {$('.smallPhotoOut.preload').removeClass('preload');});

    $('#bequipe').hover(
        function(){
            var newRdm = Math.ceil(Math.random()* nbPhotos);
            if (nbPhotos >= 2) {
                while(newRdm == rdm) {
                    newRdm = Math.ceil(Math.random()* $('.smallPhotoOut').length);
                }
            }

            $('#pb1').addClass('flash');
            setTimeout(function(){$('#pb1').removeClass('flash');}, 400);

            if (timeOutHandle) {
                clearTimeout(timeOutHandle);
                timeOutHandle = null;
                $('#smallPhoto' + rdm).attr('style',
                                            "-webkit-transition: none; " +
                                            "-moz-transition:none; " +
                                            "-ms-transition:none; " +
                                            "-o-transition:none; transition:none;")
                                      .removeClass('print out');
            }

            $('#smallPhoto' + newRdm).removeAttr('style').addClass('print');

            rdm = newRdm;
        },
        function() {
            $('#smallPhoto' + rdm).addClass('out');
            timeOutHandle = setTimeout(function(){$('#smallPhoto' + rdm).attr('style',
                                           "-webkit-transition: none; " +
                                           "-moz-transition:none; " +
                                           "-ms-transition:none; " +
                                           "-o-transition:none; transition:none;")
                                      .removeClass('print out');}, 700);
        }
    );
});
