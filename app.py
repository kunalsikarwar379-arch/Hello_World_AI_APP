import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Hello World AI App")

# Simple training data: y = 2x + 1
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression()
model.fit(X, y)

value = st.slider("Pick a value", 0, 20, 5)
prediction = model.predict([[value]])[0]

st.write(f"Predicted output: **{prediction:.2f}**")