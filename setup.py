from setuptools import setup, find_packages

setup(
   name='FighterGame',
   version='0.1.0',
   author='NSI Team',
   author_email='XXXX@saint-louis29.net',
   license='LICENSE.txt',
   description='An awesome fighter game',
   long_description=open('README.md').read(),
   install_requires=[
       "pytest",
   ],

    packages=find_packages(
        where='src',
    ),
    package_dir={"": "src"}

)