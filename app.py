import streamlit as st
import numpy as np
from model import train

# Title
st.title("Hello World AI App")
st.subheader("A simple regression model")

# Train model
model = train()

# Sidebar
st.sidebar.header("Input features")
input_value = st.sidebar.slider("Select value of x", 1, 10, 5)

# Prediction
input_array = np.array([[input_value]])
prediction = model.predict(input_array)

st.write(f"Input value : {input_value}")
st.write(f"Output value: {prediction[0]:.2f}")