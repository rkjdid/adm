var indexCanvas, indexContext;


$(document).ready(function () {
    var rdm = 0;
    var nbPhotos = $('.smallPhotoOut').length;

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

    // todo: almost mais à travailler
    $('#bequipe').hover(
        function(){
            var newRdm = Math.ceil(Math.random()* nbPhotos) - 1;
            if (nbPhotos >= 2)
                while(newRdm == rdm)
                    newRdm = Math.ceil(Math.random()* $('.smallPhotoOut').length);

            rdm = newRdm;

            $('#smallPhoto' + rdm).removeClass('hidden').addClass('print');

            $('#pb1').addClass('flash');
            setTimeout(function(){$('#pb1').removeClass('flash');}, 400);
        },
        function() {
            $('.smallPhotoOut.print.out').removeClass('print out').addClass('hidden');
            $('.smallPhotoOut.print').addClass('out');
            setTimeout(function(){$('.smallPhotoOut.hidden').removeClass('hidden print out');}, 1000);
        }
    );
});
