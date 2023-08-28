import codecs
import io
import os
import re

from setuptools import setup, find_packages

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*parts):
    with codecs.open(os.path.join(SETUP_DIR, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


package_readme = readfile("README.md", split=True)[3:]  # skip title
package_license = readfile("LICENSE")
package_dependencies = [
    "setuptools",
    "numpy",
    "gias3.mapclientpluginutilities",
    "gias3.fieldwork",
    "gias3.musculoskeletal",
    "musculoskeletal-models",
    "PySide6"
]

setup(
    name=u'mapclientplugins.fieldworklowerlimb2sidegenerationstep',
    version=find_version('mapclientplugins', 'fieldworklowerlimb2sidegenerationstep', '__init__.py'),
    description='',
    long_description='\n'.join(package_readme) + package_license,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
    ],
    author=u'Ju Zhang',
    author_email='',
    url='https://github.com/mapclient-plugins/fieldworklowerlimb2sidegenerationstep',
    license='APACHE',
    packages=find_packages(exclude=['ez_setup', ]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    package_data=package_data,
    zip_safe=False,
    install_requires=package_dependencies,
)
