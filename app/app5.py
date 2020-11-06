#import s3fs
#install plotly.express
#install streamlit
# Importando las librerías requeridas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm
import streamlit as st
import plotly.express as px

def app():
    system_rebote =pd.read_csv("system_rebote.csv", sep = ',')
    system_clean_f=pd.read_csv("system_clean_f.csv", sep = ',')
    # Set header and subheader of the app
    st.header('Navigation Analysis')

    ###Time Selection
    metrics =['1 Day','3 Days','1 Week','1 Month','3 Months','6 Months', '1 Year']
    cols = st.selectbox('Time range to watch', metrics)
    # let's ask the user which column should be used as Index
    if cols in metrics:   
        range_time_to_show = cols
        if(cols=='1 Day'):
            number_of_days=2
        elif(cols=='3 Days'):
            number_of_days=6
        elif(cols=='1 Week'):
            number_of_days=14
        elif(cols=='1 Month'):
            number_of_days=60
        elif(cols=='3 Months'):
            number_of_days=180
        elif(cols=='6 Months'):
            number_of_days=360
        else:
            number_of_days=720
    ##p rebote
    p_rebote_lastest_w=system_rebote.groupby('Date')['Porcentaje de rebote'].mean().reset_index().sort_values('Date',ascending=False).head(number_of_days)

    p_robote_today=((p_rebote_lastest_w['Porcentaje de rebote'].iloc[0:int(number_of_days/2)].mean()/p_rebote_lastest_w['Porcentaje de rebote'].iloc[int(number_of_days/2):int(number_of_days)].mean())*100)-100
    st.markdown('**Bounce Rate:**')

    #st.write("<style>red{color:red} orange{color:orange}....</style>)
    #color = st.color_picker('Pick A Color', '#00f900')
    st.write(round(p_robote_today,2),'%')
    fig = px.bar(p_rebote_lastest_w.head(int(number_of_days/2)), x='Date', y='Porcentaje de rebote',color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig, use_container_width=True)
    ##sessions
    p_sessions_lastest_w=system_clean_f.groupby('Date')['Sesiones'].sum().reset_index().sort_values('Date',ascending=False).head(number_of_days)
    p_sessions_today=((p_sessions_lastest_w['Sesiones'].iloc[0:int(number_of_days/2)].mean()/p_sessions_lastest_w['Sesiones'].iloc[int(number_of_days/2):int(number_of_days)].mean())*100)-100
    st.markdown('**Sessions:**')
    st.write(round(p_sessions_today,2),'%')
    fig2 = px.bar(p_sessions_lastest_w.head(int(number_of_days/2)), x='Date', y='Sesiones',color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig2, use_container_width=True)
##average pageviews
    p_pageviews_lastest_w=system_clean_f.groupby('Date')['Número de páginas vistas'].mean().reset_index().sort_values('Date',ascending=False).head(number_of_days)
    p_pageviews_today=((p_pageviews_lastest_w['Número de páginas vistas'].iloc[0:int(number_of_days/2)].mean()/p_pageviews_lastest_w['Número de páginas vistas'].iloc[int(number_of_days/2):int(number_of_days)].mean())*100)-100
    st.markdown('**Average Pageviews:**')
    st.write(round(p_pageviews_today,2),'%')
    fig3 = px.bar(p_pageviews_lastest_w.head(int(number_of_days/2)), x='Date', y='Número de páginas vistas',color_discrete_sequence=px.colors.qualitative.Dark2)
    st.plotly_chart(fig3, use_container_width=True)
