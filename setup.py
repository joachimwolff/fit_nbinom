#!/usr/bin/env python

from setuptools import setup

install_requires_py = ["numpy >= 1.15.*",
                       "scipy >= 1.2.*"
                       ]

setup(
    name='fit_nbinom',
    version=1.1,
    author='Gökçen Eraslan, Joachim Wolff',
    author_email='wolffj@informatik.uni-freiburg.de',
    packages=['fit_nbinom'],

    url='https://github.com/joachimwolff/fit_nbinom',
    license='LICENSE.md',
    description='Negative binomial maximum likelihood estimator.',
    long_description=open('README.md').read(),
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics'],
    install_requires=install_requires_py,
)
