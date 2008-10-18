# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute


class ISDAvailabilityCheckers( Interface ):
    """A convenient way to check interfaces availability on objects.
    """
    def show_preferences_tab(self, context=None):
        """
        """

    is_batchable = Attribute(u"Boolean value to enable or not the batch tab.")
