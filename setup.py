from distutils.core import setup

import re
versionLine = open("maxims/_version.py", "rt").read()
match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", versionLine, re.M)
versionString = match.group(1)

setup(name='maxims',
      version=versionString,
      description='A set of tools and reusable items for Axiom',
      url='https://github.com/lvh/maxims',

      author='Laurens Van Houtven',
      author_email='_@lvh.io',

      packages=["maxims", "maxims.contrib", "maxims.test"],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)",
        ]
)
