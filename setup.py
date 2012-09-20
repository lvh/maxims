from distutils.core import setup

setup(name='maxims',
      version='0',
      description='A set of reusable Axiom items',
      url='https://github.com/lvh/maxims',

      author='Laurens Van Houtven',
      author_email='_@lvh.cc',

      packages=["maxims", "maxims.test"],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)",
        ]
)
