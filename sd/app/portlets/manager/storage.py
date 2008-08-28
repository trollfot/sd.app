# -*- coding: utf-8 -*-

from zope.interface import implements
from plone.app.portlets.storage import PortletAssignmentMapping
from interfaces import ISDBlocksAssignementMapping


class BlockAssignmentMapping(PortletAssignmentMapping):
    implements(ISDBlocksAssignementMapping)
    id = "++blocks++sd.blocks"
