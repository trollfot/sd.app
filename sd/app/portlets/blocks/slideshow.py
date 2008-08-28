# -*- coding: utf-8 -*-

from zope.formlib import form
from zope.interface import implements
from zope.component import getMultiAdapter

from plone.memoize.instance import memoize
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.ATContentTypes.interface import IATTopic
from Products.CMFPlone.utils import normalizeString

from sd import _
from interfaces import ISlideshowPortlet


class Assignment(base.Assignment):
    """A slideshow portlet. This is the very object that will be stored.
    """
    implements(ISlideshowPortlet)

    name = u""
    source = None
    links = True
    timer = 0
    
    def __init__(self, name=u"", source=None, timer=0, links=None):
        self.name = name
        self.source = source
        self.timer = timer
        self.links = links

    @property
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

    @property
    def available(self):
        return len(self.results)

    @property
    def show_links(self):
        return self.data.links

    @property
    @memoize
    def results(self):
        """Get the actual result brains from the collection.
        It will limit the actual selection to photos.
        """
        results = []
        source = self.source
        iface = "Products.ATContentTypes.interface.image.IPhotoAlbumAble"
        if source is not None:
            if IATTopic.providedBy(source):
                results = source.queryCatalog(object_provides = iface)
            else:
                filters = dict(object_provides = iface)
                results = source.getFolderContents(contentFilter = filters)
        return results

    @property
    def javascript_snippet(self):
        return """jq(document).ready(function(){ 
          jq('#slideshow-%(uid)s .slideshow').cycle({ 
          fx:     'fade',
          speed:  'fast',
          timeout: %(timer)i,
          height: 160,
          width: 180,
          next: '#slideshow-%(uid)s .next',
          prev: '#slideshow-%(uid)s .prev'
          }); })
          """ % {'uid': self.uid,
                 'timer': self.data.timer*1000}

    @property
    @memoize
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

