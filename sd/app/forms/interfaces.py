# -*- coding: utf-8 -*-

from zope.schema import TextLine
from zope.interface import Interface


class ITerm(Interface):
    """A very simple term representing a couple key/value
    """
    label = TextLine(title=u'Label')
    value = TextLine(title=u'Value')
