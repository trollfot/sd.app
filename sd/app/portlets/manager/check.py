# -*- coding: utf-8 -*-

from AccessControl import getSecurityManager, Unauthorized
from Acquisition import aq_inner
from zope.component import adapts
from zope.interface import implements
from plone.app.portlets.interfaces import IPortletPermissionChecker
from interfaces import ISDBlocksAssignementMapping


class BlockPermissionChecker(object):
    implements(IPortletPermissionChecker)
    adapts(ISDBlocksAssignementMapping)
    
    def __init__(self, context):
        self.context = context
    
    def __call__(self):
        sm = getSecurityManager()
        context = aq_inner(self.context)

        if not sm.checkPermission("Modify portal content", context):
            raise Unauthorized("You are not allowed to manage blocks")

        return True
