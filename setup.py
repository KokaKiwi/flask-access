#!/usr/bin/env python
'''
Flask-Access
------------

A Flask extension for Access Control Lists (inspired by Flask-ACL)
'''
from setuptools import setup, find_packages

REQUIREMENTS = [
    'Flask',
]
EXTRA_REQUIREMENTS = {
    'Login': ['Flask-Login'],
}


setup(
    name='Flask-Access',
    version='0.1.0',
    author='KokaKiwi',
    author_email='kokakiwi+py@kokakiwi.net',
    license='MIT',
    description='A Flask extension for Access Control Lists',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',

    install_requires=REQUIREMENTS,
    extras_require=EXTRA_REQUIREMENTS,
)
