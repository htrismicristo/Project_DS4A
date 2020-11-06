# Import required libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def app():
    # Set the header and subheader of the app
    st.header('Customer Segmentation')
    st.subheader(
        "Ceramica Italia's Customers segmentation based on purchasing history.")

    # import the data
    df = px.data.iris()

    fig = go.Figure(data=[go.Scatter3d(x=df['sepal_width'],
                                       y=df['sepal_length'],
                                       z=df['petal_length'],
                                       mode='markers',
                                       marker=dict(
        size=12,
        color=df['petal_width'],
        colorscale='Viridis',
        opacity=0.8
    )
    )])

    # Display the plotly figure
    st.plotly_chart(fig, use_container_width=True)
