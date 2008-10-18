# -*- coding: utf-8 -*-

from kss.core import KSSView, kssaction
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

_ = MessageFactory("sd")


class SdOrdering(BrowserView):

    def redirect(self, utils, oid):
        url = self.request['HTTP_REFERER']
        utils.addPortalMessage(_(u"Item's position has changed."))
        return self.request.RESPONSE.redirect("%s#%s-%s" % (url,
                                                            self.context.UID(),
                                                            oid))

    def doMoveUp(self, oid, redirect=True):
        utils = getToolByName(self.context, 'plone_utils')
        self.context.moveObjectsUp(oid)
        utils.reindexOnReorder(self.context)
        return redirect and self.redirect(utils, oid) or True

    def doMoveDown(self, oid, redirect=True):
        utils = getToolByName(self.context, 'plone_utils')
        self.context.moveObjectsDown(oid)
        utils.reindexOnReorder(self.context)
        return redirect and self.redirect(utils, oid) or True


class KssSdOrdering(KSSView):

    def getObjectFromUid(self, uid):
        cat = getToolByName(self.context, 'portal_catalog')
        res = cat and cat(UID=uid) or None
        return res and res[0].getObject() or None


    @kssaction
    def orderMoveUp(self, parent, oid):
        obj  = self.getObjectFromUid(parent)

        if obj is None:
            return self.render()
        
        idxs = obj.objectIds()
        idx  = idxs.index(oid)

        if idx > 0:
            swapWith = "%s-%s" % (parent, idxs[idx - 1])

            # this could be done by getting the browserview @@doMoveUp
            # but, does it really worth the cost ?
            utils = getToolByName(self.context, 'plone_utils')
            obj.moveObjectsUp(oid)
            utils.reindexOnReorder(obj)

            ksscore = self.getCommandSet('core')
            selector = ksscore.getHtmlIdSelector("%s-%s" % (parent, oid))
            ksscore.moveNodeBefore(selector, swapWith)

        return self.render()


    @kssaction
    def orderMoveDown(self, parent, oid):
        obj  = self.getObjectFromUid(parent)
        
        if obj is None:
            return self.render()
        
        idxs = obj.objectIds()
        idx  = idxs.index(oid)
        length = len(idxs)

        if length > 1 and idx != length - 1:
            swapWith = "%s-%s" % (parent, idxs[idx + 1])

            # this could be done by getting the browserview @@doMoveDown
            # but, does it really worth the cost ?
            utils = getToolByName(self.context, 'plone_utils')
            obj.moveObjectsDown(oid)
            utils.reindexOnReorder(obj)
            
            ksscore = self.getCommandSet('core')
            selector = ksscore.getHtmlIdSelector("%s-%s" % (parent, oid))
            ksscore.moveNodeAfter(selector, swapWith)

        return self.render()
