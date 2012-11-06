from distutils.core import setup

setup(name='maxims',
      version='20121107',
      description='A set of tools and reusbale items for Axiom',
      url='https://github.com/lvh/maxims',

      author='Laurens Van Houtven',
      author_email='_@lvh.cc',

      packages=["maxims", "maxims.contrib", "maxims.test"],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)",
        ]
)

