# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import re
from setuptools import setup, find_packages

setup(
    name='vanilla',
    version='0.1',
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
        'django',
        'numpy',
        'scipy',
        'pandas>=0.14.0',
        'django-manager-utils>=0.7.1',
        'django-extensions',
        'jinja2',
        'pyzmq',
        'tornado',
        'ipython',
        'jsonschema',
        'matplotlib',
        'seaborn',
        'statsmodels',
    ],
    tests_require=[
    ],
    include_package_data=True,
    zip_safe=False,
)
