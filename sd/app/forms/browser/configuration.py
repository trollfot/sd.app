# -*- coding: utf-8 -*-

from five import grok
from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from plone.app.form.base import EditForm
from sd.contents.interfaces import IBatchProvider
from sd.contents.interfaces import IDynamicStructuredItem
from sd.contents.interfaces import IPossibleBatchProvider

_ = MessageFactory("sd")


class BatchForm(grok.EditForm):
    """Batch configuration panel.
    """
    grok.name("sd.batch")
    grok.context(IPossibleBatchProvider)
    grok.require("cmf.ModifyPortalContent")
    
    label = _(u"sd.batch",
              default=u"Batch preferences")
    
    form_name = _(u"adv_batch_config",
                  default=u"Advanced batch configuration")
    
    form_fields = form.FormFields(IBatchProvider)


class PreferencesForm(EditForm):
    """Structured item configuration panel.
    """
    label = _(u"sd.preferences",
              default=u"Rendering preferences")
    
    form_name = _(u"adv_config",
                  default=u"Advanced configuration")

    form_fields = form.FormFields(IDynamicStructuredItem)
