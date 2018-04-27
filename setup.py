# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='check_systemdservices',
    packages=find_packages(),
    version='1.3.0',
    scripts=['bin/check_systemdservices'],
    install_requires=[
        'nagiosplugin>=1.2',
    ],
    description='A simple nagios plugin that detects failed systemd units.',
    author='Daniel Krämer',
    author_email='dakr@luitzifa.de',
    url='https://github.com/luitzifa/check_systemdservices',
    download_url='https://github.com/luitzifa/check_systemdservices/tarball/v1.3.0',
    keywords=['nagios', 'systemd'],
    license='GNU LGPL v2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Networking :: Monitoring'
    ],
)
