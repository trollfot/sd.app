# -*- coding: utf-8 -*-

class ImageContentRenderer(object):
    """Basic renderer for an object with an image.
    """    
    @property
    def image(self):
        return self.context.tag(scale='thumb')
