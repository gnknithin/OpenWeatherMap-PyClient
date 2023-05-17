from setuptools import find_packages, setup


def read(fname: str):
    with open(file=fname, encoding="utf-8") as fp:
        content = fp.read()
    return content


setup(
    name="openweathermappy",
    version="0.1.0",
    description="A simple wrapper around OpenWeatherMap APIs using Python",
    long_description=read("README.md"),
    author="Nithin",
    author_email="gnknithin@gmail.com",
    url="https://github.com/gnknithin/OpenWeatherMap-PyClient",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=[
        "A simple wrapper around OpenWeatherMap APIs using Python",
        "openweathermap", "openweathermap api", "openweathermap api client"
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests"]),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    python_requires=">=3.7",
    extras_require={
        "tests": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "pytest-dotenv"
        ],
    },
    test_suite="tests",
)
