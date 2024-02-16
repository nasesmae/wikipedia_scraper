
# **Country Leaders Scraper**
![Title picture](./assets/scraping.jpg)

The Country Leaders Scraper is a Python script that collects information about country leaders from 'https://country-leaders.onrender.com'. It utilizes web scraping techniques to retrieve data on the leaders of different nations. Additionally, it scrapes the first paragraph from each leader's Wikipedia page. The scraper then saves all the retrieved data into a file named 'leaders.json'.

## Setup Instructions
1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install requests beautifulsoup4

3. Clone the repository to your local directory. 


## Script Components
*Main Script (scraper.py)*:

- Defines URLs for accessing the country-leaders API and related functionalities.
- Sends HTTP requests to fetch status information and country data.
- Implements functions to extract leader information and introductory paragraphs from Wikipedia pages.
- Saves the extracted data in a JSON file.

*functions*:

- get_leaders(): Fetches information about country leaders and extracts introductory paragraphs from Wikipedia.
- get_first_paragraph(wikipedia_url, Session): Extracts the introductory paragraph from a Wikipedia page URL.
- save(leaders_per_country): Saves the extracted leader information in a JSON file.

The scraper will commence scraping the website and gathering data. Upon completion, the data will be stored in the project directory as 'leaders.json'.

## Notes
- Ensure a stable internet connection for successful retrieval of data.
- The script stores the extracted data in a leaders.json file in the local directory.

## Timeline
This project was a significant learning curve, taking me three days to complete. 
