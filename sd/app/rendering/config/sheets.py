# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from sd.rendering.base import BaseConfigSheet
from interfaces import IEnhancedPhotoAlbumConfig, ISlideshowConfig


class EnhancedPhotoAlbumConfig(BaseConfigSheet):
    implements(IEnhancedPhotoAlbumConfig)

    timer = FieldProperty(IEnhancedPhotoAlbumConfig['timer'])


class SlideshowConfig(BaseConfigSheet):
    implements(ISlideshowConfig)

    timer = FieldProperty(ISlideshowConfig['timer'])
    links_next = FieldProperty(ISlideshowConfig['links_next'])
    links_start = FieldProperty(ISlideshowConfig['links_start'])
    image_description = FieldProperty(ISlideshowConfig['image_description'])
    image_size = FieldProperty(ISlideshowConfig['image_size'])

