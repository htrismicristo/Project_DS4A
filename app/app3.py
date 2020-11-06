# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:22:55 2020

@author: David
"""
import numpy as np
from plotly import figure_factory as ff
import streamlit as st
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from folium.plugins import HeatMap
import pandas as pd
import branca.colormap as cmp


def app():
    df_total = pd.read_csv("sales_grouped.csv")
    df_date = pd.read_csv("sales_grouped_date.csv")
    st.write("""
    # Ceramica italia Sales
    Number of sales per city 
    """)

    def rad_size(number):
        if number < 10:
            return 2, '#fef0d9'
        elif 10 <= number and number < 100:
            return 5, '#fec44f'
        elif 100 <= number and number < 500:
            return 10, '#ffff33'
        elif 500 <= number and number < 1000:
            return 15, '#ff7f00'
        else:
            return 20, '#de2d26'

    year_to_filter = st.slider('year', 2010, 2020, 2010)
    df_date['year'] = pd.to_datetime(df_date['DATE']).dt.strftime('%Y')

    df_year = df_date[df_date['year'] == str(year_to_filter)]
    df_year_map = df_year[['Ciudad', 'lat', 'lon', 'sales']].groupby(
        ['Ciudad', 'lat', 'lon']).sum().reset_index()

    if st.button('Total sales'):
        df = df_total

        st.subheader('Map of total sales (2010-2020)  ')

    else:
        df = df_year_map

        st.subheader('Map of all sales in' + str(year_to_filter))

    Total = df['sales'].sum()
    st.subheader(' Total sales = ' + str(Total))
#     Total = df['sales'].sum()

    lat = list(df["lat"])
    lon = list(df["lon"])
#     Percentile = list(df_year_map["Percentile"])
    sales = list(df["sales"])
    ciudad = list(df["Ciudad"])

    base_map = folium.Map(location=[4.710989, -74.072092], zoom_start=5)
    linear = cmp.LinearColormap(
        ['#fef0d9', '#fec44f', '#ffff33', '#ff7f00', '#de2d26'],
        index=[0, 100, 500, 1000, 3000],
        vmin=1, vmax=3000,
        caption='Number of Sales'  # Caption for Color scale or Legend
    )
    fg = folium.FeatureGroup(name="My Map")
    for lt, ln, sale, ciu in zip(lat, lon, sales, ciudad):
        fg.add_child(folium.CircleMarker(location=[lt, ln], radius=rad_size(sale)[0], popup=str(ciu)+" \n number of sales:"+str(sale),
                                         fill_color=rad_size(sale)[1], fill=True, fill_opacity=0.7, color='Black', opacity=0.4))

    base_map.add_child(fg)

    # call to render Folium map in Streamlit
    linear.add_to(base_map)
    folium_static(base_map)
