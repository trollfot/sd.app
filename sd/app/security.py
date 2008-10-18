# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile


def _getContext(self):
    while 1:
        self = self.aq_parent
        if not getattr(self, '_is_wrapperish', None):
            return self
        
ZopeTwoPageTemplateFile._getContext = _getContext
