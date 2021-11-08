#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = '''A Python implementation of a 2048 bit hash function based
on the the AES (FIPS-197) block-cipher algorithm and the most common mode of
operation (CBC) with no dependencies beyond standard Python libraries and pyaes.
See README.md for API reference and details.'''

setup(name = 'haesh',
      version = '0.0.1',
      description = 'Python Implementation of a hash function based on the AES block-cipher in the CBC mode of operation',
      long_description = LONG_DESCRIPTION,
      author = 'Vincent Asante',
      author_email = 'vincenthokie@gmail.com',
      url = 'https://github.com/VincentHokie/haesh',
      packages = ['haesh'],
      classifiers = [
          'Topic :: Security :: Cryptography',
          'License :: OSI Approved :: MIT License',
      ],
      license = "License :: OSI Approved :: MIT License",
     )
