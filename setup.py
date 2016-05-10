from setuptools import setup, find_packages
import sys, os

setup(name=u'mapclientplugins.fieldworklowerlimb2sidegenerationstep',
      version='0.0',
      description='',
      long_description="",
      classifiers=[],
      author=u'Ju Zhang',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup',]),
      namespace_packages=['mapclientplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'numpy',
          'scipy',
          'mayavi[app]'.
      ],
      )
