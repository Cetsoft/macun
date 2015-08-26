import sys
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


install_pip_reqs = parse_requirements("requirements.txt", session=PipSession())
install_reqs = [str(install_req.req) for install_req in install_pip_reqs]

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='macun',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='',
    long_description='',

    # The project's main homepage.
    url='https://github.com/Cetsoft/macun',

    # Author details
    author='macun-team',

    # Choose your license
    license='Apache',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='macun development',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    setup_requires=[
        "flake8"
    ],

    install_requires=install_reqs,

    tests_require=['pytest'],
    
    extras_require={
        'dev': [],
        'test': ['coverage'],
    },

    cmdclass = {'test': PyTest}
)