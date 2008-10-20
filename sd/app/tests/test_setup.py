# -*- coding: utf-8 -*-

import unittest
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase import PloneTestCase as ptc
from sd.app.tests import base


class TestSetup(ptc.PloneTestCase):

    types = ('StructuredDocument',
             'SimpleParagraph')

    def testPortalTypes(self):
        portal_types = self.portal.portal_types.objectIds()
        for content_type in self.types:
            self.failUnless(content_type in portal_types)

    def testPortalFactorySetup(self):
        portal_factory = getToolByName(self.portal, 'portal_factory') 
        factoryTypes = portal_factory.getFactoryTypes().keys()
        for content_type in self.types:
            self.failUnless(content_type in factoryTypes)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
