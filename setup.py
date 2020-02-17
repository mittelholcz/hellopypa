import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hellopypa",
    version="0.0.2",
    author="mittelholcz",
    description="Get string 'hello pypa!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mittelholcz/hellopypa",
    packages=setuptools.find_packages(exclude=['test']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
