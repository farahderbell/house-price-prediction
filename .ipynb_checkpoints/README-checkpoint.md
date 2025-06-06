# House Price Prediction 🏠📊

![Actual vs Predicted Sale Price](actual_vs_predicted.png)

---

## Project Overview

This project is a **House Price Prediction** model built using Python and `scikit-learn`. The goal is to predict house sale prices based on various features such as location, size, and other property characteristics. This is a classic regression problem in machine learning, helping real estate professionals and buyers estimate property values with high accuracy.

---

## Why This Project?

Understanding housing prices is crucial for buyers, sellers, and investors to make informed decisions. By leveraging historical data and machine learning, this model aims to:

- Analyze key factors influencing house prices  
- Predict sale prices for new listings  
- Provide insights into the real estate market trends

---

## Dataset

The dataset consists of multiple numerical and categorical features describing houses, such as:

- Square footage  
- Number of bedrooms and bathrooms  
- Neighborhood quality  
- Year built  
- And many others

Before modeling, the data was cleaned, missing values were imputed, and categorical variables were encoded properly to ensure accuracy.

---

## Methodology

1. **Data Preprocessing:**  
   - Handling missing values using imputation strategies  
   - Encoding categorical variables using one-hot encoding  
   - Splitting data into training and testing sets  

2. **Model Training:**  
   - Using a `LinearRegression` model from `scikit-learn`  
   - Evaluating model performance with RMSE (Root Mean Squared Error)

3. **Results:**  
   - The model achieved an RMSE of **0.00289**, indicating very close predictions to actual prices  
   - Visualization below compares actual vs. predicted prices to demonstrate model effectiveness

---

## How to Use

1. Clone the repo  
2. Install required packages:  
   ```bash
   pip install -r requirements.txt
