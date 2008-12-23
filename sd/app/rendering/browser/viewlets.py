# -*- coding: utf-8 -*-

from five import grok
from AccessControl.ZopeGuards import guarded_hasattr
from zope.component import queryUtility
from zope.interface import implements, directlyProvides, Interface
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.contentprovider.interfaces import ITALNamespaceData
from plone.app.layout.viewlets.common import ViewletBase
from sd.contents.interfaces import IPossibleBatchProvider
from interfaces import ISdItemAwareManager


directlyProvides(ISdItemAwareManager,
                 ITALNamespaceData)


grok.templatedir('templates')

class ItemAwareViewletManager(grok.ViewletManager):
    grok.baseclass()
    
    implements(ISdItemAwareManager)
    item = None


class AboveTitle(ItemAwareViewletManager):
    grok.name("sd.above_item_title")


class BelowTitle(ItemAwareViewletManager):
    grok.name("sd.below_item_title")

 
class AboveRendererBody(grok.ViewletManager):
    grok.name("sd.above_content_body")

    def filter(self, viewlets):
        results = []
        for name, viewlet in viewlets:
            if getattr(viewlet, 'available', True):
                viewlet = viewlet.__of__(viewlet.context)
                if guarded_hasattr(viewlet, 'render'):
                    results.append((name, viewlet))
        return results
       

grok.context(Interface)

class OrderingViewlet(grok.Viewlet):

    grok.order(10)
    grok.viewletmanager(BelowTitle)
    grok.require('cmf.ModifyPortalContent')

    def update(self):
        self.uid = self.context.UID()
        self.oid = self.manager.item.getId()
        self.url = self.context.absolute_url()


class AccessViewlet(grok.Viewlet):

    grok.order(20)
    grok.viewletmanager(BelowTitle)
    grok.require('cmf.ModifyPortalContent')

    def update(self):
        self.access = self.manager.item.absolute_url()
        self.edit = self.access + '/edit'
        self.preferences = self.access + '/@@sd.preferences'


class LayoutViewlet(grok.Viewlet):

    grok.order(30)
    grok.viewletmanager(BelowTitle)
    grok.require('cmf.ModifyPortalContent')

    @property
    def vocabulary(self):
        voc = queryUtility(IVocabularyFactory,
                           u"sd.rendering.layout",
                           context=self.context)
        return voc(self.manager.item)

    def update(self):
        self.default_layout = self.manager.item.__view_name__
        self.uid = self.manager.item.UID()
        self.url = self.manager.item._edit_url



class BatchViewlet(grok.Viewlet):

    grok.order(50)
    grok.context(IPossibleBatchProvider)
    grok.viewletmanager(AboveRendererBody)
    grok.require('zope2.View')

    prev_url = u""
    next_url = u""

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
