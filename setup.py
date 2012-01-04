#!/usr/bin/env python

import os
from glob import glob

if os.environ.get('USE_SETUPTOOLS'):
    from setuptools import setup
    setup_kwargs = dict(zip_safe=0)
else:
    from distutils.core import setup
    setup_kwargs = dict()

data_files=[
    ('/etc/diamond',                           glob('conf/*.conf*') ),
    ('/etc/diamond/collectors',                glob('conf/collectors/*') ),
    ('share/diamond/collectors',               glob('test.py') ),
    ('share/diamond/collectors',               glob('src/collectors/*.py') ),
    ('share/diamond/collectors/user_scripts',  [] ),
]

setup(
    name            = 'diamond',
    version         = '0.2.0',
    url             = 'https://github.com/BrightcoveOS/Diamond',
    author          = 'The Diamond Team',
    author_email    = 'https://github.com/BrightcoveOS/Diamond',
    license         = 'MIT License',
    description     = 'Smart data producer for graphite graphing package',
    package_dir     = {'' : 'src'},
    packages        = ['diamond'],
    scripts         = glob('bin/*'),
    data_files      = data_files,
    **setup_kwargs
)