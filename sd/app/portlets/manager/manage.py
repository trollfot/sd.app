# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import getMultiAdapter
from Products.Five import BrowserView
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import IPortletAssignmentMapping
from interfaces import IManageSDBlocksView


class ManageSDBlocks(BrowserView):
    """A very basic implementation of a block manager.
    """
    implements(IManageSDBlocksView)
        
    @property
    def category(self):
        return CONTEXT_CATEGORY
        
    @property
    def key(self):
        return '/'.join(self.context.getPhysicalPath())
    
    def getAssignmentMappingUrl(self, manager):
        baseUrl = str(getMultiAdapter((self.context, self.request),
                                      name='absolute_url'))
        return '%s/++blocks++%s' % (baseUrl, manager.__name__)

    def getAssignmentsForManager(self, manager):
        assignments = getMultiAdapter((self.context, manager),
                                      IPortletAssignmentMapping)
        return assignments.values()
        
