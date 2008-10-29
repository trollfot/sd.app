# -*- coding: utf-8 -*-

from five import grok
from sd.contents.interfaces import *
from sd.common.fields.annotation import AdapterAnnotationProperty


class AnnonationBatchAdapter(grok.Adapter):
    """This adapter provides the field necessary for batch properties
    It will store the data in annotations.
    """
    grok.context(IPossibleBatchProvider)
    grok.provides(IBatchProvider)

    batch_size = AdapterAnnotationProperty(
        IBatchProvider['batch_size'],
        ns="sd.batch"
        )


class DynamicLayoutAdapter(grok.Adapter):
    """This adapter provides the fields necessary for embedded
    layout properties. It will store the data in annotations.
    """
    grok.context(IStructuredItem)
    grok.implements(IUndirectLayoutProvider)
    grok.provides(IDynamicStructuredItem)

    sd_layout = AdapterAnnotationProperty(
        IDynamicStructuredItem["sd_layout"],
        ns = "sd.preferences",
        name = "layout"
        )
    
    show_title = AdapterAnnotationProperty(
        IDynamicStructuredItem["show_title"],
        ns = "sd.preferences",
        )
    
    show_description = AdapterAnnotationProperty(
        IDynamicStructuredItem["show_description"],
        ns = "sd.preferences",
        )
