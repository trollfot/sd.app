# -*- coding: utf-8 -*-

from zope.interface import Interface


class ISDAvailabilityCheckers( Interface ):
    """A convenient way to check interfaces availability on objects.
    """
    def is_chapter(self):
        """Return True is the context is an IStructuredChapter
        """

    def is_paragraph(self):
        """Return True is the context is an IStructuredParagraph
        """
