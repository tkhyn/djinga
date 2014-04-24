"""
djinga
Unobtrusive jinja2 integration in Django
(c) 2014 Thomas Khyn
MIT license (see LICENSE.txt) unless otherwise stated in file header
"""

from setuptools import setup, find_packages
import os


# imports __version__ variable
exec(open('djinga/version.py').read())
dev_status = __version_info__[3]

if dev_status == 'alpha' and not __version_info__[4]:
    dev_status = 'pre'

DEV_STATUS = {'pre': '2 - Pre-Alpha',
              'alpha': '3 - Alpha',
              'beta': '4 - Beta',
              'rc': '5 - Production/Stable',
              'final': '5 - Production/Stable'}

# setup function parameters
setup(
    name='djinga',
    version=__version__,
    description='Unobtrusive jinja2 integration in Django',
    long_description=open(os.path.join('README.rst')).read(),
    author='Thomas Khyn',
    author_email='thomas@ksytek.com',
    url='http://bitbucket.org/tkhyn/djinga',
    keywords=['django', 'jinja2'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: %s' % DEV_STATUS[dev_status],
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Environment :: Other Environments',
        'Topic :: Software Development',
        'Topic :: Text Editors :: Text Processing',
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    package_data={
        '': ['LICENSE.txt', 'README.rst']
    },
    install_requires=(
      'django>=1.6',
      'jinja2'
    ),
    zip_safe=True,
)
