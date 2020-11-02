import numpy as np
from plotly import figure_factory as ff
import streamlit as st
import plotly.graph_objects as go


def app():
    # Set header and subheader of the app
    st.header('Google Analytics')
    st.subheader(
        "Summary stats of consumer behaviour from Google Analytics data.")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Plot a side-by-side bar chart using plotly
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months,
        y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
        name='B2B sales',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=months,
        y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
        name='B2C sales',
        marker_color='lightsalmon'
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

    # Create 2 different pie charts using plotly
    labels1 = ['Desktop', 'Mobile', 'Tablet']
    labels2 = ['New Users', 'Returning', 'Undefined']
    values1 = [4500, 2500, 1053]
    values2 = [2500, 1500, 2360]

    fig2 = go.Figure(data=[go.Pie(labels=labels1, values=values1)])
    fig3 = go.Figure(data=[go.Pie(labels=labels2, values=values2)])

    # Create two columns and display each pie chart on a different col
    col1, col2 = st.beta_columns(2)
    with col1:
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        st.plotly_chart(fig3, use_container_width=True)
