# -*- coding: utf-8 -*-
from zope.interface import Interface


class IDocumentContentProvider(Interface):
    """Interface to get the structure of a structured document
    """
    def contents(self, full_objects=True):
        """Returns a list of contained items. If full_objects is set to False,
        it returns the corresponding catalog brains instead.
        """
