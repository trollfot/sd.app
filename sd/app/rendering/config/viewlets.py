# -*- coding: utf-8 -*-

from five import grok
from zope.interface import Interface
from zope.component import queryUtility
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from sd.config.interfaces import IConfigurationSheetType
from sd.app.rendering.browser.viewlets import AboveRendererBody


class LayoutConfiguration(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(AboveRendererBody)
    grok.require('zope2.View')

    render = ViewPageTemplateFile("config.pt")

    @property
    def layout(self):
        return self.view.__view_name__

    @property
    def configurable(self):
        util = queryUtility(IConfigurationSheetType, self.layout, None)
        return bool(util)

    @property
    def url(self):
        if self.view.configuration is not None or self.configurable:
            return "%s/++configuration++%s" % (self.context.absolute_url(),
                                               self.layout)
        return None
