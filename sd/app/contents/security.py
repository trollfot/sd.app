# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import setDefaultRoles
from Products.CMFCore.permissions import AddPortalContent

def define_right(right, roles=('Manager', 'Owner')):
    setDefaultRoles(right, roles)
    return right

# Add permissions
AddDocument   = define_right("sd: add Structured Document")
AddParagraphs = define_right("sd: add Structured Paragraphs")

DEFAULT_ADD_CONTENT_PERMISSION = AddPortalContent
ADD_CONTENT_PERMISSIONS = {
    'StructuredDocument' : AddDocument,
    'SimpleParagraph'    : AddParagraphs,
}

__all__ = (
    'DEFAULT_ADD_CONTENT_PERMISSION',
    'ADD_CONTENT_PERMISSIONS'
    )
