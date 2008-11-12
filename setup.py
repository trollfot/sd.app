from setuptools import setup, find_packages
from os.path import join

name = 'sd.app'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()
readme = open("README.txt").read()
history = open(join('docs', 'HISTORY.txt')).read().replace(name + ' - ', '')

setup(name = name,
      version = version,
      description = 'Structured Document Plone Product',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'plone CMS zope structureddocument',
      author = 'Souheil Chelfouh',
      author_email = 'souheil@chelfouh.com',
      url = 'http://tracker.trollfot.org/wiki/StructuredDocument',
      download_url = 'http://pypi.python.org/pypi/sd.app',
      license = 'GPL',
      packages = find_packages(),
      namespace_packages = ['sd'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'setuptools',
          'sd.common >= 0.6.8',
          'sd.imaging >= 0.4',
          'sd.contents >= 1.0',
          'sd.rendering == 0.8',
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
