# -*- coding: utf-8 -*-

# Imports: Structured Document
from sd.app.contents import PROJECTNAME
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.content.folder import ATFolder
from sd.contents.interfaces import IStructuredDocument, IStructuredItem
from Products.Archetypes.ArchetypeTool import listTypes

# Imports: Zope
from zope.interface import implements
from Products.Archetypes.public import registerType
from Products.ATContentTypes.content.document import ATDocument


class StructuredDocument(ATFolder):
    """A structured document
    """
    implements(IStructuredDocument)

    # Configuration of my type
    schema = ATFolder.schema.copy() + \
             ATDocument.schema.copy()
    
    # Contents
    allowed_interfaces = (IStructuredItem,)
    
    # Modifications on the schema
    schema['text'].required    = False
    schema['subject'].schemata = 'default'
    schema['tableContents'].default = True
    
    # Reorganizing schema
    schema.moveField('subject', after='description')

    def listTypeInfo(self, ifaces):
        pt = getToolByName(self, 'portal_types')
        value = []
        for data in listTypes():
            klass = data['klass']
            for iface in ifaces:
                if iface.implementedBy(klass):
                    ti = pt.getTypeInfo(data['portal_type'])
                    if ti is not None:
                        value.append(ti)
        return value

    def getDefaultAddableTypes(self, context=None):
        if context is None:
            context = self

        pt      = getToolByName(self, 'portal_types')        
        allow   = self.listTypeInfo(self.allowed_interfaces)
        allowed = [item.getId() for item in allow]
        result  = [contentType for contentType in pt.listTypeInfo(context)
                   if contentType.getId() in allowed]

        return [t for t in result if t.isConstructionAllowed(context)]

    # We want this next previous by default
    def getNextPreviousParentValue(self):
        return True


registerType(StructuredDocument, PROJECTNAME)
