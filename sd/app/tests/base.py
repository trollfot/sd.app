# -*- coding: utf-8 -*-

from Testing.ZopeTestCase import installPackage
from Products.Five import zcml, fiveconfigure
from Products.PloneTestCase.PloneTestCase import setupPloneSite
from Products.PloneTestCase.layer import onsetup


@onsetup
def setup_product():
    """Setting up the package and including the ZCML
    """
    import sd.app
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', sd.app)
    fiveconfigure.debug_mode = False
    installPackage('sd.app')


setup_product()
setupPloneSite(products=('sd.app',))
