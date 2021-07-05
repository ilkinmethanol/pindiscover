from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "src/README.md").read_text()
# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'src/requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
    install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and ( not x.startswith('#')) and (not x.startswith('-'))]

setup(
    name='pingdiscover',
    version='1.0.0',
     description = 'A simple commandline app for ip lookup with concurrent processes',
     python_requires='>=3.7',
     author="Ilkin Mammadov",
     long_description=README,
     long_description_content_type="text/markdown",
     license='MIT',
      author_email='ilkma1998@gmail.com',
      classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
        ],
    packages=find_packages(include=['src', 'src.*']),
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['pingdiscover=src.pingdiscover:main']
    },
)




