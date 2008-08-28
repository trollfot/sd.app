# -*- coding: utf-8 -*-

from BTrees.OOBTree import OOBTree
from zope.component import adapts
from zope.interface import implements
from zope.annotation.interfaces import IAnnotations
from sd.contents.interfaces import *
from sd.common.fields.annotation import AdapterAnnotationProperty
from sd.common.adapters.base import BaseAdapter
from sd.contents.interfaces import IUndirectLayoutProvider


class AnnonationBatchAdapter(BaseAdapter):
    """This adapter provides the field necessary for batch properties
    It will store the data in annotations.
    """
    adapts(IPossibleBatchProvider)
    implements(IBatchProvider)

    # Annotation field
    batch_size = AdapterAnnotationProperty(
        IBatchProvider['batch_size'],
        ns="sd.batch"
        )


class DynamicLayoutChapterAdapter(BaseAdapter):
    """This adapter provides the fields necessary for chapters' layout
    properties. It will store the data in annotations.
    """
    adapts(IStructuredChapter)
    implements(IDynamicStructuredChapter, IUndirectLayoutProvider)
    
    # Annotation fields
    sd_layout = AdapterAnnotationProperty(
        IDynamicStructuredChapter["sd_layout"],
        ns = "sd.chapter",
        name = "layout"
        )
    
    show_title = AdapterAnnotationProperty(
        IDynamicStructuredChapter["show_title"],
        ns = "sd.chapter",
        )
    
    show_description = AdapterAnnotationProperty(
        IDynamicStructuredChapter["show_description"],
        ns = "sd.chapter",
        )


class DynamicLayoutParagraphAdapter(BaseAdapter):
    """This adapter provides the fields necessary for paragraphs'
    layout properties. It will store the data in annotations.
    """
    adapts(IStructuredParagraph)
    implements(IDynamicStructuredParagraph, IUndirectLayoutProvider)

    # Annotation fields
    sd_layout = AdapterAnnotationProperty(
        IDynamicStructuredParagraph["sd_layout"],
        ns = "sd.paragraph",
        name = "layout"
        )
    
    show_title = AdapterAnnotationProperty(
        IDynamicStructuredParagraph["show_title"],
        ns = "sd.paragraph",
        )
    
    show_description = AdapterAnnotationProperty(
        IDynamicStructuredParagraph["show_description"],
        ns = "sd.paragraph",
        )
