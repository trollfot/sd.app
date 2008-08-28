# -*- coding: utf-8 -*-

class TopicCustomRenderer(object):
    """Custom view
    """
    @property
    def enabled(self):
        return self.context.getCustomView()
    
    @property
    def fields(self):
        return self.context.getCustomViewFields()

    @property
    def metadatas(self):
        return self.context.listMetaDataFields(False)


class EnhancedPhotoalbum(object):
    """A content fetcher that adds javascript
    """
    @property
    def timer(self):
        conf = self.configuration
        return conf and conf.timer * 1000 or 0
    
    def javascript(self):
        return """
        jq('#gallery-%(uid)s .main_image').cycle({ 
        fx: 'fade', 
        timeout: %(timer)s,
        height: 400,
        width: 400,
        pager:  '#gallery-%(uid)s .nav', 
        pagerAnchorBuilder: function(idx, slide) {
          return '#gallery-%(uid)s .nav li:eq(' + idx + ') a';
        },
        updateActivePagerLink : function(pager, currSlideIndex) { 
            jq(pager).find('li.activeSlide').removeClass('activeSlide')
              .fadeTo('fast',0.3)
              .filter('li:eq('+currSlideIndex+')')
              .addClass('activeSlide').fadeTo('fast', 1);
        }
        })
        """ % {"uid" : self.UID(),
               "timer": self.timer }
