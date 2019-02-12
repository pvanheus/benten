import pathlib
from datetime import datetime
from setuptools import setup, find_packages

current_path = pathlib.Path(__file__).parent

name = 'benten'
ver_path = pathlib.Path(current_path, "benten", "version.py")
version = ver_path.open("r").read().split("=")[1].strip().replace("\"", "")
now = datetime.utcnow()
desc_path = pathlib.Path(current_path, "Readme.md")
long_description = desc_path.open("r").read()

setup(
    name=name,
    version=version,
    packages=find_packages(),
    platforms=['POSIX', 'MacOS', 'Windows'],
    python_requires='>=3.7.0',
    install_requires=[
        "pyyaml",
        "PySide2",
        "pygraphviz"  # For the "dot" layout algorithm
    ],
    entry_points={
        'console_scripts': [
            'benten = benten.guimain:main'
        ],
    },

    author='Seven Bridges Genomics Inc.',
    maintainer='Seven Bridges Genomics Inc.',
    maintainer_email='kaushik.ghose@sbgenomics.com',
    author_email='kaushik.ghose@sbgenomics.com',
    description='SBG Python tool to assist hand coding of CWL workflows',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    license='Copyright (c) {} Seven Bridges Genomics'.format(now.year),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
    ],
    keywords='seven bridges cwl common workflow language'
)