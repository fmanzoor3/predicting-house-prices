## Using BeautifulSoup to scrape info from Zillow clone
from bs4 import BeautifulSoup
import requests
import pandas

# TODO [] Add Orientation/Heating info to our scraped data
# TODO [] Get selenium to enter each page, scrape the info and then after each listing on a page to go to the next page
# TODO [] Format our scraped data so that it can be turned into a csv that we will be able to use in our data analysis
# TODO [] When webscraping if a property doesnt have a feature its not going to be mentioned in its info; account for this to say that those features are N/A

REAL_ESTATE_URL = (
    "https://tekce.com/ad/adb-00070-brand-new-apartments-for-sale-in-izmir-sasali"
)

from property_data_manager import PropertyDataScraper

pds = PropertyDataScraper()
print(pds.obtain_all_property_info(REAL_ESTATE_URL))

# response = requests.get(REAL_ESTATE_URL)
# response.raise_for_status()

# real_estate_html = response.text

# soup = BeautifulSoup(real_estate_html, "html.parser")

# location_elements = soup.select(".site-road .main-paths li a")


# def get_location_details(location_elements):
#     tracker = 0
#     location_details = {}
#     for element in location_elements:
#         if tracker == 1:
#             location_details["CITY"] = element.getText()
#             tracker += 1
#         elif tracker == 2:
#             location_details["DISTRICT"] = element.getText()
#             tracker += 1
#         elif tracker == 3:
#             location_details["NEIGHBOURHOOD"] = element.getText()
#             tracker += 1
#         if element.getText() == "Türkiye":
#             tracker = 1
#     return location_details


# general_details = {}
# general_details.update(get_location_details(location_elements))

# KEY_FEATURES = [
#     "AIR CONDITIONING",
#     "FURNISHED",
#     "CAR PARK",
#     "CENTRAL HEATING",
#     "GAS COMBI",
#     "UNDERFLOOR HEATING",
#     "UNDERFLOOR COOLING",
# ]
# features_elements = soup.select(".features")


# def get_property_features(features_blocks):
#     property_features = {feature: "0" for feature in KEY_FEATURES}
#     for feature in KEY_FEATURES:
#         if features_blocks[0].find_all(
#             string=lambda text: text == f"{feature.title()}"
#         ):
#             property_features[feature] = "1"
#     return property_features


# general_details.update(get_property_features(features_elements))
# print(general_details)

# price_elements = soup.select(".rooms div")


# def get_property_prices(price_elements):
#     info = []
#     for element in price_elements:
#         dict = {}
#         data_tab = element.get("data-tab")
#         price = element.get("data-price")
#         dict["data-tab"] = data_tab
#         dict["data-price"] = price
#         info.append(dict)
#     return info


# property_prices = get_property_prices(price_elements)
# print(property_prices)


# def get_all_property_details(property):
#     data_tab = property["data-tab"]
#     lists = soup.select(f'.property-details .detail-list[data-tab="{data_tab}"] li')
#     dict = {}
#     for list in lists:
#         test = list.select("span")
#         if (
#             test[0].getText()
#             in ["REALTOR FEE", "TOTAL FLOORS", "COMPLETION DATE", "PLOT SIZE"]
#             or data_tab != "general"
#         ):
#             dict[test[0].getText()] = test[1].getText()
#     return dict


# all_details_list = []
# for property in property_prices:
#     if property["data-tab"] == "general":
#         general_details.update(get_all_property_details(property))
#     else:
#         all_details_list.append(
#             {**general_details, **get_all_property_details(property)}
#         )
# print(all_details_list)

# FIELDNAMES = [
#     "CITY",
#     "DISTRICT",
#     "NEIGHBOURHOOD",
#     "AIR CONDITIONING",
#     "FURNISHED",
#     "CAR PARK",
#     "CENTRAL HEATING",
#     "GAS COMBI",
#     "UNDERFLOOR HEATING",
#     "UNDERFLOOR COOLING",
#     "REALTOR FEE",
#     "TOTAL FLOORS",
#     "COMPLETION DATE",
#     "SUBTYPE",
#     "PROPERTY SIZE",
#     "STOREYS",
#     "BEDROOM",
#     "BATHROOM",
#     "BALCONY",
#     "FLOOR",
# ]
# import csv

# csv_file = "property_data.csv"

# with open(csv_file, "a", newline="", encoding="utf-8") as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)

#     # # Write header
#     # writer.writeheader()

#     # Write rows
#     for row in all_details_list:
#         writer.writerow(row)

# data = pandas.read_csv("property_data.csv")
# print(data.head(8))

# print(property_price[-1].get("data-price"))

# house_attributes = [tag.select("span") for tag in house_details]
# test = {}
# for i in range(len(house_attributes)):
#     test[house_attributes[i][0].getText()] = [house_attributes[i][1].getText()]
# print(test)
# data = pandas.DataFrame(test)
# data.to_csv("new_data.csv")
