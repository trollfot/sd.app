# -*- coding: utf-8 -*-

from zope.app.form.browser.widget import SimpleInputWidget
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from sd.app.forms.objects import MinimalTerm


class TermWidget(SimpleInputWidget):
    """The term widget simply renders 2 text inputs that are used as
    a dict key/value couple.
    """
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


