# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from sd.rendering.base import BaseConfigSheet
from interfaces import IEnhancedPhotoAlbumConfig


class EnhancedPhotoAlbumConfig(BaseConfigSheet):
    implements(IEnhancedPhotoAlbumConfig)
    
    name  = FieldProperty(IEnhancedPhotoAlbumConfig['name'])
    timer = FieldProperty(IEnhancedPhotoAlbumConfig['timer'])
