var timeOutHandle;
var rdm = 0;
var nbPhotos = $('.smallPhotoOut').length;

var pauseAnimMap = {
    '-webkit-animation-play-state' : 'paused',
    '-moz-animation-play-state' : 'paused',
    '-ms-animation-play-state' : 'paused',
    'animation-play-state' : 'paused'};

var bclientTimerHandle;

$(document).ready(function () {
    // z-rotation fix
    $('#copyTurn, #copyright').click(function () {
        window.location = '/agence/';
    });

    // Just to be sure... load photobooth pictures
    $('#photoPreload').load(function() {$('.smallPhotoOut.preload').removeClass('preload');});
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 200);
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 600);
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 1200);
    setTimeout (function () {$('.smallPhotoOut.preload').removeClass('preload');}, 3000);

    // Bind animations
    $('.bclients, #client').hover(
        function(){bclientAnimIn();},
        function(){bclientAnimOut();}
    );

    $('.bagence, #copyright').hover(
        function(){bagenceAnimIn();},
        function() {bagenceAnimOut();}
    );


    $('.bportfolio, #cupcake').hover(
        function(){bportfolioAnimIn();},
        function() {bportfolioAnimOut();}
    );

    $('.bcontact, #mug').hover(
        function(){bcontactAnimIn();},
        function() {bcontactAnimOut();}
    );

    $('.bequipe, #pbox').hover(
        function(){bequipAnimIn();},
        function() {bequipAnimOut();}
    );

    // Trigger animations, for fun, when page loaded
    $(window).load(function () {
        setTimeout(function(){bequipAnimIn();}, 400);
        setTimeout(function(){bequipAnimOut();}, 1200);

        setTimeout(function(){bportfolioAnimIn();}, 1400);
        setTimeout(function(){bportfolioAnimOut();}, 4500);

        setTimeout(function(){bcontactAnimIn();}, 1200);
        setTimeout(function(){bcontactAnimOut();}, 4400);

        setTimeout(function(){bclientAnimIn();}, 1600);
        setTimeout(function(){bclientAnimOut();}, 3400);

        setTimeout(function(){bagenceAnimIn();}, 2600);
        setTimeout(function(){bagenceAnimOut();}, 4400);
    });
});



//******* HOVER ANIMATIONS **********//
function bclientAnimIn() {
    if (jQuery.browser.msie)
        return;

    var noTimer = false;

    if (!$('#flamand').is(':animated')) {
        $('#buisson').addClass("shake");
        noTimer = true;
    }

    // Dummy timer to check if flam has started moving (delay .5s)
    if (noTimer)
        bclientTimerHandle = setTimeout(function (){bclientTimerHandle = null;}, 650);

    $('#flamand').stop().removeAttr("style").removeClass('flampop').addClass("flampop");
    $('#uh').addClass("what");
}

function bclientAnimOut() {
    if (jQuery.browser.msie)
        return;

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

function bagenceAnimIn() {
    $("#copyTurn").addClass("twist");
    setTimeout(function(){
        $("#copyTurn").removeClass("twist");
    }, 1000);
}

function bagenceAnimOut() {
    $("#copyTurn").removeClass("twist");
}

function bportfolioAnimIn() {
    $('#cupcake1').addClass("hidden");
    timeOutHandle = setTimeout(function(){$('#cupcake2').addClass('hidden');}, 900);
}

function bportfolioAnimOut() {
    clearTimeout(timeOutHandle);
    $('#cupcake1').removeClass("hidden");
    $('#cupcake2').removeClass("hidden");
}

function bcontactAnimIn() {
    $('#cupcopy').addClass("copypop");
}

function bcontactAnimOut() {
    $('#cupcopy').removeClass("copypop");
}

function bequipAnimIn() {
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
}

function bequipAnimOut() {
    $('#smallPhoto' + rdm).addClass('out');
    timeOutHandle =
        setTimeout(
            function(){
                $('#smallPhoto' + rdm).attr('style',
                                            "-webkit-transition: none; " +
                                              "-moz-transition:none; " +
                                              "-ms-transition:none; " +
                                              "-o-transition:none; transition:none;")
                                      .removeClass('print out');
            }, 700);
}
