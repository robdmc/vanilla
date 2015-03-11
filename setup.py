# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = 'brain/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='vanilla',
    version=get_version(),
    description='Plain vanilla dango project',
    long_description='plain vanilla project',
    url='',
    author='Rob deCarvalho',
    author_email='rob.decarvalho@ambition.com',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Private :: Do Not Upload',
    ],
    install_requires=[
        'django>=1.6.5,<1.7',
        'numpy>=1.8.0',
        'pandas>=0.14.0',
        'django-manager-utils>=0.7.1'
    ],
    tests_require=[
    ],
    #test_suite='run_tests.run_tests',
    include_package_data=True,
    zip_safe=False,
)
