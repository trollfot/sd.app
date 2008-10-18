/**
*** When KSS is not enough...
**/


jq(document).ready(function(){ 

jq('body').intercept('click', {
  'a.action-header, a.action-header small': function(e){
    var parent = jq(this).parent();
    jq("ul.submenu", parent).addClass('clicked').toggle()
    jq("ul.submenu:visible").not('.clicked').hide();
    jq("ul.submenu").removeClass('clicked');
    e.preventDefault();
  }
});

jq('body').intercept('click', {
  'li.layout a': function(e){
    jq("ul.submenu").hide();
    e.preventDefault();
  }
});

jq.fn.cycle.updateActivePagerLink = function(pager, currSlideIndex) { 
    jq(pager).find('li').removeClass('activeSlide').fadeTo('fast',0.3)
        .filter('li:eq('+currSlideIndex+')').addClass('activeSlide').fadeTo('fast', 1);
}; 

})


