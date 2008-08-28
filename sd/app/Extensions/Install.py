import transaction
from Products.CMFCore.utils import getToolByName

PRODUCT_DEPENDENCIES = tuple()
EXTENSION_PROFILES = ('sd.app:default',)
UNINSTALL_PROFILES = ('sd.app:uninstall',)

def install(self, reinstall=False):
    """Inspired of 'oi.plum'. It will install the product
    and all its dependencies. It will apply the dedicated
    profile.
    """
    portal_quickinstaller = getToolByName(self, 'portal_quickinstaller')
    portal_setup = getToolByName(self, 'portal_setup')

    for product in PRODUCT_DEPENDENCIES:
        is_installed = portal_quickinstaller.isProductInstalled(product)
        
        if reinstall and is_installed:
            portal_quickinstaller.reinstallProducts([product])
            transaction.savepoint()
            
        elif not is_installed:
            portal_quickinstaller.installProduct(product)
            transaction.savepoint()
        
    for extension_id in EXTENSION_PROFILES:
        portal_setup.runAllImportStepsFromProfile('profile-%s' % extension_id,
                                                  purge_old=False)
        product_name = extension_id.split(':')[0]
        portal_quickinstaller.notifyInstalled(product_name)
        transaction.savepoint()

    return "Ran all install steps for."


def uninstall(self):
    """This uninstaller will only apply the GS uninstallation
    profiles. There can be more than one, so we keep the loop.
    """
    portal_setup = getToolByName(self, 'portal_setup')
    for extension_id in UNINSTALL_PROFILES:
        portal_setup.runAllImportStepsFromProfile('profile-%s' % extension_id,
                                                  purge_old=False)
        transaction.savepoint()
        
    return "Ran all uninstall steps for."
