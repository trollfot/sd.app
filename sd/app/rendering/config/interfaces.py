# -*- coding: utf-8 -*-

from zope.schema import Int, Choice, Bool
from zope.i18nmessageid import MessageFactory
from sd.rendering.interfaces import IConfigurationSheet


_ = MessageFactory("sd")


class IEnhancedPhotoAlbumConfig(IConfigurationSheet):
    """Defines a configuration sheet useable of an enhanced photo gallery.
    """
    timer = Int(title=_("slideshow_timer", default=u"Timer"),
                description=_("slideshow_timer_desc",
                              default=u"The time between each image (sec)"),
                default=5,
                required=True)



class ISlideshowConfig(IConfigurationSheet):
    """Defines a configuration sheet useable for a slideshow.
    """
    timer = Int(
        title = _(u"timer", default=u"Timer (in seconds)"),
        description = _(u"timer_desc", default=u"The timer defines the time "
                        u"between each image. If the timer is set to 0, a "
                        u"click is needed to trigger the transition."),
        default=30,
        required = True)
    links_next = Bool(
        title = _(u"slideshow_links", default=u"Display next-previous links"),
        description = _(u"slideshow_links_desc", default=u"You can display "
                        "links to trigger manually the transition between "
                        u"each image can be triggered manually. "),
        required = False)
    links_start = Bool(
        title = _(
            u"slideshow_links_start",
            default=u"Display start-stop links"),
        description = _(
            u"slideshow_links_desc",
            default=u"You can display links to trigger manually " \
                u"the start and stop of slideshow. "),
        required = False)
    image_description = Bool(
        title = _(
            u"slideshow_image_description",
            default=u"Display image description"),
        description = _(
            u"slideshow_image_description_desc",
            default=u"You can display the image description. "),
        required = False)
    image_size = Choice(
        title = _(u"Image size"),
        default = 'thumb',
        values = ['thumb', 'mini', 'preview'],
        required = True)
