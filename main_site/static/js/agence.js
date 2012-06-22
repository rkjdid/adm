$(document).ready(function(){
    $('#secteurs').click(function(){
        glassPane2('#popSecteurs');
    });

    $('#integre').click(function(){
        glassPane2('#popIntegre');
    });

    $('#poles').click(function(){
        glassPane2('#popPole');
    });
});

function glassPane2 (pop) {
    $('#glassPane').addClass('fadeIn');
    $(pop).addClass('pop');
    $('#glassPane').click(function () {
        // close popup + fadeout
        $('#glassPane').removeClass('fadeIn');
        $(pop).removeClass('pop');

        $('#glassPane').click(function(){}); // reset glassPane click handler
    });
}