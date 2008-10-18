# -*- coding: utf-8 -*-

from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from plone.app.form.base import EditForm
from sd.contents.interfaces import IBatchProvider
from sd.contents.interfaces import IDynamicStructuredItem

_ = MessageFactory("sd")


class BatchForm(EditForm):
    """Batch configuration panel.
    """
    label = _(u"batch_prefs",
              default=u"Batch preferences")
    
    form_name = _(u"adv_batch_config",
                  default=u"Advanced batch configuration")
    
    form_fields = form.FormFields(IBatchProvider)


class PreferencesForm(EditForm):
    """Structured paragraph configuration panel.
    """
    label = _(u"paragraph_prefs",
              default=u"Paragraph preferences")
    
    form_name = _(u"adv_paragraph_config",
                  default=u"Advanced paragraph configuration")

    form_fields = form.FormFields(IDynamicStructuredItem)
