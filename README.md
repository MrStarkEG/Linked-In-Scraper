# LinkedIn Scraper

This project is a LinkedIn scraper developed for educational purposes. It demonstrates how to scrape job listings from LinkedIn using Python, BeautifulSoup, and Selenium(Soon). The primary goal is to provide a learning resource for understanding web scraping techniques and tools.

## Table of Contents

- [Features] : It Extracts only the first 2 links of the seeked job.
- [Prerequisites] : Python 3.7 or Later
- [Installation] : requests, bs4
- [License] : MIT License

## Features

- **Scrapes LinkedIn Job Listings**: Extracts job titles, number of applicants, job criteria, and time since the job was posted.
- **BeautifulSoup**: Used for parsing the HTML content and extracting relevant data.
- **Selenium (UNDER DEVELOPMENT)**: Handles JavaScript-loaded content to ensure all job data is scraped correctly.

## Prerequisites

Before running the scraper, make sure you have the following installed:

- Python 3.7 or higher
- `pip` package manager
- A LinkedIn account (for login purposes)

Additionally, you'll need the following Python packages:

- `requests`
- `beautifulsoup4`

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/linkedin-scraper.git
   cd linkedin-scraper
   
   Create and activate a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   pip install -r requirements.txt

   python linkedin-scrapy.py
   Input the job title you want to search for when prompted.
   View the results in the console. The scraper will output job titles, number of applicants, job criteria, and links to the job postings.
  ```

   
