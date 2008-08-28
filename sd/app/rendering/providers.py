# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import queryAdapter, adapts, provideAdapter
from zope.component import queryMultiAdapter
from zope.publisher.interfaces.browser import IBrowserRequest
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from sd.rendering.base import BaseStructuredContentProvider
from sd.rendering.interfaces import *
from sd.contents.interfaces import *


class DocumentChaptering(BaseStructuredContentProvider):
    """A content provider serving chapters.
    """
    implements(IStructuredDocumentChaptering)
    adapts(IStructuredDocument, IBrowserRequest, IStructuredDocumentView)

    template = ViewPageTemplateFile("browser/templates/chaptering.pt")

    def render(self):
        chapters = list()
        for chapter in self.chapters:
            name = IDynamicStructuredChapter(chapter).sd_layout
            renderer = queryMultiAdapter((chapter, self.request),
                                         IChapterRenderer,
                                         name = name)
            if renderer:
                chapters.append(renderer)

        return self.template(chapters = chapters)

    @property
    def chapters(self):
        return self.__parent__.contents(full_objects=True)


class DocumentParagraphing(BaseStructuredContentProvider):
    """A content provider serving paragraphs.
    """
    implements(IStructuredDocumentParagraphing)
    adapts(IStructuredChapter, IBrowserRequest, IStructuredChapterView)

    template = ViewPageTemplateFile("browser/templates/paragraphing.pt")

    def render(self):
        paragraphs = list()
        for paragraph in self.paragraphs:
            name = IDynamicStructuredParagraph(paragraph).sd_layout
            renderer = queryMultiAdapter((paragraph, self.request),
                                         IParagraphRenderer,
                                         name = name)
            if renderer:
                paragraphs.append(renderer)

        return self.template(paragraphs = paragraphs)

    @property
    def paragraphs(self):
        return self.__parent__.contents(full_objects=True)


# Registering content providers
provideAdapter(DocumentChaptering,
               provides=IStructuredDocumentChaptering,
               name=u"sd.chaptering")

provideAdapter(DocumentParagraphing,
               provides=IStructuredDocumentParagraphing,
               name=u"sd.paragraphing")
