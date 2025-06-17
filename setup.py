from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = (
    "A package to compute FES and their convergence using Mean Force Integration"
)
LONG_DESCRIPTION = "README"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pyMFI",
    version=VERSION,
    author="Antoniu Bjola, Matteo Salvalaglio",
    author_email="m.salvalaglio@ucl.ac.uk",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "numba",
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    classifiers=[
        "Development Status :: pre - Alpha",
        "Intended Audience :: Academic",
        "Programming Language :: Python :: 3",
    ],
    license="MIT",
)
