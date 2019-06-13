from setuptools import setup, find_packages
import phoopy.http

long_description = open('README.rst', 'r').read()

setup(
    name='phoopy-http',
    version=phoopy.http.__version__,
    packages=find_packages(),
    package_data={
        'phoopy.http.http_bundle': ['config/*.yml'],
    },
    setup_requires=['wheel'],
    install_requires=[
        'CherryPy>=18.1.0',
        'Flask>=1.0.0',
    ],
    description="Http library for phoopy framework",
    long_description=long_description,
    url='https://github.com/phoopy/phoopy-http',
    author='Phoopy',
    author_email='reisraff@gmail.com',
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
