#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='dht22',
      version='1.0',
      url='https://github.com/Jeremie-C/python_OPi_dht22',
      author='Jeremie-C',
      description='Python DHT22 Library for OrangePi.',
      packages=['dht22'],
      long_description=open('README.md').read(),
      requires=['python (>= 2.7)'],
      classifiers=['Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Embedded Systems'
      ]
)
