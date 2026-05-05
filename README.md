# Dubrovnik Real Estate Analysis

This project analyzes apartment prices in Dubrovnik using real estate data from Njuškalo. The goal is to understand how location affects property prices and to segment districts based on price levels.

## Project objectives

- Clean and preprocess real estate data
- Calculate price per square meter
- Analyze price differences across districts
- Identify market segmentation using clustering
- Detect market trends and insights

## Dataset

The dataset contains apartment listings with information such as:
- Price
- Size (m²)
- Location (district in Dubrovnik)

## Project structure


data/ Raw dataset (Excel file)
main.py Main analysis script
requirements.txt Dependencies


## Key insights

- Dubrovnik real estate prices vary significantly by district
- Premium districts (Pile, Stari Grad, Lozica) are more than twice as expensive as budget areas
- Location is the strongest factor affecting price per m²
- The market can be clearly divided into 3 segments: budget, mid-range, and luxury

## Methods used

- Data cleaning and preprocessing (pandas)
- Feature engineering (price per m²)
- Statistical analysis (mean, median, correlation)
- Outlier detection (IQR method)
- Clustering (KMeans from scikit-learn)
- Data visualization (matplotlib)

## Market segmentation

The analysis groups districts into three categories:

- Budget areas: peripheral districts with lower prices
- Mid-range areas: standard residential zones
- Luxury areas: Old Town and coastal premium locations

## Results

- Most expensive district: Pile
- Cheapest district: Dubrava
- Price gap between districts: ~5400 €/m²
- Clear clustering structure in the real estate market

## How to run

Install dependencies:


pip install -r requirements.txt


Run analysis:


python main.py


## Tools used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## Author

Created as a data analysis project for learning purposes and portfolio development.
