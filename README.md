# Amazon Scraper
Extract ASIN (Amazon Standard Identification Number), name and price from Amazon product pages.

## Installation

### Setup
1. Clone the repository 
```
git clone https://github.com/XavierZambrano/amazon-scraper.git
```
2. Create a virtual environment and activate it
3. Install the requirements
```bash
pip install -r requirements.txt
```

## Usage
To run the scraper, use the following command: 
- urls. List of URLs to scrape. It can be a single URL or multiple URLs separated by commas.
```
scrapy crawl product -a urls=https://www.amazon.com/Little-Black-Classics-Box-Penguin/dp/0141398876/,https://www.amazon.com/War-Peace-Penguin-Clothbound-Classics/dp/0241265541/ -O results.csv
```
For more information about scrapy crawl arguments, check the [Scrapy documentation](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl).

Example result: [results.csv](assets/results.csv)
