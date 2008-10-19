# -*- coding: utf-8 -*-

from kss.core import KSSView, kssaction
from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName
from sd.rendering.interfaces import IStructuredRenderer
from sd.contents.interfaces import IDynamicStructuredItem


class ChangeLayout(KSSView):

    def getObjectFromUid(self, uid):
        cat = getToolByName(self.context, 'portal_catalog')
        res = cat and cat(UID=uid) or None
        return res and res[0].getObject() or None
    
    @kssaction
    def changeLayout(self, layout, item):

        obj = self.getObjectFromUid(item)

        if obj is not None:
            adapted = IDynamicStructuredItem(obj)
            old = adapted.sd_layout
            adapted.sd_layout = layout
            renderer = queryMultiAdapter((obj, self.request),
                                         IStructuredRenderer,
                                         name = layout)

            ksscore = self.getCommandSet('core')
            selector = ksscore.getHtmlIdSelector('kssattr-bodyid-%s' % item)
            ksscore.replaceInnerHTML(selector, renderer.render())

            for change in [old, layout]:
                switcher = "ul.kssattr-uid-%s a.kssattr-layout-%s" % (item,
                                                                      change)
                node = ksscore.getCssSelector(switcher)
                ksscore.toggleClass(node, value="selected-layout")

            script_id = "script-js-%s" % renderer.UID()
            ksscore.deleteNode(ksscore.getCssSelector("head %s" % script_id))

            javascript_snippet = None
            try:
                javascript_snippet = renderer.javascript()
            except NotImplementedError:
                javascript_snippet = None

            if javascript_snippet is not None:
                head = ksscore.getCssSelector("head")
                ksscore.insertHTMLAsLastChild(head,
                                              '<script id="%s">%s</script>' %
                                              (script_id, javascript_snippet))

        return self.render()
