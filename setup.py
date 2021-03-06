#! /usr/bin/env python

"""TODO: Maybe add a docstring containing a long description

  This would double as something we could put int the `long_description`
  parameter for `setup` and it would squelch some complaints pylint has on
  `setup.py`.

"""

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='demandlib',
      version='0.1.2dev',
      author='oemof developer group',
      url='https://oemof.org/',
      license='GPL3',
      author_email='oemof@rl-institut.de',
      description='Demandlib of the open energy modelling framework',
      long_description=read('README.rst'),
      packages=find_packages(),
      install_requires=['numpy >= 1.7.0, <= 1.14.2',
                        'pandas >= 0.18.0, <= 0.22'],
      )
