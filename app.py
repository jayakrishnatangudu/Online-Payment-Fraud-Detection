import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("fraud_model.pkl", "rb"))

st.title("💳 Online Payment Fraud Detection")
st.write("Enter transaction details to predict whether a payment is fraudulent.")

# ---- INPUT FIELDS ----
# ⚠️ Number of inputs MUST match training features
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)

# ---- PREDICTION ----
if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
