# -*- coding: utf-8 -*-
from Acquisition import aq_base
from zope.cachedescriptors.property import CachedProperty


class ImageContentRenderer(object):
    """Basic renderer for an object with an image.
    """    
    def getSize(self):
        method = getattr(aq_base(self.context), "getImage_scale", None)
        return method is not None and method() or 'thumb'

    @CachedProperty
    def caption(self):
        return self.context.getImageCaption() or self.Rights()
    
    @CachedProperty
    def image(self):
        return self.context.tag(scale=self.getSize())


class TopicCustomRenderer(object):
    """Custom view
    """
    @CachedProperty
    def enabled(self):
        return self.context.getCustomView()
    
    @CachedProperty
    def fields(self):
        return self.context.getCustomViewFields()

    @CachedProperty
    def metadatas(self):
        return self.context.listMetaDataFields(False)


class EnhancedPhotoalbum(object):
    """A content fetcher that adds javascript
    """
    @CachedProperty
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
