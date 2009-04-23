# -*- coding: utf-8 -*-

from five import grok
from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from sd.contents import interfaces

_ = MessageFactory("sd")

grok.templatedir("templates")

class PreferencesForm(grok.EditForm):
    """Structured item configuration panel.
    """
    grok.name("sd.preferences")
    grok.context(interfaces.IStructuredItem)
    grok.require("cmf.ModifyPortalContent")

    label = _(u"sd.preferences",
              default=u"Rendering preferences")
    
    form_name = _(u"adv_config",
                  default=u"Advanced configuration")
    
    @property
    def form_fields(self):
        ifaces = [interfaces.IDynamicStructuredItem]
        if interfaces.IPossibleBatchProvider.providedBy(self.context):
            ifaces.append(interfaces.IBatchProvider)
        return form.FormFields(*ifaces)
    
    @grok.action(_(u"label_save", default=u"Save"))
    def handle_save_action(self, *args, **data):
        if form.applyChanges(self.context,
                             self.form_fields, data,
                             self.adapters):
            self.status = u"Save changed"
        else:
            self.status = u"No changes"
