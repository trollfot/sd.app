# -*- coding: utf-8 -*-
from zope.interface import Interface


class IDocumentContentProvider(Interface):
    """Interface to get the structure of a structured document
    """
    def contents():
        """Returns a list of brains, representing the contained objects.
        """
        
