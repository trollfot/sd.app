# -*- coding: utf-8 -*-

from five import grok
from zope.component import queryMultiAdapter
from zope.cachedescriptors.property import CachedProperty
from sd.rendering.interfaces import IStructuredView, IRendererResolver
from sd.contents.interfaces import IStructuredItem

grok.templatedir('browser/templates')


class StructuredContentProvider(grok.ViewletManager):
    """A content provider serving the contents.
    """
    grok.name("sd.contents")
    grok.require('zope2.View')
    grok.view(IStructuredView)
    grok.context(IStructuredItem)

    @CachedProperty
    def renderers(self):
        return [queryMultiAdapter((content, self.request),
                                  IRendererResolver).renderer
                for content in self.view.contents(full_objects=True)]
