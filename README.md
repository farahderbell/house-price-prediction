# 🏠 House Price Prediction

This project builds a machine learning model to predict house sale prices based on various property features, helping buyers and sellers estimate property values accurately.

---

## 📁 Dataset

- **Source:** House price data with multiple numerical and categorical features such as size, bedrooms, neighborhood, year built, and more.  
- Contains detailed property attributes and sale prices.

---

## 🌍 Content Overview

- Data preprocessing including missing value imputation and categorical encoding  
- Training a Linear Regression model to predict sale prices  
- Evaluating model performance with RMSE metric  
- Visualizing actual vs predicted sale prices  
- Deploying the trained model as a web application using Streamlit

---

## 📈 Visualizations

### 1. Actual vs Predicted Sale Prices  
![Regression Plot](notebooks/actual_vs_predicted.png)

---

## 🧠 Machine Learning

- **Model:** Linear Regression  
- **Preprocessing:** SimpleImputer for missing values, OneHotEncoder for categorical features  
- **Evaluation Metric:** Root Mean Squared Error (RMSE)

---

## 🛠️ Tools Used

- Python (Pandas, NumPy, Matplotlib)  
- scikit-learn (LinearRegression, SimpleImputer, OneHotEncoder)  
- Jupyter Notebook  
- Streamlit (for web app)

---

## 🌐 Web App

An interactive web application is built using **Streamlit**...

### 📷 Web App Preview

![House Price Predictor UI](notebooks/house.png)

This app allows users to enter features such as:
- Lot Area  
- Year Built  
- Overall Quality  
- Number of Bedrooms  

And instantly get a predicted sale price based on the trained model.

### Features:

- User-friendly form to input features like square footage, neighborhood, etc.  
- Displays predicted house price instantly  
- Integrated with the trained ML model

---

## 🚀 Deployment

You can deploy the Streamlit app locally or on a cloud platform like **Streamlit Community Cloud**, **Render**, or **Heroku**.

### Run the app locally:

```bash
streamlit run app.py

## 🚀 How to Run locally

1. Clone this repository 
2.pip install -r requirements.txt
3.streamlit run app.py
---

## 📌 Author

Made with ❤️ by [Farah]