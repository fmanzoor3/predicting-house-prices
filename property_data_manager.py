from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


KEY_FEATURES = [
    "AIR CONDITIONING",
    "FURNISHED",
    "CAR PARK",
    "CENTRAL HEATING",
    "GAS COMBI",
    "UNDERFLOOR HEATING",
    "UNDERFLOOR COOLING",
]

FIELDNAMES = [
    "CITY",
    "DISTRICT",
    "NEIGHBOURHOOD",
    *KEY_FEATURES,
    "REALTOR FEE",
    "TOTAL FLOORS",
    "COMPLETION DATE",
    "SUBTYPE",
    "PROPERTY SIZE",
    "STOREYS",
    "BEDROOM",
    "BATHROOM",
    "BALCONY",
    "FLOOR",
]

CSV_FILE = "property_data.csv"


class PropertyDataScraper:

    def __init__(self):
        self.reset_data()

    def reset_data(self):
        self.general_details = {}
        self.all_details_list = []
        self.property_prices = []

    def set_soup(self, URL):
        self.reset_data()
        response = requests.get(URL)
        response.raise_for_status()
        real_estate_html = response.text
        self.soup = BeautifulSoup(real_estate_html, "html.parser")
        self.location_elements = self.soup.select(".site-road .main-paths li a")
        self.features_elements = self.soup.select(".features")
        self.price_elements = self.soup.select(".rooms div")

    def get_location_details(self):
        tracker = 0
        location_details = {}
        for element in self.location_elements:
            text = element.getText()
            if tracker == 1:
                location_details["CITY"] = text
                tracker += 1
            elif tracker == 2:
                location_details["DISTRICT"] = text
                tracker += 1
            elif tracker == 3:
                location_details["NEIGHBOURHOOD"] = text
                tracker += 1
            if text == "Türkiye":
                tracker = 1
        self.general_details.update(location_details)

    def get_property_features(self):
        property_features = {feature: "0" for feature in KEY_FEATURES}
        for feature in KEY_FEATURES:
            if self.features_elements[0].find_all(
                string=lambda text: text.strip().upper() == feature
            ):
                property_features[feature] = "1"
        self.general_details.update(property_features)

    def get_property_prices(self):
        info = []
        for element in self.price_elements:
            data_tab = element.get("data-tab")
            price = element.get("data-price")
            if data_tab and price:
                info.append({"data-tab": data_tab, "data-price": price})
        self.property_prices = info

    def get_all_property_details(self, property):
        data_tab = property["data-tab"]
        lists = self.soup.select(
            f'.property-details .detail-list[data-tab="{data_tab}"] li'
        )
        details = {}
        for list_item in lists:
            spans = list_item.select("span")
            if len(spans) >= 2:
                key = spans[0].getText().strip().upper()
                value = spans[1].getText().strip()
                if key in FIELDNAMES:
                    details[key] = value
        return details

    def obtain_all_property_info(self, URL):
        self.set_soup(URL)
        self.get_location_details()
        self.get_property_features()
        self.get_property_prices()

        for property in self.property_prices:
            property_details = self.get_all_property_details(property)
            if property["data-tab"] == "general":
                self.general_details.update(property_details)
            else:
                full_details = {**self.general_details, **property_details}
                self.all_details_list.append(full_details)
        return self.all_details_list

    def create_csv(self):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

            # Write header
            writer.writeheader()

            # Write rows
            for row in self.all_details_list:
                writer.writerow(row)

    def update_csv(self):
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

            # Write rows
            for row in self.all_details_list:
                writer.writerow(row)
