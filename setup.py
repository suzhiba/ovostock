#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'Click==6.6'
]

test_requirements = [
    # TODO: put package test requirements here
    'unittest2==1.1.0'
]

setup(
    name='ovostock',
    version='0.1.0',
    description="ovoStock is a Machine Learning toolkit for making stock market predictions.",
    long_description=readme + '\n\n' + history,
    author="Kevin Jacobs",
    author_email='kevin91nl@gmail.com',
    url='https://github.com/kevin91nl/ovostock',
    packages=[
        'ovostock',
    ],
    package_dir={'ovostock':
                 'ovostock'},
    entry_points={
        'console_scripts': [
            'ovostock=ovostock.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ovostock',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
