# -*- coding: utf-8 -*-

from zope.schema import Int, List, TextLine, Choice, Bool
from zope.i18nmessageid import MessageFactory

from Products.ATContentTypes.interface import IATTopic
from Products.Archetypes.interfaces._base import IBaseFolder
from plone.app.vocabularies.catalog import SearchableTextSourceBinder

from sd.imaging.interfaces import IPortletWithImage
from sd.contents.interfaces import IStructuredBlock
from sd.app.forms.fields import TermField

_ = MessageFactory("sd")


class IStructuredIllustratedBlock(IStructuredBlock, IPortletWithImage):
    """A marker interface for structured blocks with an image field.
    """

class ICountryBlock(IStructuredIllustratedBlock):
    """A schema representing a country.
    """
    name = TextLine(
        title=_("Name of the country"),
        description=_(u"Name of the country in the site's language"),
        required = True
        )

    local_names = List(
        title = _(u"Local names"),
        description = _(u"The country name in other dialects or languages."),
        default = list(),
        value_type = TermField(),
        required = False
        )


class IPersonBlock(IStructuredIllustratedBlock):
    """A schema representing a person.
    """
    name = TextLine(
        title=_("Name of the person"),
        description=_(u"Fullname"),
        default=u"",
        required = True
        )

    details = List(
        title = _(u"Details"),
        description = _(u"Add more information"),
        default = list(),
        value_type = TermField(),
        required = False
        )


class ITableOfContents(IStructuredBlock):
    """A schema representing a table of contents.
    """
    name = TextLine(
        title=_("Title"),
        description=_(u"Title of the table of contents"),
        default=u"Table of contents",
        required = True
        )

    display_description = Bool(
        title = _(u"Display description"),
        description = _(u"Display the description of each item"),
        default = False,
        required = True
        )
    

class IBookBlock(IStructuredIllustratedBlock):
    """A schema representing a book.
    """
    name = TextLine(
        title=_("Title"),
        default=u"",
        required = True
        )

    author = TextLine(
        title=_("Author"),
        description=_(u"Name of the writer/author"),
        default=u"",
        required = False
        )

    publishing_year = TextLine(
        title=_("Year"),
        description=_(u"Year of first publishing"),
        default=u"",
        required = False
        )

    serie = TextLine(
        title=_("Serie"),
        description=_(u"The name of the serie of book"),
        default=u"",
        required = False
        )

    tome = Int(
        title=_("Tome"),
        description=_(u"The tome number"),
        default=1,
        required = False
        )

    details = List(
        title = _(u"Details"),
        description = _(u"Add more information"),
        default = list(),
        value_type = TermField(),
        required = False
        )


class ISlideshowPortlet(IStructuredBlock):
    """Slideshow portlet is based on collection portlet.
    """
    name = TextLine(
        title=_("Title"),
        default=u"",
        required = True
        )

    source = Choice(
        title = _(u"Target folder or topic"),
        description = _(u"Find the source which provides the pictures."),
        required = True,
        source = SearchableTextSourceBinder(
          {'object_provides' : (IATTopic.__identifier__,
                                IBaseFolder.__identifier__)},
          default_query = 'path:'
          )
        )

    timer = Int(
        title = _(u"timer", default=u"Timer (in seconds)"),
        description = _(u"timer_desc", default=u"The timer defines the time "
                        u"between each image. If the timer is set to 0, a "
                        u"click is needed to trigger the transition."),
        required = True
        )

    links = Bool(
        title = _(u"slideshow_links", default=u"Display next-previous links"),
        description = _(u"slideshow_links_desc", default=u"You can display "
                        "links to trigger manually the transition between "
                        u"each image can be triggered manually. "),
        required = False
        )

    size = Choice(
        title = _(u"Image size"),
        default = 'thumb',
        values = ['thumb', 'mini'],
        required = True,
        )
