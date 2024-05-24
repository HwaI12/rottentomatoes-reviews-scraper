from setuptools import setup, find_packages

setup(
    name='rottentomatoes-scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'selenium',
        'webdriver_manager'
    ],
    entry_points={
        'console_scripts': [
            'rottentomatoes-scraper=rottentomatoes_scraper.main:main',
        ],
    },
    url='https://github.com/HwaI12/rottentomatoes-scraper',
    license='MIT',
    description='A package to scrape reviews from Rotten Tomatoes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
