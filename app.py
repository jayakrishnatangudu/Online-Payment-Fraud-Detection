import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("fraud_model.pkl", "rb"))

st.set_page_config(page_title="Fraud Detection", layout="centered")

st.title("💳 Online Payment Fraud Detection")
st.write("Enter transaction feature values to predict fraud.")

# Exact feature list (DO NOT change order)
feature_names = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7',
    'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14',
    'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26',
    'V27', 'V28', 'normAmount'
]

st.subheader("Transaction Features")

# Collect user input
input_data = {}

for feature in feature_names:
    input_data[feature] = st.number_input(
        label=feature,
        value=0.0,
        format="%.6f"
    )

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame([input_data])  # keeps column order

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")
