# Example 3 

import streamlit as st
import plotly.express as px
import pandas as pd

# Load Sample Data
df = px.data.gapminder()

# Title of the app
st.title("Interactive Dashboard with Multiple Plots")

# Select Year with Slider
year = st.slider("Select Year:", int(df["year"].min()), int(df["year"].max()), int(df["year"].min()),step = 5)


# Filter Data
filtered_df = df[df["year"] == year]

# Create three different plots t
fig1 = px.scatter(filtered_df, x = "gdpPercap", y = "lifeExp", size = "pop", color = "continent",
                 hover_name = "country", log_x = True, size_max = 60, title = "Life Expectancy vs GDP ")

fig2 = px.scatter(filtered_df, x = "continent", y = "pop", color = "continent", title = "Population per Continent ")

fig3 = px.scatter(filtered_df, x = "country", y = "gdpPercap", color = "continent", title = "GDP Per Capita by Country ")

# Arrange the plots in a grid layout 
col1, col2= st.columns(2) # create 2 columns 

with col1:
    st.plotly_chart(fig1, use_container_width = True)

with col2:
    st.plotly_chart(fig2, use_container_width = True)

# Add the third plot in a full-width row below 
st.plotly_chart(fig3, use_container_width = True)

# COPY and PASTE all of the above from this cell into the github repository
