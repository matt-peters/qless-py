#! /usr/bin/env python

try:
	from setuptools import setup
	extra = {
		'install_requires' : ['argparse']
	}
except ImportError:
	from distutils.core import setup
	extra = {
		'dependencies' : ['argparse']
	}

setup(name               = 'qless-py',
	version              = '0.0.1',
	description          = 'Redis Queue Management',
	long_description     = '''
    Redis-based queue management, with heartbeating, job tracking,
    stats, and a whole lot more.
    ''',
	url                  = 'http://github.com/seomoz/qless-py',
	author               = 'Dan Lecocq',
	author_email         = 'dan@seomoz.org',
    license              = "MIT License",
	keywords             = 'redis, qless, job',
	packages             = ['qless'],
	package_dir          = {'qless': 'qless'},
    package_data         = {'qless': ['qless-core/*.lua']},
    include_package_data = True,
	classifiers          = [
        'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent'
	],
	**extra
)
