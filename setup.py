import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  #
# Fallback to '0.0.0'
version = os.getenv("VERSION", "0.0.0")


setup(
    name="attendancelist_test",
    version=version,
    author="Maksymilian Jura",
    author_email="maksymilian.jura3118@gmail.com",
    description="Attendance list for uni",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kaksi3118/attendancelist_test",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
