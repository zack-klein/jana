import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="jana",
    author="Zack Klein",
    author_email="klein.zachary.j@gmail.com",
    description=("An easy way to use secrets in (several of) the cloud(s)."),
    license="MIT",
    packages=["jana"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    url="https://github.com/zack-klein/jana",
    install_requires=requirements,
)
