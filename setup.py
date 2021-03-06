#!/usr/bin/env python

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    args = ['--doctest-module', './cdx_toolkit', './tests/unit']
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]
    # python ./setup.py --pytest-args='-v -v'

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.args = PyTest.args.copy()
        self.pytest_args = ''

    def finalize_options(self):
        TestCommand.finalize_options(self)

    def run_tests(self):
        import pytest
        import shlex
        if self.pytest_args:
            self.args.extend(shlex.split(self.pytest_args))
        errno = pytest.main(self.args)
        sys.exit(errno)


packages = [
    'cdx_toolkit',
]

requires = ['requests', 'warcio']

test_requirements = ['pytest>=3.0.0']  # 'coverage', 'pytest-cov']

scripts = ['scripts/cdx_size', 'scripts/cdx_iter']

try:
    import pypandoc
    description = pypandoc.convert_file('README.md', 'rst')
except (IOError, ImportError):
    description = open('README.md').read()

setup(
    name='cdx_toolkit',
    use_scm_version=True,
    description='A toolkit for working with CDX indices',
    long_description=description,
    author='Greg Lindahl and others',
    author_email='lindahl@pbm.com',
    url='https://github.com/cocrawler/cdx_toolkit',
    packages=packages,
    setup_requires=['setuptools_scm'],
    install_requires=requires,
    scripts=scripts,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
)
