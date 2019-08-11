#
# A setuptools based setup module.
#


import os

from setuptools import setup, find_packages


def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()


setup(
    name='gameTitle',
    version='0.0.0-dev',

    description='A utility to rename ROM game files.',
    long_description=_read('README.md'),
    url='https://github.com/caedus75/gameTitle',

    author='Carlos Millett',
    author_email='carlos4735@gmail.com',

    license='MIT',

    packages=find_packages('src'),

    package_dir={'': 'src'},

    scripts=[
        'bin/gameTitle'
    ],

    keywords='utility rename rom games',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    python_requires='>=3.5'
)
