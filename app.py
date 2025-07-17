import streamlit as st
import pandas as pd
import pickle
import numpy as np

# --- 1. Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(page_title="Barcelona Price Predictor", layout="wide")


# --- 2. Load Trained Model and Scaler ---
# We define a function to cache the model loading
@st.cache_resource
def load_model_and_scaler():
    try:
        # Load the selected champion model and its corresponding scaler
        model_path = 'models/RandomForest_no_outliers.pkl'
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        scaler_path = 'models/scaler_no_outliers.pkl'
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        
        return model, scaler
    except FileNotFoundError:
        return None, None

model, scaler = load_model_and_scaler()


# --- 3. Streamlit App Interface ---
st.title("🏠 Barcelona Real Estate Price Predictor")
st.write("Enter the property features below to get an estimated price.")

# Show an error message if the model could not be loaded
if not model or not scaler:
    st.error("Error: Model or scaler file not found. Please ensure the 'models' folder contains the trained 'random_forest_no_outliers.pkl' and 'scaler_no_outliers.pkl' files.")
else:
    # --- Input Form ---
    with st.form("property_form"):
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Key Features")
            m2 = st.number_input("Area (m²)", min_value=20, max_value=500, value=80)
            rooms = st.number_input("Number of Rooms", min_value=0, max_value=10, value=3)
            floor_number = st.number_input("Floor Number", min_value=-2, max_value=50, value=2)
            discount = st.number_input("Discount (%)", min_value=0, max_value=100, value=0)

        with col2:
            st.header("Property Classification")
            status = st.selectbox("Property Status", options=[('Good Condition', 1), ('To Renovate', 2), ('New Build', 3), ('Unknown', 0)], format_func=lambda x: x[0])
            property_type = st.selectbox("Property Type", options=[('Exterior', 2), ('Interior', 1), ('Unknown', 0)], format_func=lambda x: x[0])
            cluster = st.selectbox("Market Segment (Cluster)", options=[0, 1, 2, 3], help="0: Standard, 1: High-End, 2: Budget, 3: Luxury")

        with col3:
            st.header("Amenities")
            air = st.checkbox("Air Conditioning")
            terrace = st.checkbox("Terrace")
            storage = st.checkbox("Storage Room")
            garage = st.checkbox("Garage")
            outside = st.checkbox("Outside Facing")
            wardrobes = st.checkbox("Built-in Wardrobes")
            pool = st.checkbox("Pool")
            garden = st.checkbox("Garden")
            has_elevator = st.checkbox("Elevator")
        
        submit_button = st.form_submit_button("Predict Price")

    # --- Prediction Logic ---
    if submit_button:
        # Create a dictionary with user inputs
        input_data = {
            'rooms': rooms, 'air': int(air), 'terrace': int(terrace), 'storage': int(storage),
            'garage': int(garage), 'outside': int(outside), 'wardrobes': int(wardrobes),
            'pool': int(pool), 'garden': int(garden), 'status': status[1],
            'has_elevator': int(has_elevator), 'property_type': property_type[1],
            'floor_number': floor_number, 'cluster': cluster, 'm2': m2,
            'discount': discount
        }
        
        # Define the feature order to match the training data
        feature_names = ['discount', 'm2', 'rooms', 'air', 'terrace', 'storage', 'garage', 'outside', 'wardrobes', 'pool', 'garden', 'status', 'has_elevator', 'property_type', 'floor_number', 'cluster']
        input_df = pd.DataFrame([input_data])[feature_names]

        # Scale the input data
        input_scaled = scaler.transform(input_df)

        # Make the prediction
        prediction = model.predict(input_scaled)[0]
        
        # Display the result
        st.success(f"💰 Estimated Price: **€{prediction:,.2f}**")