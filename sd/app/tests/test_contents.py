# -*- coding: utf-8 -*-

import unittest
from Products.PloneTestCase import PloneTestCase as ptc
from Products.CMFPlone.utils import _createObjectByType
from sd.app.tests import base


class TestContentsBasics(ptc.PloneTestCase):
    """Test the basics, like creation
    """
    def afterSetUp(self):
        """This method is called before each single test.
        """
        pass

    def beforeTearDown(self):
        """This method is called after each single test.
        """
        pass
    
    def testStructuredDocumentCreation(self):
        """Try creating and deleting a very simple architecture
        """
        # Creating a Structured Document
        doc_id = 'sd'
        doc = _createObjectByType('StructuredDocument', self.portal, doc_id)
        self.failIfEqual(doc, None)
        self.failUnless(doc_id in self.portal.objectIds())

        # Cleaning the portal
        self.portal._delObject(doc_id)
        self.failIf(doc_id in self.portal.objectIds())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestContentsBasics))
    return suite
