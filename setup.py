import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))

version = "0.90"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()


required = [
    "pip>=18.0",
    "setuptools>=36.2.1",
    "virtualenv-clone>=0.2.5",
    "virtualenv",
]
extras = {}





class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(here, "dist"))
        except FileNotFoundError:
            pass
        self.status("Building Source distribution...")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))
        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload --repository testpypi dist/*")
        self.status("Pushing git tags...")
        os.system("git tag v{0}".format(version))
        os.system("git push --tags")
        sys.exit()


setup(
    name="clutch",
    version=version,
    description="Clutch Python Package Manager",
    long_description="Clutch Python Package Manager",
    long_description_content_type='text/markdown',
    author="Austin Gabel",
    author_email="agabel@gabelmedia.com",
    url="https://github.com/agabel/clutch",
    packages=find_packages(exclude=[]),
    entry_points={
        "console_scripts": [
            "clutch=clutch:cli",
        ]
    },
    package_data={
        "": ["LICENSE", "README.md"],
    },
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    zip_safe=True,
    setup_requires=[],
    install_requires=required,
    extras_require=extras,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    cmdclass={"upload": UploadCommand},
)
