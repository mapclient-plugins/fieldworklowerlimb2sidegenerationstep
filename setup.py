from setuptools import setup, find_packages
import io


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
    "gias2",
    "PySide2"
]
package_data = {
    'mapclientplugins.fieldworklowerlimb2sidegenerationstep': [
        'data/atlas_meshes/*',
        'data/shape_models/*',
    ],
}

setup(name=u'mapclientplugins.fieldworklowerlimb2sidegenerationstep',
      version='1.0.3',
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
