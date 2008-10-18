# -*- coding: utf-8 -*-

from zope.component.zcml import adapter
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.pagetemplate.simpleviewclass import SimpleViewClass
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.metaclass import makeClass

from sd.rendering.base import StructuredRenderer, FolderishRenderer
from sd.rendering.interfaces import IStructuredRenderer
from sd.common.pagetemplate import ViewPageTemplateAndMacroFile

    
def rendererDirective(_context, targets, renderer=None, template=None,
                      name="default", filtering = None, description=None,
                      folderish=True, macro=None, layer=None):
    
    cname = "StructuredRenderer %s" % name
    attrs = {}

    if template is not None:
        if macro is not None:
            attrs['index'] = ViewPageTemplateAndMacroFile(template)
            attrs['__renderer_macro__'] = macro
        else:
            attrs['index'] = ViewPageTemplateFile(template)
            attrs['__renderer_macro__'] = None

    if renderer is None:
        attrs['__doc__'] = description or u"default renderer"
        baseclasses = (StructuredRenderer,)
    else:
        attrs['__doc__'] = description or renderer.__doc__
        baseclasses = (renderer, StructuredRenderer,)

    if folderish == True:
        baseclasses = baseclasses + (FolderishRenderer,)

    attrs['__name__'] = name
    klass = makeClass(cname, baseclasses, attrs)
    if filtering:
        klass._filtering = filtering

    if layer is None:
        layer = IBrowserRequest
        
    for target in targets:
        adapter(_context, (klass,), provides = IStructuredRenderer,
                for_ = (target, layer), name = name, trusted=True)
