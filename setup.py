import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="jabba",
    author="Zack Klein",
    author_email="klein.zachary.j@gmail.com",
    description=("An easy way to use secrets in (several of) the cloud(s)."),
    license="MIT",
    packages=["jabba"],
    long_description=read("README.md"),
    setup_requires=["setuptools_scm"],
)
