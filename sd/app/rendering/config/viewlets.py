# -*- coding: utf-8 -*-

from five import grok
from zope.component import queryUtility
from zope.cachedescriptors.property import CachedProperty
from zope.i18nmessageid import MessageFactory

from sd.app.rendering.browser.viewlets import AboveRendererBody
from sd.rendering.interfaces import IConfigurableRenderer
from sd.contents.interfaces import IStructuredItem

_ = MessageFactory("sd")


class LayoutConfiguration(grok.Viewlet):
    grok.order(60)
    grok.context(IStructuredItem)
    grok.viewletmanager(AboveRendererBody)
    grok.require('cmf.ModifyPortalContent')

    @CachedProperty
    def layout(self):
        return self.view.__view_name__

    @CachedProperty
    def url(self):
        layout = self.view.__view_name__
        if self.view.configuration:
            return "%s/@@%s/configuration/@@edit" % (
                self.view.absolute_url(), layout
                )
            
        return "%s/@@%s/@@configure" % (
                self.view.absolute_url(), layout
                )

    def render(self):
        if not IConfigurableRenderer.providedBy(self.view):
            return u''
        return u'''<p class="configuration-sheet discreet">
                   <a href="%s">%s</a>
                  </p>''' % (self.url, _("Display configuration"))
