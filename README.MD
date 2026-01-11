# Books to Scrape - Python Scraper

A Python-based web scraper designed to extract book information from [Books to Scrape](https://books.toscrape.com/), a sandbox website for web scraping practice.

## Features
- **Multi-page Scraping**: Iterates through the catalogue pages automatically.
- **Detailed Extraction**: Collects book titles, prices, descriptions, and URLs.
- **Image Downloader**: Automatically downloads book cover images to a local folder.
- **Excel Export**: Saves all scraped data into a structured `.xlsx` file using `XlsxWriter`.
- **Memory Efficient**: Uses Python generators (`yield`) to process data without loading everything into RAM at once.

## Tech Stack
- **Python 3.x**
- **Requests**: For handling HTTP communications.
- **BeautifulSoup4 & LXML**: For parsing and navigating HTML structures.
- **XlsxWriter**: For generating Excel reports.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   
2. Install all dependencies from requirements.txt:  

   pip install -r requirements.txt