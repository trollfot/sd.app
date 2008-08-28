# -*- coding: utf-8 -*-
from zope.component import queryMultiAdapter
from Products.Five  import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.view import memoize

from sd.contents.interfaces import IDynamicStructuredChapter
from sd.rendering.interfaces import IChapterRenderer


class SimpleChapterView(BrowserView):
    """The AT view of the SimpleChapter
    """
    template = ViewPageTemplateFile("templates/chapter_view.pt")
    
    @memoize
    def render(self):
        chapter = IDynamicStructuredChapter(self.context)
        renderer = queryMultiAdapter((self.context, self.request),
                                     IChapterRenderer,
                                     name = chapter.sd_layout)
        return renderer or u""

    def __call__(self):
        return self.template(chapter = self.render())
