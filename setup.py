import os
from setuptools import setup, find_packages

main_ns = {}
ver_path = os.path.join('spotui', 'version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="spotui",
    version=main_ns['__version__'],
    author="ceuk",
    description="Spotify TUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="spotify spotifytui",
    url="https://github.com/ceuk/spotui",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "spotipy==2.22.1",
        "windows-curses; platform_system == 'Windows'",
    ],
    entry_points={"console_scripts": ["spotui=spotui.__main__:main"]},
)
