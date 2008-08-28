# -*- coding: utf-8 -*-

from zope.interface import implements
from Products.Five  import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from sd.rendering.interfaces import IStructuredDocumentView
from interfaces import IDocumentContentProvider


class DocumentContentProvider(BrowserView):
    """Access to a document contents
    """
    implements(IDocumentContentProvider, IStructuredDocumentView)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @memoize
    def contents(self, full_objects=True):
        iface  = {"object_provides":
                  'sd.contents.interfaces.IStructuredChapter'}       
        return self.context.getFolderContents(contentFilter = iface,
                                              full_objects = full_objects)
