# -*- coding: utf-8 -*-

from five import grok
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.form.browser.widget import SimpleInputWidget
from zope.app.form.interfaces import IInputWidget
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from objects import MinimalTerm
from interfaces import ITermField


class TermWidget(grok.MultiAdapter, SimpleInputWidget):
    """The term widget simply renders 2 text inputs that are used as
    a dict key/value couple.
    """
    grok.adapts(ITermField, IBrowserRequest)
    grok.provides(IInputWidget)
    
    template = ViewPageTemplateFile('templates/dict_widget.pt')

    def __call__(self):
        data = self._data
        return self.template(name = self.name,
                             key = data and data.label or u"",
                             value = data and data.value or u"")

    def _toFieldValue(self, input):
        if isinstance(input, list) and len(input) == 2:
            return MinimalTerm(*input)
        return u""


