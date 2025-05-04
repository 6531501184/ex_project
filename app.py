# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load model
with open('random_forest_model.pkl', 'rb') as f:
    dtm_model = pickle.load(f)

# App title
st.title("🎶 Music Recommendation System")
st.write("Please select your preferences for the following music-related features:")

# Predict group section
st.subheader("Predict Group (Cluster)")

# Input fields based on numerical columns
num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
if "cluster" in num_cols:
    num_cols.remove("cluster")

input_data = []
for col in num_cols:
    val = st.number_input(f"Enter {col}", value=float(df[col].mean()))
    input_data.append(val)

if st.button("Predict Group"):
    prediction = model.predict([input_data])[0]
    st.success(f"The predicted group is: **Cluster {prediction}**")

# Optional: visualization
if "cluster" in df.columns and len(num_cols) >= 2:
    st.subheader("Cluster Plot")
    x_axis = st.selectbox("X-Axis", num_cols)
    y_axis = st.selectbox("Y-Axis", [col for col in num_cols if col != x_axis])

    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_axis, y=y_axis, hue="cluster", palette="Set2", ax=ax)
    st.pyplot(fig)






