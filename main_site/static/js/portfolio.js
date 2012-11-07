var startEventHandle;
var bookHandles = new Array(6);

$(document).ready(function(){
    // Get page indexes
    for (var i = 1; i <= 6; i++) {
        bookHandles[i-1] = $('#bookHandle'+i).html();
    }

    // URIs
    Hash.on('^page\/([0-9]*|design|photo|web|com|marketo|marketd)$', {
        yep: function(path, parts) {
            var page = parts[1];

            switch(page) {
                case 'design':
                    page = bookHandles[0];
                    break;
                case 'photo':
                    page = bookHandles[1];
                    break;
                case 'web':
                    page = bookHandles[2];
                    break;
                case 'com':
                    page = bookHandles[3];
                    break;
                case 'marketo':
                    page = bookHandles[4];
                    break;
                case 'marketd':
                    page = bookHandles[5];
                    break;
            }

            if (page !== undefined) {
                $('#flipbook').turn('page', page);
                // Gets the range of pages that the book needs right now
                var range = $('#flipbook').turn('range', page);

                // Check if each page is within the book
                for (var p = range[0]; p<=range[1]; p++)
                    populatePage(p, $('#flipbook'));
            }
        },
        nop: function(path) {
        }
    });

    // Arrow keys
    $(window).bind('keydown', function(e){
        if (e.target && e.target.tagName.toLowerCase()!='input')
            if (e.keyCode==37)
                $('#flipbook').turn('previous');
            else if (e.keyCode==39)
                $('#flipbook').turn('next');
    });
});

function populatePage(page, book) {
    // 	Check if the page is already filled in
    if ($('#page-'+page+ ' .loader').length) {
        var data = $('#page-'+page+ ' .data');
        Dajaxice.main_site.getImage
            (Dajax.process,
             {
                 'selector' : 'page-' + data.find('.dataSelector').html(),
                 'book'     : data.find('.dataBook').html(),
                 'page'     : data.find('.dataPage').html(),
                 'bEven'    : data.find('.dataEven').html()=='true'
             }
        );
    }
}

function loadBook() {
    // FlipBook (flip.js)
    $("#flipbook").turn({
        acceleration: true,
        elevation: 50,
        gradients: true,
        when: {
            turning: function(e, page, view) {
                // Disable scrollbars during animation
                $('#bodyContainer').css('overflow', 'hidden');

                /* Book alignment */
                if(page == $(this).turn('pages'))
                    $(this).removeClass('first').addClass('last');
                else if (page > 1)
                    $(this).removeClass('first last');
                else if (page == 1)
                        $(this).removeClass('last').addClass('first');


                $('#navBook li').removeClass('active');
                if        (page > 3 && page < bookHandles[1]) {
                    $('#liDesign').addClass('active');
                } else if (page >= bookHandles[1] && page < bookHandles[2]) {
                    $('#liPhoto').addClass('active');
                } else if (page >= bookHandles[2] && page < bookHandles[3]) {
                    $('#liWeb').addClass('active');
                } else if (page >= bookHandles[3] && page < bookHandles[4]) {
                    $('#liCom').addClass('active');
                } else if (page >= bookHandles[4] && page < bookHandles[5]) {
                    $('#liMarketo').addClass('active');
                } else if (page >= bookHandles[5] && page < $('#flipbook').turn('pages') - 2) {
                    $('#liMarketd').addClass('active');
                }

                window.location = '#page/' + page;
            },

            turned: function(e, page) {
            },

            start: function(e, pageObject, corner) {
                // Disable scrollbars during animation
                $('#bodyContainer').css('overflow', 'hidden');

                // Gets the range of pages that the book needs right now
                var range = $(this).turn('range', pageObject.page);

                // Check if each page is within the book
                for (var p = range[0]; p<=range[1]; p++)
                    populatePage(p, $(this));

                // trickshot
                startEventHandle = e;
            },
            end: function(event, pageObject, turned) {
                // Enable scrollbars after animation --trickshot
                if (startEventHandle == null)
                    $('#bodyContainer').css('overflow', 'auto');
                else {
                    setTimeout(function() {
                        if (!$('#flipbook').turn('animating'))
                            $('#bodyContainer').css('overflow', 'auto');
                    }, 200);
                }
                startEventHandle = null;
            }
        }
    });
}
