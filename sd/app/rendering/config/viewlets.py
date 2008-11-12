# -*- coding: utf-8 -*-

from five import grok
from zope.component import queryUtility
from sd.app.rendering.browser.viewlets import AboveRendererBody
from zope.cachedescriptors.property import CachedProperty
from sd.config.interfaces import IConfigurationSheetType
from sd.contents.interfaces import IStructuredItem
from zope.i18nmessageid import MessageFactory
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
    def configurable(self):
        return bool(self.view.configurable)

    @CachedProperty
    def url(self):
        if self.view.configuration is not None or self.configurable:
            return "%s/++configuration++%s" % (self.context.absolute_url(),
                                               self.layout)
        return None

    def render(self):
        if not self.url:
            return u''
        return u'''<p class="configuration-sheet discreet">
                   <a href="%s">%s</a>
                  </p>''' % (self.url, _("Display configuration"))
