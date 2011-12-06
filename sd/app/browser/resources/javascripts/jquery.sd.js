/**
*** When KSS is not enough...
**/

(function($) {

    $(document).ready(function(){

        $('body').intercept('click', {
            'a.action-header, a.action-header small': function(event){
                var $parent = $(this).parent();
                $("ul.submenu", $parent).addClass('clicked').toggle();
                $("ul.submenu:visible").not('.clicked').hide();
                $("ul.submenu").removeClass('clicked');
                event.preventDefault();
            }
        });

        $('body').intercept('click', {
            'li.layout a': function(e){
                $("ul.submenu").hide();
                e.preventDefault();
            }
        });

        $('.portlet-photoalbum').each(function() {
            var $portlet = $(this);
            var $slideshow = $portlet.find('.slideshow');
            var $start = $portlet.find('.start');
            var $stop = $portlet.find('.stop');

            $slideshow.cycle({
                fx:     'fade',
                speed:  'fast',
                timeout: +$slideshow.attr('data-slideshow-timeout'),
                next:   $portlet.find('.next'),
                prev:   $portlet.find('.prev')
            });
            $start.bind('click', function(event) {
                $slideshow.cycle('resume');
                $portlet.removeClass('stopped');
                event.preventDefault();
            });
            $stop.bind('click', function(event) {
                $slideshow.cycle('pause');
                $portlet.addClass('stopped');
                event.preventDefault();
            });

        });

        $.fn.cycle.updateActivePagerLink = function(pager, currSlideIndex) {
            $(pager).find('li').removeClass('activeSlide').fadeTo('fast',0.3)
                .filter('li:eq('+currSlideIndex+')').addClass('activeSlide').fadeTo('fast', 1);
        };

    });
})(jQuery);

