import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --- Configuration and Constants ---
# Define the percentage tolerance for investment analysis
TOLERANCE = 0.10 

# --- Load Model and Features ---
try:
    model = joblib.load('house_price_model.joblib')
    feature_cols = joblib.load('feature_columns.joblib')
except FileNotFoundError:
    st.error("Model files not found. Please ensure 'house_price_model.joblib' and 'feature_columns.joblib' are uploaded.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model or features: {e}")
    st.stop()


# --- Helper Functions for UI Dropdowns ---

# Note: These values must be consistent with the features created in Cell 2
def get_unique_values(feature_list, prefix):
    values = [col.split(prefix)[-1] for col in feature_list if col.startswith(prefix)]
    
    # Manually defined base values 
    if prefix == 'Number of rooms_':
        base_value = '1+1' 
    elif prefix == 'District_':
        base_value = sorted(values)[0] if values else ''
    elif prefix == 'Building Age_':
        base_value = '0' 
    else:
        base_value = sorted(values)[0] if values else '' 
        
    return [base_value] + sorted(values)

# Unique categorical values
DISTRICTS = get_unique_values(feature_cols, 'District_')
ROOMS = get_unique_values(feature_cols, 'Number of rooms_')
AGE = get_unique_values(feature_cols, 'Building Age_')
FLOOR = get_unique_values(feature_cols, 'Floor location_')
HEATING = get_unique_values(feature_cols, 'Heating_')
USING_STATUS = get_unique_values(feature_cols, 'Using status_')


# --- Streamlit UI ---
st.set_page_config(page_title="Investment Opportunity Predictor", layout="wide")
st.title("🏡 Istanbul Property Investment Advisor")
st.subheader("Compare Listing Price to Fair Market Value")
st.markdown(f"The investment recommendation uses a $\\pm {int(TOLERANCE*100)}\\%$ market value margin.")


# --- Sidebar Inputs (Property Features) ---
with st.sidebar:
    st.header("1. Property Features")
    
    gross_sqm = st.number_input("Gross m²", min_value=50, max_value=500, value=120)
    net_sqm = st.number_input("Net m²", min_value=40, max_value=450, value=100)
    bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=1)
    
    st.header("2. Location & Condition")
    
    district = st.selectbox("District", options=DISTRICTS, index=0)
    rooms = st.selectbox("Number of Rooms", options=ROOMS, index=ROOMS.index('3+1') if '3+1' in ROOMS else 0)
    age = st.selectbox("Building Age", options=AGE, index=AGE.index('1') if '1' in AGE else 0)
    floor = st.selectbox("Floor Location", options=FLOOR, index=FLOOR.index('5') if '5' in FLOOR else 0)
    heating = st.selectbox("Heating Type", options=HEATING, index=HEATING.index('Natural Gas (Combi)') if 'Natural Gas (Combi)' in HEATING else 0)
    using_status = st.selectbox("Using Status", options=USING_STATUS, index=USING_STATUS.index('Property owner') if 'Property owner' in USING_STATUS else 0)

    st.header("3. Key Amenities")
    
    has_elevator = st.checkbox("Has Elevator", value=True)
    has_security = st.checkbox("Has Security", value=True)
    has_pool = st.checkbox("Has Swimming Pool (Open)", value=False)
    
st.markdown("---")

# --- Main Panel Inputs (Listing Price & Button) ---
st.header("4. Listing Price Input")
listing_price = st.number_input(
    "Enter the Advertised Listing Price (TL)", 
    min_value=10000.0, 
    max_value=10000000.0, 
    value=450000.0, 
    step=10000.0,
    format="%f"
)

st.markdown("---")
analyze_button = st.button("🚀 Analyze Investment Potential")


# --- Prediction and Comparison Logic ---
if analyze_button:
    
    # 1. Create a dictionary of user inputs (features only)
    user_data = {
        'm² (Gross)': gross_sqm,
        'm² (Net)': net_sqm,
        'Number of bathrooms': bathrooms,
        'District': district,
        'Number of rooms': rooms,
        'Building Age': age,
        'Floor location': floor,
        'Heating': heating,
        'Using status': using_status,
        'Elevator': 1 if has_elevator else 0, 
        'Security': 1 if has_security else 0,
        'Swimming Pool (Open)': 1 if has_pool else 0 
    }
    
    # 2. Prepare Feature DataFrame
    input_df = pd.DataFrame([user_data])
    
    # 3. Handle One-Hot Encoding
    cols_to_encode = ['District', 'Number of rooms', 'Building Age', 'Floor location', 'Heating', 'Using status']
    input_df_encoded = pd.get_dummies(input_df, columns=cols_to_encode, drop_first=True)
    
    # 4. Align features (Crucial for the XGBoost model's input vector)
    missing_cols = set(feature_cols) - set(input_df_encoded.columns)
    for c in missing_cols:
        input_df_encoded[c] = 0
    
    # Reorder columns to match the saved blueprint
    final_input_df = input_df_encoded[feature_cols]
    
    # 5. Predict the Model Value
    try:
        predicted_value = model.predict(final_input_df)[0]
        
        # 6. Apply Investment Recommendation Logic
        lower_bound = predicted_value * (1 - TOLERANCE)
        upper_bound = predicted_value * (1 + TOLERANCE)
        
        st.header("✅ Investment Recommendation")

        if listing_price < lower_bound:
            st.success("## 🌟 OPPORTUNITY")
            st.markdown(f"The listing price of **₺ {listing_price:,.0f} TL** is significantly below the model's estimated value.")
            st.balloons()
            
        elif listing_price > upper_bound:
            st.error("## 💸 EXPENSIVE")
            st.markdown(f"The listing price of **₺ {listing_price:,.0f} TL** is significantly above the model's estimated value.")
            
        else:
            st.info("## ⚖️ NORMAL")
            st.markdown(f"The listing price of **₺ {listing_price:,.0f} TL** falls within the expected market value range.")

        # 7. Summary
        st.markdown("---")
        st.subheader("Summary")
        st.markdown(f"- **Advertised Listing Price:** **₺ {listing_price:,.0f} TL**")
        st.markdown(f"- **Model Estimated Value (Fair Value):** **₺ {predicted_value:,.0f} TL**")
        st.markdown(f"- **Normal Range ( $\\pm {int(TOLERANCE*100)}\\%$ ):** ₺ {lower_bound:,.0f} TL to ₺ {upper_bound:,.0f} TL")
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
