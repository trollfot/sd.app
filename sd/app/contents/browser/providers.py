# -*- coding: utf-8 -*-

from zope.interface import implements
from Products.Five  import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from sd.rendering.interfaces import IStructuredDocumentView
from sd.common.adapters.interfaces import IContentQueryHandler


class DocumentContentProvider(BrowserView):
    """Access to a document contents
    """
    implements(IStructuredDocumentView)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @memoize
    def contents(self, full_objects=True):
        contentFilter  = {"object_provides":
                          'sd.contents.interfaces.IStructuredChapter'}
        handler = IContentQueryHandler(self.context)
        brains = handler and handler.query_contents(contentFilter) or []
        return (full_objects and [brain.getObject() for brain in brains]
                or brains)
