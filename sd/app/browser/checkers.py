# -*- coding: utf-8 -*-

from five import grok

from sd.contents import interfaces as sdct
from zope.interface import directlyProvides, noLongerProvides

class ShowPreferences(grok.View):

    grok.context(sdct.IStructuredItem)
    grok.name("sd.show_preferences")
    grok.require("zope2.View")

    def render(self):
        return True


class ShowPortlets(grok.View):

    grok.context(sdct.IStructuredDocument)
    grok.name("sd.is_structured_document")
    grok.require("zope2.View")

    def render(self):
        return True


class Tagging(grok.View):

    grok.context(sdct.IStructuredItem)
    grok.name("sd.tagging")
    grok.require("cmf.ModifyPortalContent")

    def render(self):
        directlyProvides(self.context, sdct.IStructuredDocument)
        self.context.setLayout("@@sd.document.onepage")
        self.context.reindexObject()
        self.request.RESPONSE.redirect(self.context.absolute_url())


class UnTagging(grok.View):

    grok.context(sdct.IStructuredDocument)
    grok.name("sd.untagging")
    grok.require("cmf.ModifyPortalContent")

    def render(self):
        noLongerProvides(self.context, sdct.IStructuredDocument)
        self.context.setLayout(self.context.getDefaultLayout())
        self.context.reindexObject()
        self.request.RESPONSE.redirect(self.context.absolute_url())


class DocumentOptions(grok.View):

    grok.context(sdct.IStructuredDocument)
    grok.name("sd.options")
    grok.require("cmf.ModifyPortalContent")

    def render(self):
        layout = self.request.get('layout', None)
        if layout:
            self.context.setLayout(layout)
        self.request.RESPONSE.redirect(self.context.absolute_url())
