# -*- coding: utf-8 -*-

import sd.rendering
from five import grok
from sd.rendering import base
from Acquisition import aq_base
from zope.cachedescriptors.property import CachedProperty
from Products.ATContentTypes import interface as atct


grok.templatedir('browser/templates')


class ATDocument(sd.rendering.StructuredRenderer):
    """A simple document rendering.
    """
    sd.rendering.target(atct.IATDocument)


class ImageContentRenderer(sd.rendering.StructuredRenderer):
    """Basic renderer for an object with an image.
    """
    sd.rendering.target(atct.IImageContent)
    
    def getSize(self):
        method = getattr(aq_base(self.context), "getImage_scale", None)
        return method is not None and method() or 'thumb'

    @CachedProperty
    def caption(self):
        return self.context.getImageCaption() or self.context.Rights()
    
    @CachedProperty
    def image(self):
        return self.context.tag(scale=self.getSize())


class PhotoAlbum(sd.rendering.FolderishRenderer):
    """A photoalbum.
    """
    sd.rendering.name(u"sd_photoalbum")
    sd.rendering.target(atct.IATFolder)
    sd.rendering.target(atct.IATBTreeFolder)
    sd.rendering.target(atct.IATTopic)
    sd.rendering.restrict(atct.IPhotoAlbumAble)
    

class EnhancedPhotoalbum(PhotoAlbum):
    """A content fetcher that adds javascript
    """
    sd.rendering.name(u"sd_enhanced_photoalbum")
        
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


class TopicCustomRenderer(sd.rendering.FolderishRenderer):
    """Custom view
    """
    sd.rendering.name(u"sd_topiccustom")
    sd.rendering.target(atct.IATTopic)
    
    @CachedProperty
    def enabled(self):
        return self.context.getCustomView()
    
    @CachedProperty
    def fields(self):
        return self.context.getCustomViewFields()

    @CachedProperty
    def metadatas(self):
        return self.context.listMetaDataFields(False)


