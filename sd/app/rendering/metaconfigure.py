# -*- coding: utf-8 -*-

from zope.component.zcml import adapter
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.pagetemplate.simpleviewclass import SimpleViewClass
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.metaclass import makeClass

from sd.rendering.base import ChapterStructuredRenderer
from sd.rendering.base import ParagraphStructuredRenderer
from sd.rendering.base import FolderishRenderer
from sd.rendering.interfaces import IChapterRenderer, IParagraphRenderer
from sd.common.pagetemplate import ViewPageTemplateAndMacroFile


def chapterDirective(_context, targets, renderer=None, template=None,
                     name="default", filtering = None, description=None,
                     folderish=True, macro=None):

    cname = "Chapter renderer %s" % name
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
        baseclasses = (ChapterStructuredRenderer,)
    else:
        attrs['__doc__'] = description or renderer.__doc__
        baseclasses = (renderer, ChapterStructuredRenderer)

    if folderish == True:
        baseclasses = baseclasses + (FolderishRenderer,)

    attrs['__name__'] = name
    klass = makeClass(cname, baseclasses, attrs)
    if filtering:
        klass._filtering = filtering

    for target in targets:
        adapter(_context, (klass,), provides = IChapterRenderer,
                for_ = (target,IBrowserRequest), name = name, trusted=True)
    

def paragraphDirective(_context, targets, renderer=None, template=None,
                       name="default", filtering = None, description=None,
                       folderish=False, macro=None):
    
    cname = "Paragraph renderer %s" % name
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
        baseclasses = (ParagraphStructuredRenderer,)
    else:
        attrs['__doc__'] = description or renderer.__doc__
        baseclasses = (renderer, ParagraphStructuredRenderer,)

    if folderish == True:
        baseclasses = baseclasses + (FolderishRenderer,)

    attrs['__name__'] = name
    klass = makeClass(cname, baseclasses, attrs)
    if filtering:
        klass._filtering = filtering

    for target in targets:
        adapter(_context, (klass,), provides = IParagraphRenderer,
                for_ = (target,IBrowserRequest), name = name, trusted=True)
