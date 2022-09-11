import os
from setuptools import *

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="Ratio_Analysis_Tool",
    version="0.0.1",
    author="Andrej Babamov",
    author_email="andrejbabamov@gmail.com",
    description="A simple python package that can be used for ratio analysis",
    long_description="A python package that can be used to obtain information regarding financial statements. ",
    long_description_content_type="text/markdown",
    url="https://github.com/babamovandrej/Ratio_Analysis_Tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
