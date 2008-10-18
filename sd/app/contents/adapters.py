# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements
from sd.contents.interfaces import *
from sd.common.adapters.base import BaseAdapter
from sd.common.fields.annotation import AdapterAnnotationProperty


class AnnonationBatchAdapter(BaseAdapter):
    """This adapter provides the field necessary for batch properties
    It will store the data in annotations.
    """
    adapts(IPossibleBatchProvider)
    implements(IBatchProvider)

    batch_size = AdapterAnnotationProperty(
        IBatchProvider['batch_size'],
        ns="sd.batch"
        )


class DynamicLayoutAdapter(BaseAdapter):
    """This adapter provides the fields necessary for paragraphs'
    layout properties. It will store the data in annotations.
    """
    adapts(IStructuredItem)
    implements(IDynamicStructuredItem, IUndirectLayoutProvider)

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
