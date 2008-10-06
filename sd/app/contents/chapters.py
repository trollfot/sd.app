# -*- coding: utf-8 -*-

from zope.interface import Interface, implements
from sd.app.contents import PROJECTNAME
from sd.contents.container import StructuredContainer
from sd.contents.interfaces import IStructuredParagraph, IBatchProvider
from interfaces import ISimpleChapter


class SimpleChapter(StructuredContainer):
    """A very simple chapter inside a document
    """
    implements(ISimpleChapter, IBatchProvider)
    allowed_interfaces = (IStructuredParagraph,)
    sd_layout = u"default"
    show_title = True
    batch_size = 0
    show_description = True


# Registers the type
from Products.Archetypes.public import registerType
registerType(SimpleChapter, PROJECTNAME)
