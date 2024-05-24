import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rottentomatoes-scraper",
    version="0.0.1",
    author="Fami Ishikawa",
    author_email="s2222061@stu.musashino-u.ac.jp",
    description="A package to scrape Rotten Tomatoes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HwaI12/rottentomatoes-scraper",
    project_urls={
        "Bug Tracker": "https://github.com/HwaI12/rottentomatoes-scraper",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=[
        'rottentomatoes_scraper'
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'rottentomatoes-scraper=rottentomatoes_scraper:main',
        ],
    },
)