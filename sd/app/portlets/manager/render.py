# -*- coding: utf-8 -*-

from AccessControl import getSecurityManager
from zope.component import adapts
from zope.interface import Interface
from zope.publisher.interfaces import browser
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.browser.editmanager import EditPortletManagerRenderer
from plone.app.portlets.manager import ColumnPortletManagerRenderer
from interfaces import IStructuredDocumentBlocks, IManageSDBlocksView


class SDBlocksManagerRenderer(ColumnPortletManagerRenderer):
    """Render a column of structured blocks
    """
    adapts(Interface, browser.IDefaultBrowserLayer,
           browser.IBrowserView, IStructuredDocumentBlocks)

    template = ViewPageTemplateFile('templates/renderer.pt')

    def __init__(self, context, request, view, manager):
        super(SDBlocksManagerRenderer, self).__init__(
            context, request, view, manager)

    def can_manage_portlets(self):
        sm = getSecurityManager()
        context = self._context()
        if not sm.checkPermission("Modify portal content", context):
            return False
        return True


class SDBlocksEditRenderer(EditPortletManagerRenderer):
    """Render the edit mode of the structured blocks column
    """
    adapts(Interface, browser.IDefaultBrowserLayer,
           IManageSDBlocksView, IStructuredDocumentBlocks)
