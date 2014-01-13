#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import glob
import os
import sys

import ah_bootstrap
ah_bootstrap.use_astropy_helpers()

from setuptools import setup

#A dirty hack to get around some early import/configurations ambiguities
if sys.version_info[0] >= 3:
    import builtins
else:
    import __builtin__ as builtins
builtins._ASTROPY_SETUP_ = True

from astropy_helpers.setup_helpers import (register_commands, adjust_compiler,
                                           get_debug_option)
from astropy_helpers.version_helpers import generate_version_py
from astropy_helpers.git_helpers import get_git_devstr

# Set affiliated package-specific settings
PACKAGEFULLNAME = 'APLpy'
PACKAGENAME = 'aplpy'
DESCRIPTION = 'The Astronomical Plotting Library in Python'
LONG_DESCRIPTION = ''
AUTHOR = 'Thomas Robitaille and Eli Bressert'
AUTHOR_EMAIL = 'thomas.robitaille@gmail.com, elibre@users.sourceforge.net'
LICENSE = 'MIT'
URL = 'http://aplpy.github.com'

# VERSION should be PEP386 compatible (http://www.python.org/dev/peps/pep-0386)
VERSION = '0.9.12.dev'

# Indicates if this version is a release version
RELEASE = 'dev' not in VERSION

if not RELEASE:
    VERSION += get_git_devstr(False)

# Populate the dict of setup command overrides; this should be done before
# invoking any other functionality from distutils since it can potentially
# modify distutils' behavior.
cmdclassd = register_commands(PACKAGENAME, VERSION, RELEASE)

# Adjust the compiler in case the default on this platform is to use a
# broken one.
adjust_compiler(PACKAGENAME)

# Freeze build information in version.py
generate_version_py(PACKAGENAME, VERSION, RELEASE, get_debug_option(PACKAGENAME))

# Treat everything in scripts except README.rst as a script to be installed
scripts = [fname for fname in glob.glob(os.path.join('scripts', '*'))
           if os.path.basename(fname) != 'README.rst']


from astropy_helpers.setup_helpers import get_package_info

# Get configuration information from all of the various subpackages.
# See the docstring for setup_helpers.update_package_files for more
# details.
package_info = get_package_info(PACKAGENAME)

# Add the project-global data
package_info['package_data'][PACKAGENAME] = ['data/*']

setup(name=PACKAGEFULLNAME,
      version=VERSION,
      description=DESCRIPTION,
      scripts=scripts,
      requires=['astropy', 'numpy', 'matplotlib'],
      provides=[PACKAGENAME],
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      long_description=LONG_DESCRIPTION,
      cmdclass=cmdclassd,
      zip_safe=False,
      use_2to3=True,
      classifiers=[
                   "Development Status :: 4 - Beta",
                   "Programming Language :: Python",
                   "License :: OSI Approved :: MIT License",
                  ],
      **package_info
)
