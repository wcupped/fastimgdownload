from io import open
from setuptools import setup

"""
:authors: wCupped
:license: None
:copyright: (c) 2024 wCupped
"""

version = '1.1'
'''
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
'''

long_description = '''Python module that uses requests module to simplify the downloading of image'''

setup(
    name='fastimgdownload',
    version=version,

    author='wCupped',

    description=(
        u'Python module that uses requests module to simplify the downloading of image'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    license='None',

    packages=['fastimgdownload'],
    install_requires=['requests'],
)