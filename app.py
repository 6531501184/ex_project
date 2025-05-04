# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
import numpy as np

# Load model
with open('random_forest_model.pkl', 'rb') as f:
    dtm_model = pickle.load(f)

# App title
st.title("🌼 Music Recommendation")
st.write("Choose your music preference:")

# Radio buttons instead of sliders
sepal_length = st.radio("Sepal Length (cm)", [1, 2, 3, 4, 5, 6])
sepal_width = st.radio("Sepal Width (cm)", [1, 2, 3, 4, 5, 6])
petal_length = st.radio("Petal Length (cm)", [1, 2, 3, 4, 5, 6])
petal_width = st.radio("Petal Width (cm)", [1, 2, 3, 4, 5, 6])

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = dtm_model.predict(input_data)
    species = [1, 2, 3, 4, 5, 6]
    st.success(f"The predicted species is: **{species[prediction[0]]}**")




