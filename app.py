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
st.title("🎶 Music Recommendation System")
st.write("Please select your preferences for the following music-related features:")

# Define options (adjust if needed)
options = [1, 2, 3, 4, 5]  # Or use descriptive values if applicable

# Create 16 radio buttons
f1 = st.radio("🎧 Feature 1: Rhythm", options)
f2 = st.radio("🎧 Feature 2: Melody", options)
f3 = st.radio("🎧 Feature 3: Tempo", options)
f4 = st.radio("🎧 Feature 4: Energy", options)
f5 = st.radio("🎧 Feature 5: Danceability", options)
f6 = st.radio("🎧 Feature 6: Acousticness", options)
f7 = st.radio("🎧 Feature 7: Instrumentalness", options)
f8 = st.radio("🎧 Feature 8: Vocal Clarity", options)
f9 = st.radio("🎧 Feature 9: Lyrics Depth", options)
f10 = st.radio("🎧 Feature 10: Genre Familiarity", options)
f11 = st.radio("🎧 Feature 11: Mood Preference", options)
f12 = st.radio("🎧 Feature 12: Popularity Tolerance", options)
f13 = st.radio("🎧 Feature 13: Repetition Tolerance", options)
f14 = st.radio("🎧 Feature 14: Complexity Preference", options)
f15 = st.radio("🎧 Feature 15: Loudness Tolerance", options)
f16 = st.radio("🎧 Feature 16: Genre Variety", options)

# Predict button
if st.button("Predict"):
    # Combine all features into an input array
    input_data = np.array([[f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16]])

    try:
        prediction = dtm_model.predict(input_data)
        music_types = ["1", "2", "3", "4", "5", "6"]
        st.success(f"🎵 Recommended Music Type: **{music_types[prediction[0]]}**")
    except IndexError:
        st.error("Prediction index out of range. Check your model output or class labels.")
    except Exception as e:
        st.error(f"An error occurred: {e}")






