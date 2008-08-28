# -*- coding: utf-8 -*-
from zope.component import queryMultiAdapter
from Products.Five  import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.view import memoize

from sd.contents.interfaces import IDynamicStructuredParagraph
from sd.rendering.interfaces import IParagraphRenderer


class SimpleParagraphView( BrowserView ):
    """The AT view of the SimpleParagraph
    """
    template = ViewPageTemplateFile("templates/paragraph_view.pt")
    
    @memoize
    def render(self):
        paragraph = IDynamicStructuredParagraph(self.context)
        renderer = queryMultiAdapter((self.context, self.request),
                                     IParagraphRenderer,
                                     name = paragraph.sd_layout)
        return renderer or u""

    def __call__(self):
        return self.template(paragraph = self.render())
