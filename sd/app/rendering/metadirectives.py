# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from zope.configuration import fields as configuration_fields


class IStructuredRendererDirective(Interface):

    targets = configuration_fields.Tokens(
        title=u"Content type type interface",
        description=u"Should correspond to the interface of the content type.",
        value_type=configuration_fields.GlobalInterface(),
        required=True)

    filtering = schema.TextLine(
        title=u"Content types interfaces filtering",
        description=u"Should correspond to the dotted name of an interface.",
        required=False)

    name = configuration_fields.PythonIdentifier(
        title=u"Name",
        description=u"The name of the renderer",
        required=False)

    description = schema.TextLine(
        title=u"Description",
        description=u"The detailed name of the renderer",
        required=False)
    
    renderer = configuration_fields.GlobalObject(
        title=u"The class used to render the item.",
        description=u"A class.",
        required=False)

    template = configuration_fields.Path(
        title=u"The name of a template.",
        description=u"The template used to display the renderer.",
        required=False
        )

    macro = configuration_fields.PythonIdentifier(
        title=u"Macro",
        description=u"The name of the macro that is to be rendered",
        required=False)
    
    folderish = schema.Bool(
        title=u"Defines if the renderer should provide folder's utilities",
        required=False
        )
