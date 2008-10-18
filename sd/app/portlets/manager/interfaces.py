# -*- coding: utf-8 -*-

from zope.interface import Interface
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.app.portlets.browser.interfaces import IManagePortletsView
from plone.app.portlets.interfaces import IColumn

class IManageSDBlocksView(IManagePortletsView):
    """Marker for the manage structured blocks view
    """

class ISDBlocksAssignementMapping(IPortletAssignmentMapping):
    """FIXME
    """

class IStructuredDocumentBlocks( IPortletManager, IColumn ):
    """A portlet manager, handling 'blocks', the contextual
    portlets limited to a single structured document.
    """
