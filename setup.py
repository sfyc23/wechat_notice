#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: wechat-notice
Creator: DoubleThunder
Create time: 2019-10-06 00:33
Introduction:
"""

import io
import os
from setuptools import setup, Command
import sys
from shutil import rmtree

NAME = 'wechat_notice'
DESCRIPTION = 'Send Wechat a message at any time.'
URL = 'https://github.com/sfyc23/wechat_notice'
EMAIL = 'sfyc23@gmail.com'
AUTHOR = 'DoubleThunder'
VERSION = '0.0.03'


# What packages are required for this module to be executed?
REQUIRED = [
    'requests', 'yagmail'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

current_dir = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

packages = [
    'wechat_notice',
]

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            # delete update cache.
            rmtree(os.path.join(current_dir, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Publishing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')

        sys.exit()



# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT',
    python_requires='>=3.6.0',
    url=URL,

    # packages=packages,
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    py_modules=['wechat_notice'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,

    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords='wechat, 微信, notice, 通知',
    # cmdclass={
    #         'upload': UploadCommand,
    # },
)




