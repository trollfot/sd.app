# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.formlib.form import Fields
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base

from sd import _
from sd.common.portlets.base import BasePortletRenderer
from interfaces import ITableOfContents


class TableOfContents(base.Assignment):
    """A portlet displaying the table of the document contents.
    """
    implements(ITableOfContents)

    def __init__(self, name, display_description):
        super(TableOfContents, self).__init__(name, display_description)
        self.name = name
        self.display_description = display_description

    @property
    def title(self):
        return self.name


class AddForm(base.AddForm):
    """Table of contents block add form
    """
    form_fields = Fields(ITableOfContents)

    def create(self, data):
        toc = TableOfContents(**data)
        return toc


class EditForm(base.EditForm):
    """ToC block edit form
    """
    label = _(u"Edit table of contents block")
    description = _(u"This form allow you to edit your table of contents.")
    form_fields = Fields(ITableOfContents)


class Renderer(BasePortletRenderer):
    """Browser view to render a ToC
    """
    render = ViewPageTemplateFile('templates/toc.pt')

    def entries(self):
        return self.__parent__.contents()

    @property
    def display_description(self):
        return self.data.display_description
