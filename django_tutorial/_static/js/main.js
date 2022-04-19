(function ($) {
    $.fn.scrollingTo = function (opts) {
        var defaults = {
            animationTime: 1000,
            easing: '',
            callbackBeforeTransition: function () { },
            callbackAfterTransition: function () { }
        };

        var config = $.extend({}, defaults, opts);

        $(this).click(function (e) {
            var eventVal = e;
            e.preventDefault();

            var $section = $(document).find($(this).data('section'));
            if ($section.length < 1) {
                return false;
            };

            if ($('html, body').is(':animated')) {
                $('html, body').stop(true, true);
            };

            var scrollPos = $section.offset().top;

            if ($(window).scrollTop() == scrollPos) {
                return false;
            };

            config.callbackBeforeTransition(eventVal, $section);

            $('html, body').animate({
                'scrollTop': (scrollPos + 'px')
            }, config.animationTime, config.easing, function () {
                config.callbackAfterTransition(eventVal, $section);
            });
        });
    };
}(jQuery));



jQuery(document).ready(function () {
    "use strict";
    new WOW().init();


    (function () {
        jQuery('.smooth-scroll').scrollingTo();
    }());

});




$(document).ready(function () {




    $(window).scroll(function () {
        if ($(window).scrollTop() > 50) {
            $(".navbar-brand a").css("color", "#fff");
            $("#top-bar").removeClass("animated-header");
        } else {
            $(".navbar-brand a").css("color", "inherit");
            $("#top-bar").addClass("animated-header");
        }
    });

    $("#clients-logo").owlCarousel({

        itemsCustom: false,
        pagination: false,
        items: 5,
        autoplay: true,

    })

});



// fancybox
$(".fancybox").fancybox({
    padding: 0,

    openEffect: 'elastic',
    openSpeed: 450,

    closeEffect: 'elastic',
    closeSpeed: 350,

    closeClick: true,
    helpers: {
        title: {
            type: 'inside'
        },
        overlay: {
            css: {
                'background': 'rgba(0,0,0,0.8)'
            }
        }
    }
});

// (.navbar높이 + .container높이(#content) + footer높이) >= 뷰포트 높이보다 크면
// footer태그의 .fixed-bottom 를 삭제함.
let nav_h = document.querySelector('header').clientHeight;
let con_h = document.querySelector('section').clientHeight;
let footer_h = document.querySelector('footer').clientHeight;
console.log(nav_h, con_h, footer_h)
console.log(window.innerHeight)
doc_h = nav_h + con_h + footer_h
if (doc_h >= window.innerHeight) {
    document.querySelector('footer').classList.remove('fixed-bottom')
}









