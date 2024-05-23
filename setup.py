# setup.py
from setuptools import setup, find_packages

setup(
    name='rottentomatoes-scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'selenium',
    ],
    author='Fami Ishikawa',
    author_email='noki0610.yu@gmail.com',
    description='A scraper for Rotten Tomatoes reviews',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HwaI12/rottentomatoes-scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
