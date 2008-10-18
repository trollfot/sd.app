# -*- coding: utf-8 -*-
from Acquisition import aq_base
from zope.component import adapts, provideAdapter
from zope.interface import implements
from plone.memoize.instance import memoize
from plone.app.layout.nextprevious.interfaces import INextPreviousProvider
from Products.CMFCore.utils import getToolByName
from sd.contents.interfaces import IStructuredDocument


class SDNextPrevious(object):
    """Let a structured document act as a next/previous provider.
    This will be automatically found by the @@plone_nextprevious_view
    and viewlet.
    """
    implements(INextPreviousProvider)
    adapts(IStructuredDocument)

    def __init__(self, context):
        self.context  = context
        
        sp = getToolByName(self.context, 'portal_properties').site_properties
        self.view_action_types = sp.getProperty('typesUseViewActionInListings',
                                                ())

    def getNextItem(self, obj):
        relatives = self.itemRelatives(obj.getId())
        return relatives["next"]

        
    def getPreviousItem(self, obj):
        relatives = self.itemRelatives(obj.getId())
        return relatives["previous"]

    @property
    def enabled(self):
        return self.context.getNextPreviousEnabled()

    @memoize
    def itemRelatives(self, oid):
        """Get the relative next and previous items
        """
        folder = self.context
        catalog = getToolByName(self.context, 'portal_catalog')
        position = folder.getObjectPosition(oid)

        next = None
        previous = None

        # Get the previous item
        if position - 1 >= 0:
            prev_brain = catalog(
                self.buildNextPreviousQuery(position = position - 1,
                                            range = 'max',
                                            sort_order = 'reverse')
                )
            if prev_brain and len(prev_brain) > 0:
                previous = self.buildNextPreviousItem(prev_brain[0])

        # Get the next item
        if (position + 1) < len(folder._objects):
            next_brain = catalog(
                self.buildNextPreviousQuery(position = position + 1,
                                            range = 'min')
                )
            if next_brain and len(next_brain) > 0:
                next   = self.buildNextPreviousItem(next_brain[0])

        return dict(next=next, previous=previous)

        
    def buildNextPreviousQuery(self, position, range, sort_order = None):
        sort_on = 'getObjPositionInParent'
        
        query = {}
        query['sort_on'] = sort_on
        query['sort_limit'] = 1
        query['object_provides'] = ("sd.contents.interfaces.IStructuredItem")
        query['path'] = dict(query = '/'.join(self.context.getPhysicalPath()),
                             depth = 1)
                
        # Query the position using a range
        query[sort_on] = 0
        if position != 0:
            query[sort_on] = dict(query = position,
                                  range = range)

        # Filters on content
        query['is_default_page'] = False

        # Should I sort in any special way ?
        if sort_order:
            query['sort_order']  = sort_order

        return query


    def buildNextPreviousItem(self, brain):
        return {'id'          : brain.getId,
                'url'         : self.getViewUrl(brain),
                'title'       : brain.Title,
                'description' : brain.Description,
                'portal_type' : brain.portal_type,
                }


    def getViewUrl(self, brain):
        """create link and support contents that requires /view 
        """    
        if brain.portal_type in self.view_action_types:
            return "%s/view" % brain.getURL()
        return brain.getURL()


provideAdapter(SDNextPrevious,
               provides=INextPreviousProvider)
