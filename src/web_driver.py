from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

REAL_ESTATE_URL = "https://tekce.com/property-turkiye"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


class WebDriver:
    def __init__(self):
        self.URL_list = []
        self.final_page_number = 1

    def get_final_page_number(self):
        driver.get(REAL_ESTATE_URL)
        page_number_elements = driver.find_elements(
            By.CSS_SELECTOR, value=".pagination li"
        )
        page_numbers = []
        for element in page_number_elements:
            if element.get_attribute("data-page"):
                page_numbers.append(int(element.get_attribute("data-page")))
        self.final_page_number = max(page_numbers)

    def obtain_property_URLS_from_page(self, page_number):
        driver.get(f"{REAL_ESTATE_URL}?page={page_number}")
        property_list_elements = driver.find_elements(
            By.CSS_SELECTOR, value=".property-list .property-details a"
        )
        for element in property_list_elements:
            self.URL_list.append(element.get_attribute("href"))

    def obtain_all_URLS_across_all_pages(self):
        self.get_final_page_number()
        for i in range(self.final_page_number):
            page_number = i + 1
            self.obtain_property_URLS_from_page(page_number)
