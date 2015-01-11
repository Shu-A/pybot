from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name        = 'pybot',
    version     = '0.1.0',
    packages    = [
        'src.pybot',
    ],

    description = 'Pybot project',
    long_description = long_description,

    url         = 'https://github.com/byforce/pybot',
    author      = 'Shuichiro Aiba',
    author_email= 'shuichiro.aiba@gmail.com',

    license     = 'MIT',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    install_requires = open('requirements.txt').read().splitlines(),

    scripts = [
        'bin/pybot',
    ],

)
