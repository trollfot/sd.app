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
    def image(self):
        return self.context.tag(scale=self.getSize())
