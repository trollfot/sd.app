# -*- coding: utf-8 -*-

from five import grok
from zope.component import queryMultiAdapter
from zope.cachedescriptors.property import CachedProperty

from sd.contents.interfaces import IStructuredItem, IDynamicStructuredItem
from sd.rendering.interfaces import IStructuredView, IStructuredRenderer

grok.templatedir('browser/templates')


class StructuredContentProvider(grok.ViewletManager):
    """A content provider serving.
    """
    grok.name("sd.contents")
    grok.view(IStructuredView)
    grok.context(IStructuredItem)
    grok.require('zope2.View')
    
    @CachedProperty
    def renderers(self):
        renderers = list()
        for content in self.view.contents(full_objects=True):
            name = IDynamicStructuredItem(content).sd_layout
            renderer = queryMultiAdapter((content, self.request),
                                         IStructuredRenderer,
                                         name = name)
            if renderer:
                renderers.append(renderer)
        return renderers
