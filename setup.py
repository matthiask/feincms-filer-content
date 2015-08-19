#!/usr/bin/env python

from os.path import dirname, join
from setuptools import setup, find_packages

setup(
    name='feincms-filer-content',
    packages=find_packages(),
    include_package_data=True,
    version=__import__('mediafiler').__version__,
    description='A FeinCMS contenttype package for django-filer',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='Simon Baechler',
    author_email='sb@feinheit.ch',
    url='https://github.com/sbaechler/feincms-filer-content',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
