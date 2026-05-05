# Real Estate Price Analysis in Croatia

## Project Overview
This project analyzes real estate listings from Njuškalo to understand pricing patterns in Croatia. The goal is to clean the data, calculate useful metrics, and extract insights about the housing market.

## Objectives
- Clean and prepare raw real estate data
- Convert text-based values into numeric format
- Calculate price per square meter
- Identify outliers and inconsistencies
- Analyze prices by location
- Visualize key relationships in the data

## Dataset
The dataset contains the following columns:
- price
- property type (house/condo)
- name
- description
- square footage
- number of rooms
- location

## Data Cleaning
The following steps were performed:
- Converted price values from text (e.g. "300.000 €") into numeric format
- Cleaned square footage values (e.g. "79,47 m²" → 79.47)
- Extracted numeric values for number of rooms
- Split location into county, city, and district
- Removed missing and invalid values

## Feature Engineering
A new variable was created:
- price per square meter = price / square footage

This metric was used for all further analysis.

## Outlier Handling
Some values of price per square meter were unrealistic (very low or very high).  
To improve data quality, extreme values were filtered out.

## Key Findings
- Average price per square meter is around 6900 €/m²
- Prices vary significantly depending on location
- Dubrovnik has the highest average prices
- Luxury properties significantly increase the upper range of values

## Visualizations
The analysis includes:
- Distribution of price per square meter
- Relationship between square footage and price
- Average price per location

## Tools Used
- Python
- Pandas
- Matplotlib

## Conclusion
The project demonstrates a full data analysis workflow including data cleaning, feature engineering, exploratory analysis, and visualization. It provides insights into real estate pricing patterns in Croatia.
