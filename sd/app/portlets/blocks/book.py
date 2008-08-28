# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.formlib.form import Fields
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from sd import _
from sd.imaging.portlet import *
from interfaces import IBookBlock


class Book(AssignmentWithImage):
    """A portlet representing a book.
    """
    implements(IBookBlock)

    def __init__(self, name, url, author=u"", publishing_year=u"",
                  caption=u"", serie=u"", tome=0, details=[], image=None):
        super(Book, self).__init__(name, url, caption, image)
        self.author = author
        self.tome = tome
        self.serie = serie
        self.publishing_year = publishing_year
        self.details = details


class AddForm(AddFormWithImage):
    """Book block add form
    """
    form_fields = Fields(IBookBlock)

    def create(self, data):
        return Book(**data)


class EditForm(EditFormWithImage):
    """Book block edit form
    """
    label = _(u"Edit book block")
    description = _(u"This form allow you to edit your book block.")
    form_fields = Fields(IBookBlock)


class Renderer(ImagePortletRenderer):
    """Browser view to render a book block
    """
    render = ViewPageTemplateFile('templates/book.pt')

    @property
    def details(self):
        return self.data.details

    @property
    def author(self):
        return self.data.author

    @property
    def publishing_year(self):
        return self.data.publishing_year

    @property
    def serie(self):
        return self.data.serie

    @property
    def tome(self):
        return self.data.tome
