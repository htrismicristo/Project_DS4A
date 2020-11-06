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
    X = pd.read_csv('datos_cluster.csv')
    fig = px.scatter_3d(X, x='dias_ultima_compra', y='monto', z='frecuencia',
                        color='cluster')

    # Display the plotly figure
    st.plotly_chart(fig, use_container_width=True)
