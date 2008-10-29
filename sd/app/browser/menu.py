# -*- coding: utf-8 -*-

from five import grok
from interfaces import IStructuredMenu, Interface, IStructuredSubMenu
from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from zope.app.publisher.browser import menu
from zope.cachedescriptors.property import CachedProperty
from plone.app.contentmenu.interfaces import IContentMenuItem
from sd.contents import interfaces as sdct

_ = MessageFactory("sd")


class ActionsSubMenuItem(grok.MultiAdapter, menu.BrowserSubMenuItem):
    grok.implements(IStructuredSubMenu)
    grok.name("sd.contentmenu.options")
    grok.adapts(Interface, Interface)
    grok.provides(IContentMenuItem)

    order = 5
    extra = {'id': 'sd-contentmenu-options'}
    submenuId = 'sd_contentmenu_options'

    title = _(u'label_sd_contentmenu_options',
              default=u'Structured Document')
    
    description = _(u'title_sd_contentmenu_options',
                    default=u'Options altering the content behavior.')

    @CachedProperty
    def action(self):
        return self.context.absolute_url() + '/@@sd.preferences'

    def available(self):
        if not sdct.IPossibleBatchProvider.providedBy(self.context):
            return False

        if self.context.portal_type == 'StructuredDocument':
            return False
        
        return True

    def selected(self):
        return False



class StructuredDocumentOptions(menu.BrowserMenu):

    implements(IStructuredMenu)

    def getMenuItems(self, context, request):
        """Return menu item entries in a TAL-friendly form."""

        results = []
        url = context.absolute_url()
        can_tag = not sdct.IStructuredDocument.providedBy(context)
        can_untag = not can_tag
        
        if can_tag:
            results.append(
                { 'title' : "Mark as a structured document",
                  'description' : 'Mark the content as a structured document',
                  'action' : "%s/@@sd.tagging" % url,
                  'selected' : False,
                  'icon' : u"",
                  'extra' : {'id': 'sd_tag',
                             'separator': None,
                             'class': ''
                             },
                  'submenu'     : None,
                  }
                )
        else:
            layout = context.getLayout()
            results.append(
                { 'title' : "Remove structured document options",
                  'description' : 'Restore the content normal behavior',
                  'action' : "%s/@@sd.untagging" % url,
                  'selected' : False,
                  'icon' : u"",
                  'extra' : {'id': 'sd_untag',
                             'separator': None,
                             'class': ''
                             },
                  'submenu'     : None,
                  }
                )
                
            results.append(
                { 'title' : "Document on one page",
                  'description' : 'Change the display of the document',
                  'action' : ("%s/@@sd.options?layout=@@sd.document.onepage"
                              % url),
                  'selected' : layout == '@@sd.document.onepage',
                  'icon' : u"",
                  'extra' : {'id': 'sd_document_onepage',
                             'separator': 'actionSeparator',
                             'class': ''
                             },
                  'submenu': None,
                  }
                )
        return results

        
