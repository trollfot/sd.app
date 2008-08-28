# -*- coding: utf-8 -*-
from zope.interface import Interface


class IDocumentContentProvider( Interface ):
    """Interface to get the structure of a structured document
    """
    def chapters():
        """Returns a list of chapters brain
        """
