# -*- coding: utf-8 -*-

from five import grok
from zope.interface import implements
from zope.component import queryMultiAdapter
from zope.cachedescriptors.property import CachedProperty
from sd.contents.interfaces import IStructuredDocument, IStructuredItem
from sd.contents.interfaces import IDynamicStructuredItem
from sd.rendering.interfaces import IStructuredView, IStructuredRenderer
from sd.common.adapters.interfaces import IContentQueryHandler

grok.templatedir('templates')


class DocumentContentProvider(grok.View):
    """Access to a document contents
    """
    grok.require('zope2.View')
    grok.name('sd.document.onepage')
    grok.context(IStructuredDocument)
    grok.implements(IStructuredView)

    @CachedProperty
    def _contents(self):
        contentFilter = {"object_provides":
                         'sd.contents.interfaces.base.IStructuredItem'}
        handler = IContentQueryHandler(self.context)
        brains = handler and handler.query_contents(**contentFilter) or []
        return [brain.getObject() for brain in brains]

    def contents(self, *args, **kwargs):
        return self._contents


class GenericView(grok.View):
    """The AT view of the SimpleParagraph
    """
    grok.name('sd.generic_view')
    grok.context(IStructuredItem)
    grok.require('zope2.View')

    @CachedProperty
    def body(self):
        item = IDynamicStructuredItem(self.context)
        renderer = queryMultiAdapter((self.context, self.request),
                                     IStructuredRenderer,
                                     name = item.sd_layout)
        return renderer.render() or u""
