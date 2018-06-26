from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), "README.rst"), encoding="utf-8") as handle:
    readme = handle.read()

setup(
    name="siphash-cffi",
    version="0.1.3",
    description="Tested, performant SipHash bindings for Python 3 with support for double-output-size, half-word and variable-round variants.",
    long_description=readme,
    url="https://github.com/kpdemetriou/siphash-cffi",
    author="Phil Demetriou",
    author_email="inbox@philonas.net",
    license="BSD",
    packages=find_packages(exclude=["tests"]),
    setup_requires=["cffi>=1.4.0"],
    cffi_modules=[
        "build.py:siphash_ffi",
        "build.py:siphash_variable_ffi",
        "build.py:halfsiphash_ffi",
        "build.py:halfsiphash_variable_ffi",
    ],
    install_requires=["cffi>=1.4.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: C",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
    ],
)
