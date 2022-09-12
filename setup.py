from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Financial Statement Analysis Tool'
LONG_DESCRIPTION = 'A package allowing users to compute ratios needed for financial statement analysis'

setup(
    name="ratioanalysistool",
    version="0.0.1",
    author="Andrej Babamov",
    author_email="andrejbabamov@gmail.com",
    url="https://github.com/babamovandrej/Ratio_Analysis_Tool",
    description="A python package that computes ratios that are used for financial statement analysis. The package can be used to evaluate a company's liquidity,solvency,and profitability. ",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'finance', 'statements',
              'liquidity', 'earnings', 'profitability', 'turnover', 'capital'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
