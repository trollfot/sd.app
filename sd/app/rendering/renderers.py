# -*- coding: utf-8 -*-

import sd.rendering
from five import grok
from Acquisition import aq_base
from zope.i18nmessageid import MessageFactory
from zope.cachedescriptors.property import CachedProperty
from sd.app.contents import interfaces as sdct
from Products.ATContentTypes import interface as atct

grok.templatedir('templates')
_ = MessageFactory("sd")


class Document(sd.rendering.StructuredRenderer):
    sd.rendering.target(sdct.ITextContent)

    label = _("sd_document",
              default=u"Document rendering.")
    
    def render(self):
        return self.context.getText()


class ATFile(sd.rendering.StructuredRenderer):
    sd.rendering.target(atct.IATFile)

    label = _("sd_atfile",
              default=u"Classical file rendering.")
    

class ATLink(sd.rendering.StructuredRenderer):
    sd.rendering.target(atct.IATLink)
    
    label = _("sd_atlink",
              default=u"Classical link rendering.")
    
    
class ATEvent(sd.rendering.StructuredRenderer):
    sd.rendering.target(atct.IATEvent)

    label = _("sd_atevent",
              default=u"Classical event rendering.")
    

class Image(sd.rendering.StructuredRenderer):
    sd.rendering.target(atct.IATImage)

    label = _("sd_image",
              default=u"Centered image.")

    @CachedProperty
    def image(self):
        return self.context.tag(scale="preview")


class ImageContent(sd.rendering.StructuredRenderer):
    sd.rendering.target(sdct.ITextWithImage)

    label = _("sd_imagecontent_center",
              default=u"Centered image above text.")    
    
    def getSize(self):
        scale = getattr(aq_base(self.context), "getImage_scale", None)
        return scale is not None and scale() or 'thumb'

    @CachedProperty
    def caption(self):
        caption = getattr(aq_base(self.context), "getImageCaption", None)
        return caption is not None and caption() or self.context.Rights()
    
    @CachedProperty
    def image(self):
        return self.context.tag(scale=self.getSize())


class ImageContentLeft(ImageContent):
    sd.rendering.name(u"imagecontent_left")

    label = _("imagecontent_left",
              default=u"Text with an image on the left.")


class ImageContentRight(ImageContent):
    sd.rendering.name(u"sd_imagecontent_right")

    label = _("imagecontent_right",
              default=u"Text with an image on the right.")


class FolderListing(sd.rendering.FolderishRenderer):
    sd.rendering.target(atct.IATFolder)
    sd.rendering.target(atct.IATBTreeFolder)
    sd.rendering.target(atct.IATTopic)

    label = _("sd_folderlisting",
              default=u"Listing of the content.")


class FolderAsChapter(sd.rendering.FolderishRenderer):
    sd.rendering.name(u"sd_chapter")
    sd.rendering.target(atct.IATFolder)
    sd.rendering.target(atct.IATBTreeFolder)
    sd.rendering.target(atct.IATTopic)

    label = _("chapter",
              default=u"Contents as standalone items.")


class PhotoAlbum(FolderAsChapter):
    sd.rendering.name(u"sd_photoalbum")
    sd.rendering.restrict(atct.IImageContent)

    label = _("photoalbum",
              default=u"Photo album with thumbnails.")


class EnhancedPhotoalbum(PhotoAlbum):
    sd.rendering.name(u"sd_enhanced_photoalbum")

    label = _("enhanced_photoalbum",
              default=u"Photo album with slideshow options and javascript.")
        
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
    sd.rendering.name(u"sd_topiccustom")
    sd.rendering.target(atct.IATTopic)

    label = _("topiccustom",
              default=u"Custom view (if defined).")
    
    @CachedProperty
    def enabled(self):
        return self.context.getCustomView()
    
    @CachedProperty
    def fields(self):
        return self.context.getCustomViewFields()

    @CachedProperty
    def metadatas(self):
        return self.context.listMetaDataFields(False)
