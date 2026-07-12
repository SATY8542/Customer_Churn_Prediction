import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = "models/churn_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("Model file not found! Please train the model first.")
    st.stop()

model = joblib.load(MODEL_PATH)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 Customer Churn Prediction")

st.sidebar.info("""
Machine Learning Project

Algorithm:
• Random Forest Classifier

Libraries:
• Streamlit
• Pandas
• Scikit-learn
""")

st.sidebar.success("Model Loaded Successfully")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Churn Prediction System")

st.write(
    "Predict whether a customer is likely to leave the company based on customer information."
)

st.markdown("---")

# -----------------------------
# Input Fields
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    credit = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=650
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

with col2:
    balance = st.number_input(
        "Balance",
        min_value=0.0,
        value=50000.0
    )

    salary = st.number_input(
        "Estimated Salary",
        min_value=0.0,
        value=60000.0
    )

# -----------------------------
# Show Input
# -----------------------------
st.subheader("Customer Details")

customer = pd.DataFrame({
    "CreditScore":[credit],
    "Age":[age],
    "Balance":[balance],
    "EstimatedSalary":[salary]
})

st.dataframe(customer)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Customer Churn"):

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0]

    st.markdown("---")

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("❌ Customer Will Leave")
    else:
        st.success("✅ Customer Will Stay")

    st.subheader("Prediction Probability")

    stay = probability[0] * 100
    leave = probability[1] * 100

    st.metric("Stay Probability", f"{stay:.2f}%")
    st.metric("Leave Probability", f"{leave:.2f}%")

    st.progress(float(probability[1]))



# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    " Customer Churn Prediction using Machine Learning"
)