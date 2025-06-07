import streamlit as st
import pandas as pd
import joblib
import os
import json

# Load pipeline
model_path = os.path.join(os.path.dirname(__file__), '../model_pipeline.pkl')
pipeline = joblib.load(model_path)

# Load expected features list saved during training
features_path = os.path.join(os.path.dirname(__file__), '../expected_features.json')
with open(features_path, 'r') as f:
    expected_features = json.load(f)

# Load feature dtypes saved during training
dtypes_path = os.path.join(os.path.dirname(__file__), '../feature_dtypes.json')
with open(dtypes_path, 'r') as f:
    feature_dtypes = json.load(f)

st.title("🏠 House Price Predictor")

# Inputs for some key features
lot_area = st.number_input('Lot Area (sq ft)', min_value=100, max_value=100000, value=5000)
year_built = st.number_input('Year Built', min_value=1800, max_value=2025, value=2000)
overall_qual = st.slider('Overall Quality (1-10)', 1, 10, 5)
bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=10, value=3)

if st.button("Predict Price"):
    # Build input dict with defaults
    input_dict = {}
    for feat in expected_features:
        if feat == 'LotArea':
            input_dict[feat] = [lot_area]
        elif feat == 'YearBuilt':
            input_dict[feat] = [year_built]
        elif feat == 'OverallQual':
            input_dict[feat] = [overall_qual]
        elif feat == 'BedroomAbvGr':
            input_dict[feat] = [bedrooms]
        else:
            # fill other features with default numeric 0 or string 'missing'
            if feature_dtypes.get(feat, 'float64') in ['object', 'category']:
                input_dict[feat] = ['missing']
            else:
                input_dict[feat] = [0]

    input_df = pd.DataFrame(input_dict)

    # Cast input dataframe columns to the saved dtypes
    for col, dtype_str in feature_dtypes.items():
        if col in input_df.columns:
            try:
                if dtype_str == 'category':
                    input_df[col] = input_df[col].astype('category')
                else:
                    input_df[col] = input_df[col].astype(dtype_str)
            except Exception as e:
                st.warning(f"Warning casting column {col} to {dtype_str}: {e}")

    # Predict
    prediction = pipeline.predict(input_df)

    st.success(f"🏷️ Estimated Sale Price: ${prediction[0]:,.2f}")
    st.write("This prediction is based on a machine learning model trained on historical house prices.")
    st.write("Happy predicting! 🏠")
    

    