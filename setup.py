import os
import io
from setuptools import find_packages, setup

def extract_version():
    """
    Extracts version values from the main matplotlib __init__.py and
    returns them as a dictionary.
    """
    with open('catpy/__init__.py') as fd:
        for line in fd.readlines():
            if (line.startswith('__version__')):
                exec(line.strip())
    return locals()["__version__"]


setup(
    name="catpy",
    # Increase the version in catpy/__init__.py
    version=extract_version(),
    author="Greg Lamp",
    author_email="greg@yhathq.com",
    url="https://github.com/yhat/catpy/",
    license="BSD",
    packages=find_packages(),
    package_dir={"catpy": "catpy"},
    package_data={
        "catpy": [
            "data/*"
        ]
    },
    description="Categorical variable friendly pandas data frames",
    # run pandoc --from=markdown --to=rst --output=README.rst README.md
    long_description=io.open("README.rst", encoding='utf8').read(),
    install_requires=[
        "pandas"
    ],
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3'],
    zip_safe=False,
)

