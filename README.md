# Rotten Tomatoes Scraper

Rotten Tomatoes Scraper is a Python package for scraping movie reviews from Rotten Tomatoes. This package allows you to extract and process reviews efficiently.

## Features

- Scrape movie reviews from Rotten Tomatoes.
- Save reviews to CSV files.
- Process and analyze review data.

## Installation

You can install the package via pip:

```bash
pip install rottentomatoes-scraper
```

## Usage

### Command Line Interface

You can use the scraper directly from the command line:

```bash
rottentomatoes-scraper <movie_name>
```

### As a Python Module

You can also use the package as a Python module:

```python
from rottentomatoes_scraper import reviews_scraper

# Scrape reviews for a specific movie
reviews = reviews_scraper.scrape_reviews("Inception")

# Process and save reviews
import csv_handler
csv_handler.save_to_csv(reviews, "inception_reviews.csv")
```

## Files

- `main.py`: Entry point for the command line interface.
- `reviews_scraper.py`: Contains the scraping logic.
- `csv_handler.py`: Handles CSV file operations.
- `date_utils.py`: Utility functions for date manipulation.
- `web_element_click.py`: Utility functions for interacting with web elements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

Your Name - [seokcheonhwami@gmail.com](mailto:your.seokcheonhwami@gmail.com)

## Acknowledgements

- Inspired by the need to automate the process of scraping movie reviews.
- Thanks to the open-source community for providing the tools and libraries that made this project possible.