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
st.title("🌼 Music Recommendation System")
st.write("Choose your preferences:")

# Radio buttons for 6 features (adjust labels and values as needed)
f1 = st.radio("Rhythm Preference", [1, 2, 3, 4, 5])
f2 = st.radio("Energy Level", [1, 2, 3, 4, 5])
f3 = st.radio("Mood", [1, 2, 3, 4, 5])
f4 = st.radio("Tempo", [1, 2, 3, 4, 5])
f5 = st.radio("Vocal vs. Instrumental", [1, 2, 3, 4, 5])
f6 = st.radio("Genre Variety", [1, 2, 3, 4, 5])

# Predict button
if st.button("Predict"):
    # Combine inputs into array
    input_data = np.array([[f1, f2, f3, f4, f5, f6]])

    # Predict using the model
    prediction = dtm_model.predict(input_data)

    # Dummy labels for predicted classes (adjust as per your model)
    music_types = ["1", "2", "3", "4", "5", "6"]

    try:
        st.success(f"🎵 Recommended Music Type: **{music_types[prediction[0]]}**")
    except IndexError:
        st.error("Prediction index out of range. Please check your model output or labels.")





