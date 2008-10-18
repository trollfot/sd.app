# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest
from zope.component import adapts, getUtility, getMultiAdapter
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from sd.contents.interfaces import IStructuredDocument


class SDBlocksNamespace(object):
    """Determines the namespace traverser ++blocks++
    """
    implements(ITraversable)
    adapts(IStructuredDocument, IHTTPRequest)
    
    def __init__(self, context, request=None):
        self.context = context
        self.request = request        

    @property
    def key(self):
        return '/'.join(self.context.getPhysicalPath())
        
    def traverse(self, name, ignore):
        column = getUtility(IPortletManager, name=name)
        manager = getMultiAdapter((self.context, column,),
                                  IPortletAssignmentMapping)
        return manager
