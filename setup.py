from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-helloworld',
	version=version,
	description="Testing the waters...",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Ryan Clark',
	author_email='ryan.clark.j@gmail.com',
	url='',
	license='MIT',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.helloworld'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
	[ckan.plugins]
	helloworld=ckanext.helloworld.plugin:HelloWorldPlugin
	""",
)
