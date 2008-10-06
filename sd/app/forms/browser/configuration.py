# -*- coding: utf-8 -*-

from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from plone.app.form.base import EditForm
from sd.contents.interfaces import IBatchProvider
from sd.contents.interfaces import IDynamicStructuredChapter
from sd.contents.interfaces import IDynamicStructuredParagraph

_ = MessageFactory("sd")


class StructuredBatchForm(EditForm):
    """Batch configuration panel.
    """
    label = _(u"batch_prefs",
              default=u"Batch preferences")
    
    form_name = _(u"adv_batch_config",
                  default=u"Advanced batch configuration")
    
    form_fields = form.FormFields(IBatchProvider)


class StructuredChapterForm(EditForm):
    """Structured chapter configuration panel.
    """
    label = _(u"chapter_prefs",
              default=u"Chapter preferences")
    
    form_name = _(u"adv_chapter_config",
                  default=u"Advanced chapter configuration")
    
    form_fields = form.FormFields(IDynamicStructuredChapter)
    

class StructuredParagraphForm(EditForm):
    """Structured paragraph configuration panel.
    """
    label = _(u"paragraph_prefs",
              default=u"Paragraph preferences")
    
    form_name = _(u"adv_paragraph_config",
                  default=u"Advanced paragraph configuration")

    form_fields = form.FormFields(IDynamicStructuredParagraph)
