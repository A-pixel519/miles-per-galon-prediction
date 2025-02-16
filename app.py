
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("miles per galon predictor")

# input widget for getting user values for X (feature matrix value)
price = st.slider("acceleration", min_value=0, max_value=100, value=20)
horsepower = st.slider("weight", min_value=0, max_value=100, value=20)
eng_size = st.slider("cylinders", min_value=0, max_value=100, value=20)

# After selesting price, the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[price, horsepower, eng_size]])[0].round(2)
  st.write("The predicted miles per galon of your car is", prediction, "mpg")
