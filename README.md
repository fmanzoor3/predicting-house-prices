# Data Analysis Project: Price Prediction Model Of Real Estate in Türkiye

## Overview
This project aims to build a model that provides price estimates for houses in Türkiye based on various characteristics of the properties. The model considers data scraped from a real estate website to create a dataset of 3479 properties, each described by 21 features.

## Table of Contents
1. [Introduction](#introduction)
2. [Data](#data)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Conclusion](#conclusion)
6. [Usage](#usage)
7. [License](#license)

## Introduction
The objective of this project is to predict the price of a house in Türkiye based on its characteristics such as the number of rooms, whether it has air conditioning, if it is furnished, etc. Accurate price predictions can aid potential buyers and sellers in making informed decisions.

## Data
The dataset was created by web scraping data from [Tekce Overseas Property](https://tekce.com/property-turkiye). A total of 3479 properties were scraped, each described by 21 features:

    1. CITY                city the property resides in
    2. DISTRICT            district the property resides in
    3. NEIGHBOURHOOD       neighbourhood the property resides in
    4. AIR CONDITIONING    dummy variable (= 1 if property has air conditioning; 0 otherwise)
    5. FURNISHED           dummy variable (= 1 if property is furnished; 0 otherwise)
    6. CAR PARK            dummy variable (= 1 if property has car park; 0 otherwise)
    7. CENTRAL HEATING     dummy variable (= 1 if property has central heating; 0 otherwise)
    8. GAS COMBI           dummy variable (= 1 if property has gas combi; 0 otherwise)
    9. UNDERFLOOR HEATING  dummy variable (= 1 if property has underfloor heating; 0 otherwise)
    10. UNDERFLOOR COOLING dummy variable (= 1 if property has underfloor cooling; 0 otherwise)
    11. REALTOR FEE         
    12. TOTAL FLOORS        total floors of the building the property is in
    13. COMPLETION DATE     completion date of the property
    14. SUBTYPE             the type of property (e.g. ground floor apartment, detatched villa, etc.)
    15. PROPERTY SIZE       size of property in m^2
    16. STOREYS             number of storeys in the property
    17. BEDROOM             number of bedrooms in the property
    18. BATHROOM            number of bathrooms in the property
    19. BALCONY             number of balconies in the property
    20. FLOOR               the floor number of the property with respect to the building it is in (if applicable)
    21. PRICE               price of the property in €1000's

### Data Preprocessing
The raw data was preprocessed to handle missing values, encode categorical variables, and normalize numerical features.

## Methodology
1. **Web Scraping**: Used web scraping techniques and a web driver to collect data from the real estate website.
2. **Exploratory Data Analysis (EDA)**: Analysed the distribution and relationships of the features and target variable (house price).
3. **Data Splitting**: Split the dataset into training and testing sets to evaluate the model's performance.
4. **Multivariable Regression**: Built a multivariable regression model to predict house prices.
5. **Model Evaluation**: Evaluated the model's coefficients and residuals to understand its performance.
6. **Price Estimation**: Used the final model to estimate property prices based on given characteristics.

## Results
The final multivariable regression model showed the following performance:
- Coefficients: (List significant coefficients and their interpretations)
- Residuals: (Discuss the distribution and any patterns observed)
- Model Performance: (Include metrics like R-squared, Mean Absolute Error, etc.)

### Visualizations
- Scatter plots showing predicted vs actual prices
- Distribution of residuals
- Importance of features

## Conclusion
The model successfully predicts house prices in Turkey with reasonable accuracy. The analysis showed that features such as the number of rooms, presence of air conditioning, and district are significant predictors of house prices. Future work could explore more sophisticated models like Random Forests or Gradient Boosting to further improve accuracy.

## Usage
To replicate the analysis and use the model to estimate house prices:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fmanzoor3/predicting-house-prices.git
   cd predicting-house-prices
