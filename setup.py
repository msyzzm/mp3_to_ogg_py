from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="audio-converter-cli",
    version="1.0.0",
    author="Your Name",
    description="A simple command-line tool to convert between MP3 and OGG audio formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mp3-to-ogg-py",
    py_modules=["mp3_to_ogg", "exporters"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pydub>=0.25.1",
        "progress>=1.6",
    ],
    entry_points={
        "console_scripts": [
            "audio-converter=mp3_to_ogg:main",
        ],
    },
)

