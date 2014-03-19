"""
djinga
Unobtrusive jinja2 integration in Django
(c) 2014 Thomas Khyn
MIT license (see LICENSE.txt) unless otherwise stated in file header
"""

from distutils.core import setup
import os

INC_PACKAGES = 'djinga',  # string or tuple of strings
EXC_PACKAGES = ()  # tuple of strings

install_requires = (
  'django>=1.6',
  'jinja2'
)
setup_requires = (
)


# imports __version__ variable
exec(open('djinga/version.py').read())

# setup function parameters
metadata = dict(
    name='djinga',
    version=__version__,
    description='Unobtrusive jinja2 integration in Django',
    author='Thomas Khyn',
    author_email='thomas@ksytek.com',
    url='http://open.ksytek.com/djinga/',  # TODO: check url
    keywords=['django', 'jinja2'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Environment :: Other Environments',
        'Topic :: Software Development',
        'Topic :: Text Editors :: Text Processing',
    ]
)


# packages parsing from root packages, without importing sub-packages
root_path = os.path.dirname(__file__)
if isinstance(INC_PACKAGES, basestring):
    INC_PACKAGES = (INC_PACKAGES,)

packages = []
excludes = list(EXC_PACKAGES)
for pkg in INC_PACKAGES:
    pkg_root = os.path.join(root_path, *pkg.split('.'))
    for dirpath, dirs, files in os.walk(pkg_root):
        rel_path = os.path.relpath(dirpath, pkg_root)
        pkg_name = pkg
        if (rel_path != '.'):
            pkg_name += '.' + rel_path.replace(os.sep, '.')
        for x in excludes:
            if x in pkg_name:
                continue
        if '__init__.py' in files:
            packages.append(pkg_name)
        elif dirs:  # stops package parsing if no __init__.py file
            excludes.append(pkg_name)


def read(filename):
    return open(os.path.join(root_path, filename)).read()

setup(**dict(metadata,
   packages=packages,
   long_description=read('README.txt'),  # use reST in README.txt !
   install_requires=install_requires,
   setup_requires=setup_requires
))
