## Using BeautifulSoup and Selenium to scrape data on properties in Turkey
from property_data_scraper import PropertyDataScraper
from web_driver import WebDriver

property_data_scraper = PropertyDataScraper()
web_driver = WebDriver()

web_driver.obtain_all_URLS_across_all_pages()
all_property_URLs = web_driver.URL_list
print(all_property_URLs)

for URL in all_property_URLs:
    property_data = property_data_scraper.obtain_all_property_info(URL)
    property_data_scraper.update_csv()
