# We register the indexable attribute.

from sd.common.catalog.indexable_attributes import hasImageAndCaption
from Products.CMFPlone.CatalogTool import registerIndexableAttribute
registerIndexableAttribute('hasImageAndCaption', hasImageAndCaption)
