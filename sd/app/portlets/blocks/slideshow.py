# -*- coding: utf-8 -*-

from zope.formlib import form
from zope.interface import implements
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.cachedescriptors.property import CachedProperty

from plone.app.portlets.portlets import base
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import normalizeString

from interfaces import ISlideshowPortlet
from sd.common.adapters.interfaces import IContentQueryHandler

_ = MessageFactory("sd")


class Assignment(base.Assignment):
    """A slideshow portlet. This is the very object that will be stored.
    """
    implements(ISlideshowPortlet)

    name = u""
    source = None
    links = True
    links_start = False
    image_description = False
    timer = 0
    size = 'thumb'

    def __init__(self, name=u"", source=None, timer=0, links=False, size='thumb', links_start=False, image_description=False):
        self.name = name
        self.source = source
        self.timer = timer
        self.links = links
        self.size = size
        self.links_start = links_start
        self.image_description = image_description

    @CachedProperty
    def title(self):
        """Title of the portlet
        """
        return self.name


class Renderer(base.Renderer):
    """Renders a slideshow portlet.
    """
    render = ViewPageTemplateFile('templates/slideshow.pt')

    def update(self):
        self.uid = normalizeString(self.data.__name__,
                                   context=self.context)

    def Title(self):
        return self.data.name

    @CachedProperty
    def available(self):
        return len(self.results)

    def size(self):
        return self.data.size

    def timeout(self):
        return self.data.timer * 1000

    def show_links_next(self):
        return self.data.links

    def show_links_start(self):
        return self.data.links_start

    def show_image_description(self):
        return self.data.image_description

    @CachedProperty
    def results(self):
        """Get the actual result brains from the collection.
        It will limit the actual selection to photos.
        """
        results = []
        source = self.source
        iface = "Products.ATContentTypes.interface.image.IPhotoAlbumAble"
        if source is not None:
            contentFilter = dict(object_provides = iface)
            handler = IContentQueryHandler(source, None)
            results = handler and handler.query_contents(contentFilter) or []
        return results

    @CachedProperty
    def source(self):
        """Get the source provider.
        """
        source = self.data.source

        if source.startswith('/'):
            source = source[1:]

        if not source:
            return None

        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        portal = portal_state.portal()
        return portal.restrictedTraverse(source, default=None)


class SlideshowForm(object):
    """This is a mere mixin, to gather the form information for both editing
    and adding.
    """
    form_fields = form.Fields(ISlideshowPortlet)
    form_fields['source'].custom_widget = UberSelectionWidget

    label = _(u"Edit Slideshow Portlet")
    description = _(u"This portlet display a collection of images.")


class AddForm(base.AddForm, SlideshowForm):
    """Add form for a slideshow portlet.
    """
    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm, SlideshowForm):
    """Edit form for a slideshow portlet.
    """

