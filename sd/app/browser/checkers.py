# -*- coding: utf-8 -*-

# Zope
from zope.interface import implements
from zope.cachedescriptors.property import CachedProperty
from Products.Five.browser import BrowserView
from plone.memoize.view import memoize

# Locals
from interfaces import ISDAvailabilityCheckers
from sd.contents.interfaces import *


class SDAvailabilityCheckers(BrowserView):

    implements(ISDAvailabilityCheckers)

    @memoize
    def show_preferences_tab(self, context=None):
        if not context:
            context = self.context
        parent = getattr(context.aq_inner, 'aq_parent', None)        
        if parent and IStructuredDocument.providedBy(parent):
            return IStructuredItem.providedBy(context)
        return False

    @CachedProperty
    def is_batchable(self):
        return bool(IBatchProvider(self.context, False))
