# -*- coding: utf-8 -*-

from zope.interface import implements
from interfaces import ITerm


class MinimalTerm(object):
    implements(ITerm)

    def __init__(self, label, value):
        self.label = label
        self.value = value
