# -*- coding: utf-8 -*-

from zope.schema import Object
from zope.interface import implements
from interfaces import ITerm, ITermField


class TermField(Object):
    implements(ITermField)

    def __init__(self, schema=ITerm, **kw):
        Object.__init__(self, schema, **kw)
