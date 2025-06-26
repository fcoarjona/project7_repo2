# import packages
import pandas as pd
import streamlit as st
import plotly.express as px

# Read de csv file
vehicles = pd.read_csv("vehicles_us.csv")
st.header("Vehicles for you") # Title of the app
st.markdown("What are you looking for when youwant to buy a car?") # Subtitle of the app

# Creating charts with Plotly
hist_button = st.button("Show histogram")
if hist_button:
    st.write("Built and displayed a histogram")
    st.markdown("***The type you like most, and how much they have run***")
    fig = px.histogram(vehicles, title="Type vs Km", x="type", y="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Show scatter plot")
if scatter_button:
    st.write("Built and displayed a scatter plot")
    fig = px.scatter(vehicles, x="model", y="price", color="condition")
    event = st.plotly_chart(fig, key="iris", on_select="ignore", selection_mode="Iterable", use_container_width=False)
    event.selection
