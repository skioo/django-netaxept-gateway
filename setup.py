#!/usr/bin/env python
from setuptools import setup

import netaxept

setup(
    name='django-netaxept-gateway',
    version=netaxept.__version__,
    install_requires=[
        'Django>=1.8',
        'structlog',
        'suds2',
        'requests',
    ],
    packages=[
        'netaxept',
        'netaxept.migrations',
        'netaxept.actions',
        'netaxept.views',
    ],
    package_data={'netaxept': [
        'templates/admin/netaxept/*.html',
        'templates/netaxept/example/*.html',
    ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
