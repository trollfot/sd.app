# -*- coding: utf-8 -*-

from zope.component import queryUtility
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from sd.config.interfaces import IConfigurationSheetType


class LayoutConfiguration(ViewletBase):
    render = ViewPageTemplateFile("config.pt")

    @property
    def layout(self):
        return self.view.__name__

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
