# -*- coding: utf-8 -*-

from zope.component import queryUtility
from zope.interface import implements, directlyProvides
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.contentprovider.interfaces import ITALNamespaceData

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.viewletmanager.manager import OrderedViewletManager

from sd.rendering.interfaces import IBatchedContentProvider
from sd.rendering.interfaces import IChapterRenderer, IParagraphRenderer
from interfaces import ISdItemAwareManager

directlyProvides(ISdItemAwareManager,
                 ITALNamespaceData)


class SdViewletManager(OrderedViewletManager):
    implements(ISdItemAwareManager)
    item = None


class OrderingViewlet(ViewletBase):
    render = ViewPageTemplateFile("templates/ordering.pt")

    def update(self):
        self.uid = self.context.UID()
        self.oid = self.manager.item.getId()
        self.url = self.context.absolute_url()


class BatchViewlet(ViewletBase):

    prev_url = u""
    next_url = u""
    template = ViewPageTemplateFile("templates/batch.pt")

    @property
    def available(self):
        return not (not self.__parent__.has_next_page and
                    self.__parent__.page == 0)
    
    def update(self):
        page = self.__parent__.page
        self.prev = page - 1
        self.next = page + 1
        
        url = self.request.get('ACTUAL_URL', '')
        sep = "?" in url and "&" or "?"
        
        if self.__parent__.has_next_page:
            self.next_url = "%s%s%s=%i" % (url, sep,
                                           self.__parent__.batch_name,
                                           self.next)

        if page > 0:
            self.prev_url = "%s%s%s=%i" % (url, sep,
                                           self.__parent__.batch_name,
                                           self.prev)
            
    def render(self):
        return self.available and self.template() or u''


class LayoutViewlet(ViewletBase):
    render = ViewPageTemplateFile("templates/layout.pt")

    @property
    def vocabulary(self):
        voc = queryUtility(IVocabularyFactory,
                           self.manager.item._namespace,
                           context=self.context)
        return voc(self.manager.item)

    @property
    def default_layout(self):
        return self.manager.item.__name__

    def update(self):           
        self.uid = self.manager.item.UID()
        self.url = self.manager.item._edit_url
