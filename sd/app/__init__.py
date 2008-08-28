"""Structured Document application package
"""
# Project globals
PACKAGE = "sd.app"

# We register the indexable attribute.
from sd.common.catalog.indexable_attributes import hasImageAndCaption
from Products.CMFPlone.CatalogTool import registerIndexableAttribute
registerIndexableAttribute('hasImageAndCaption', hasImageAndCaption)
