# -*- coding: utf-8 -*-

from zope.interface import Interface
from sd.contents.interfaces import IDynamicStructuredItem
from Products.ATContentTypes.interface.image import IImageContent


class ITextContent(Interface):
    """Defines a content that have textual data.
    """
    def getText(self):
        """Return the body text as a string or unicode string.
        """

class ITextWithImage(ITextContent, IImageContent):
    """Defines a content that have textual content as well as an image.
    """

class ISimpleParagraph(ITextWithImage, IDynamicStructuredItem):
    """Marker interface
    """
