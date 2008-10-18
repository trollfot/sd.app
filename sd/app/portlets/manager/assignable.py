# -*- coding: utf-8 -*-

from BTrees.OOBTree import OOBTree
from zope.interface import implementer
from zope.component import adapter
from zope.annotation.interfaces import IAnnotations

from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import ILocalPortletAssignable
from plone.portlets.constants import CONTEXT_ASSIGNMENT_KEY
from plone.app.portlets.storage import PortletAssignmentMapping

from storage import BlockAssignmentMapping
from interfaces import IStructuredDocumentBlocks


@adapter(ILocalPortletAssignable, IStructuredDocumentBlocks)
@implementer(IPortletAssignmentMapping)
def localPortletAssignmentMappingAdapter(context, manager):
    """Fixme
    """
    annotations = IAnnotations(context)
    local = annotations.get(CONTEXT_ASSIGNMENT_KEY, None)
    if local is None:
        local = annotations[CONTEXT_ASSIGNMENT_KEY] = OOBTree()
    portlets = local.get(manager.__name__, None)
    if portlets is None:
        portlets = local[manager.__name__] = BlockAssignmentMapping()
    return portlets
