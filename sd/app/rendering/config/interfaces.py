# -*- coding: utf-8 -*-

from zope.schema import Int, Bool
from sd.config.interfaces import IConfigurationSheet
from sd import _


class IEnhancedPhotoAlbumConfig(IConfigurationSheet):
    """Defines a configuration sheet useable of an enhanced photo gallery.
    """
    timer = Int(title=_("slideshow_timer", default=u"Timer"),
                description=_("slideshow_timer_desc",
                              default=u"The time between each image (sec)"),
                default=5,
                required=True)
