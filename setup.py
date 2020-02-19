import setuptools
from hellopypa.version import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hellopypa',
    version=__version__,
    author='mittelholcz',
    description='A sample Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mittelholcz/hellopypa',
    packages=setuptools.find_packages(exclude=['test']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "hellopypa=hellopypa.__main__:main",
        ]
    },
)
