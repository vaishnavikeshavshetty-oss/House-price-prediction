
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Page Config
st.set_page_config(page_title="🏡 House Price Prediction", page_icon="💰", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .stButton>button {
        background: linear-gradient(to right, #00b09b, #96c93d);
        color: white;
        border-radius: 12px;
        padding: 0.75em 1.5em;
        font-size: 1.1em;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #96c93d, #00b09b);
        color: white;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 15px;
        background: #ffffff;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏡 House Price Prediction App")
st.write("### Enter house details and get an instant price prediction 💰")

st.divider()

# Two-column layout for inputs
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("🛏️ Number of bedrooms", min_value=0, value=3)
    bathrooms = st.number_input("🛁 Number of bathrooms", min_value=0, value=2)
    condition = st.slider("🏠 House condition (1 - Worst, 5 - Best)", 1, 5, 3)

with col2:
    livingarea = st.number_input("📐 Living area (sq ft)", min_value=200, value=2000)
    numberofschools = st.number_input("🏫 Schools nearby", min_value=0, value=2)

st.divider()

# Prediction
X = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]
predictbutton = st.button("🔮 Predict Price")

if predictbutton:
    st.balloons()
    X_array = np.array(X)
    prediction = model.predict(X_array)[0]

    # Display Result in styled box
    st.markdown(f"""
        <div class="prediction-box">
            <h2>💵 Predicted House Price</h2>
            <h1 style="color:#2ecc71;">₹ {prediction:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)

else:
    st.info("👉 Enter the details above and click **Predict Price**")
