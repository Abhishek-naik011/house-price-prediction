import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

area = st.number_input("Enter Area")
bedrooms = st.number_input("Enter Bedrooms")

if st.button("Predict"):
    result = model.predict([[area, bedrooms]])
    st.success(f"Predicted Price: {result[0]}")