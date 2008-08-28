# -*- coding: utf-8 -*-

from zope.component import queryMultiAdapter
from kss.core import KSSView, kssaction
from sd.rendering.interfaces import IChapterRenderer, IParagraphRenderer
from sd.contents.interfaces import IDynamicStructuredChapter
from sd.contents.interfaces import IDynamicStructuredParagraph
from Products.CMFCore.utils import getToolByName
        

class SDBatch(KSSView):

    def getObjectFromUid(self, uid):
        cat = getToolByName(self.context, 'uid_catalog')
        res = cat and cat(UID=uid) or None
        return res and res[0].getObject() or None

    
    def render_batch(self, item, page, renderer):
        ksscore = self.getCommandSet('core')
        selector = ksscore.getHtmlIdSelector('kssattr-bodyid-%s' % item)
        renderer.page = int(page)
        ksscore.replaceInnerHTML(selector, renderer.render())
        return self.render()


    @kssaction
    def chapterBatch(self, item, action, page):
        obj = self.getObjectFromUid(item)
        if obj is not None and action is not None:
            adapted = IDynamicStructuredChapter(obj)
            renderer = queryMultiAdapter((obj, self.request),
                                         IChapterRenderer,
                                         name = adapted.sd_layout)
            return self.render_batch(item, page, renderer)                
        return self.render()


    @kssaction
    def paragraphBatch(self, item, action, page):
        obj = self.getObjectFromUid(item)
        if obj is not None and action is not None:
            adapted = IDynamicStructuredParagraph(obj)
            renderer = queryMultiAdapter((obj, self.request),
                                         IParagraphRenderer,
                                         name = adapted.sd_layout)
            return self.render_batch(item, page, renderer)
        return self.render()

