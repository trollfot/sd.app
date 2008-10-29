# -*- coding: utf-8 -*-

from five import grok
from sd.contents.interfaces import IStructuredItem


class ShowPreferences(grok.View):

    grok.context(IStructuredItem)
    grok.name("sd.show_preferences")
    grok.require("zope2.View")

    def render(self):
        return True
