# -*- coding: utf-8 -*-
from zope.schema import Object
from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager
from sd.rendering.interfaces import IBaseStructuredRenderer


class ISdItemAwareManager(Interface):
    item = Object(title=u'The iterated item',
                  schema=IBaseStructuredRenderer)


class IAboveRendererTitle(IViewletManager):
    """A viewlet manager that sits below a structured item title
    """

class IBelowRendererTitle(IViewletManager):
    """A viewlet manager that sits below a structured item title
    """

class IAboveContentBody(IViewletManager):
    """A viewlet manager that sits just above the item's body.
    """
