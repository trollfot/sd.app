# -*- coding: utf-8 -*-

from zope.interface import implements
from Products.ATContentTypes.content import document, newsitem, image
from Products.ATContentTypes.interface.image import IPhotoAlbumAble

from sd.app.contents import PROJECTNAME
from interfaces import ISimpleParagraph
from image_content import *


class SimpleParagraph(document.ATDocumentBase, image.ATCTImageTransform):
    """A very simple paragraph inside a chapter
    """
    implements(ISimpleParagraph, IPhotoAlbumAble)

    # Preferences
    sd_layout = u"default"
    show_title = True
    show_description = True

    ## Schema customization
    schema = newsitem.ATNewsItemSchema.copy() + tagselector
    schema['image'].original_size = ORIGINAL_SIZE
    schema['image'].sizes = TAG_SIZES


    def tag(self, **kwargs):
        """Generates an image tag using the api of the ImageField.
        We use it here to provide a convenient way to display
        thumbnail and also to fit the summary_view requirement
        """
        if self.getImage():
            if not 'scale' in kwargs:
                kwargs['scale'] = self.getImage_scale() or 'normal'
            return self.getWrappedField('image').tag(self, **kwargs)

        return None


    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return document.ATDocumentBase.__bobo_traverse__(self, REQUEST, name)


# Registers the type
from Products.Archetypes.public import registerType
registerType(SimpleParagraph, PROJECTNAME)

