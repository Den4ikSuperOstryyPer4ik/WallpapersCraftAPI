from setuptools import setup, find_packages
import re


github = "https://github.com/Den4ikSuperOstryyPer4ik/WallpapersCraftAPI/"

def get_version():
    with open("wallpaperscraft/__init__.py", encoding="utf-8") as f:
        return re.findall(r"__version__ = \"(.+)\"", f.read())[0]

def get_readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="wallpaperscraft",
    fullname="WallpapersCraftAPI",
    version=get_version(),
    author="Den4ikSuperOstryyPer4ik",
    description="Unofficial API WallpapersCraft (wallpaperscraft.com)",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    url=github,
    packages=find_packages(),
    download_url=f"{github}/releases/latest",
    install_requires=[
        "bs4",
        "requests",
        "aiohttp",
        "pydantic",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="python3 wallpaperscraft wallpapers craft WallpapersCraftAPI",
    python_requires='>=3.7',
    license="Apache2.0",
)
