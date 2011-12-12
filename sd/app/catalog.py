# We register the indexable attribute.
from zope.interface import Interface
from plone.indexer.decorator import indexer
from sd.common.catalog.indexable_attributes import hasImageAndCaption
from Products.CMFCore.utils import getToolByName

@indexer(Interface)
def hasImageAndCaptionFactory(content):
    return hasImageAndCaption(
        content,
        getToolByName('portal_tool', content).getPortalObject())
