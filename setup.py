#!/usr/bin/env python
from __future__ import unicode_literals

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

metadata = {}

here = os.path.abspath(os.path.dirname(__file__))

NAME = "autosub"

with open(os.path.join(here, NAME, "metadata.py")) as metafile:
    exec(metafile.read(), metadata)

setup(
    name=metadata['NAME'],
    version=metadata['VERSION'],
    description=metadata['DESCRIPTION'],
    long_description=metadata['LONG_DESCRIPTION'],
    author=metadata['AUTHOR'],
    author_email=metadata['AUTHOR_EMAIL'],
    url=metadata['HOMEPAGE'],
    packages=[str('autosub')],
    entry_points={
        'console_scripts': [
            'autosub = autosub:main',
        ]
    },
    package_data={str('autosub'): [str('data/locale/zh_CN/LC_MESSAGES/*mo')]},
    install_requires=[
        'requests>=2.3.0',
        'pysubs2>=0.2.4',
        'progressbar2>=3.34.3',
        'auditok>=0.1.5',
        'googletrans>=2.4.0',
        'langcodes-py2>=1.2.0',
        'wcwidth>=0.1.7',
        'google-cloud-speech>=1.3.1'
    ],
    license=open(os.path.join(here, "LICENSE")).read()
)
