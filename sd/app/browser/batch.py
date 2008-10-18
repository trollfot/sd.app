# -*- coding: utf-8 -*-

from zope.component import queryMultiAdapter
from kss.core import KSSView, kssaction
from sd.rendering.interfaces import IStructuredRenderer
from sd.contents.interfaces import IDynamicStructuredItem
from Products.CMFCore.utils import getToolByName
        

class AjaxBatch(KSSView):

    def getObjectFromUid(self, uid):
        cat = getToolByName(self.context, 'uid_catalog')
        res = cat and cat(UID=uid) or None
        return res and res[0].getObject() or None

    @kssaction
    def batch(self, item, action, page):
        obj = self.getObjectFromUid(item)
        if obj is not None and action is not None:
            adapted = IDynamicStructuredItem(obj)
            renderer = queryMultiAdapter((obj, self.request),
                                         IStructuredRenderer,
                                         name = adapted.sd_layout)
            ksscore = self.getCommandSet('core')
            selector = ksscore.getHtmlIdSelector('kssattr-bodyid-%s' % item)
            renderer.page = int(page)
            ksscore.replaceInnerHTML(selector, renderer.render())
            return self.render()
            
        return self.render()
