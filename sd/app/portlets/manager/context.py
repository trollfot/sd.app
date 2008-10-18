# -*- coding: utf-8 -*-

from Acquisition import aq_inner, aq_parent
from zope.component import adapts
from zope.interface import implements
from plone.portlets.interfaces import IPortletContext
from sd.contents.interfaces import IStructuredDocument


class BlockContext(object):
    """Fixme
    """
    implements(IPortletContext)
    adapts(IStructuredDocument)

    def __init__(self, context):
        self.context = context

    @property
    def uid(self):
        return '/'.join(self.context.getPhysicalPath())

    def getParent(self):
        return aq_parent(aq_inner(self.context))

    def globalPortletCategories(self, placeless=False):
        return []
