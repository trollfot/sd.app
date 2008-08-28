# -*- coding: utf-8 -*-

# Zope
from zope.interface import implements
from Products.Five.browser import BrowserView
from plone.memoize.view import memoize

# Locals
from interfaces import ISDAvailabilityCheckers
from sd.contents.interfaces import IStructuredDocument, IBatchProvider
from sd.contents.interfaces import IStructuredChapter, IStructuredParagraph


class SDAvailabilityCheckers( BrowserView ):

    implements(ISDAvailabilityCheckers)

    @memoize
    def is_chapter(self, explicit=None):
        if not explicit:
            explicit = self.context
        parent = getattr(explicit.aq_inner, 'aq_parent', None)        
        if parent and IStructuredDocument.providedBy(parent):
            return IStructuredChapter.providedBy(explicit)
        return False

    @memoize
    def is_paragraph(self):
        parent = getattr(self.context.aq_inner, 'aq_parent', None)
        if parent and self.is_chapter(explicit = parent):
            return IStructuredParagraph.providedBy(self.context)
        return False

    @memoize
    def is_batchable(self):
        return bool(IBatchProvider(self.context, False))
