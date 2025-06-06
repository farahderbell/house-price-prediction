# app/streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏠 House Price Predictor")

st.write("Input the property details and get the predicted sale price!")

# Create input widgets for your features
# Example (you can adjust based on your features):

lot_area = st.number_input('Lot Area (sq ft)', min_value=100, max_value=100000, value=5000)
year_built = st.number_input('Year Built', min_value=1800, max_value=2025, value=2000)
overall_qual = st.slider('Overall Quality (1-10)', 1, 10, 5)
bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=10, value=3)

# Make sure to add all relevant features your model needs!

if st.button("Predict Price"):
    # Prepare input for the model (make sure order matches training)
    input_data = np.array([[lot_area, year_built, overall_qual, bedrooms]])
    
    # Predict
    prediction = model.predict(input_data)
    
    st.success(f"Estimated Sale Price: ${prediction[0]:,.2f}")
