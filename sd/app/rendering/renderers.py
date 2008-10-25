# -*- coding: utf-8 -*-

import sd.rendering
from five import grok
from Acquisition import aq_base
from zope.i18nmessageid import MessageFactory
from zope.cachedescriptors.property import CachedProperty
from sd.rendering import base
from sd.rendering.interfaces import IStructuredDefaultRenderer
from Products.ATContentTypes import interface as atct


grok.templatedir('templates')
_ = MessageFactory("sd")


class ATDocument(sd.rendering.StructuredRenderer):

    label = _("sd_atdocument",
              default=u"A simple document rendering.")
    
    sd.rendering.target(atct.IATDocument)

    def render(self):
        return self.context.getText()



class ATFile(sd.rendering.StructuredRenderer):

    label = _("sd_atfile",
              default=u"A simple file rendering.")
    
    sd.rendering.target(atct.IATFile)



class ATLink(sd.rendering.StructuredRenderer):

    label = _("sd_atlink",
              default=u"A simple link rendering.")
    
    sd.rendering.target(atct.IATLink)



class ATEvent(sd.rendering.StructuredRenderer):

    label = _("sd_atevent",
              default=u"Event rendering.")
    
    sd.rendering.target(atct.IATEvent)



class ImageContent(sd.rendering.StructuredRenderer):

    label = _("sd_imagecontent_center",
              default=u"Centered image above text.")

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


class ImageContentLeft(ImageContent):
    """Text with an image on the left.
    """
    sd.rendering.name(u"sd_imagecontent_left")


class ImageContentRight(ImageContent):
    """Text with an image on the right.
    """
    sd.rendering.name(u"sd_imagecontent_right")


class FolderListing(sd.rendering.FolderishRenderer):

    label = _("sd_folderlisting",
              default=u"A listing of the content.")

    sd.rendering.target(atct.IATFolder)
    sd.rendering.target(atct.IATBTreeFolder)
    sd.rendering.target(atct.IATTopic)


class PhotoAlbum(sd.rendering.FolderishRenderer):
    """A simple photo album.
    """
    sd.rendering.name(u"sd_photoalbum")
    sd.rendering.restrict(atct.IPhotoAlbumAble)
    sd.rendering.target(atct.IATFolder)
    sd.rendering.target(atct.IATBTreeFolder)
    sd.rendering.target(atct.IATTopic)


class EnhancedPhotoalbum(PhotoAlbum):
    """A photo album with slideshow options and javascript.
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


class TopicCustomView(sd.rendering.FolderishRenderer):
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


