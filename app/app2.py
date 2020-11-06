import numpy as np
import pandas as pd
import plotly
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


def app():
    # Set header and subheader of the app
    st.header('Google Analytics')
    st.subheader(
        "Summary stats of consumer behaviour from Google Analytics data.")

    # ADWORDS BY NATALI
    # Times
    st.subheader("ADWORDS")
    st.write("Times of the day when Adwords ads are most effective")
    adwordsbyhour = st.cache(pd.read_csv)("AdwordsByHour.csv")
    is_check = st.checkbox("Display Data")
    if is_check:
        st.write(adwordsbyhour)

    horario = adwordsbyhour['Hora']
    sesion = adwordsbyhour['Sesiones']
    fig4 = go.Figure(data=[go.Pie(labels=horario, values=sesion)])
    st.plotly_chart(fig4, use_container_width=True)

    # searches
    st.subheader("SEARCHES")
    st.write("Most searched words")
    adwords1 = st.cache(pd.read_csv)("Adwords1.csv")
    is_check1 = st.checkbox("Display Searches")
    if is_check1:
        st.write(adwords1)
    st.bar_chart(adwords1.ConsultaBusqueda)

    # placements
    st.subheader("PLACEMENTS")
    st.write("Most effective placement URLs")
    adwords3 = st.cache(pd.read_csv)("Adwords3.csv")
    is_check3 = st.checkbox("Display Table")
    if is_check3:
        st.write(adwords3)
    adwords3 = adwords3[~adwords3['URL del emplazamiento'].astype(
        str).str.startswith('mobileapp::')]

    url = [adwords3[i]
           for i in adwords3.columns if 'URL del emplazamiento' in i]
    df_url = pd.concat(url).reset_index()
    df_url = df_url.rename(columns={0: 'Urls'})
    rurl = df_url.groupby(
        by=['index', 'URL del emplazamiento']).count().reset_index()
    rulr = rurl.groupby('URL del emplazamiento').agg(
        'count').sort_values('index', ascending=False).head(10)

    col3, col4 = st.beta_columns(2)
    with col3:
        st.write(rulr)
    with col4:
        st.bar_chart(rulr)

    # days
    st.subheader("WEEKDAYS")
    st.write("Ads effectiveness by day of the week.")
    adwords2 = st.cache(pd.read_csv)("Adwords2.csv")
    st.bar_chart(adwords2.day)

   # Wilson's charts
    system_rebote = pd.read_csv('./system_rebote.csv', sep=',')
    system_clean_f = pd.read_csv('./system_clean_f.csv', sep=',')
    metrics = ['1 Day', '3 Days', '1 Week',
               '1 Month', '3 Months', '6 Months', '1 Year']
    cols = st.selectbox('Time range to watch', metrics)
    # let's ask the user which column should be used as Index
    if cols in metrics:
        range_time_to_show = cols
        if(cols == '1 Day'):
            number_of_days = 2
        elif(cols == '3 Days'):
            number_of_days = 6
        elif(cols == '1 Week'):
            number_of_days = 14
        elif(cols == '1 Month'):
            number_of_days = 60
        elif(cols == '3 Months'):
            number_of_days = 180
        elif(cols == '6 Months'):
            number_of_days = 360
        else:
            number_of_days = 720
    # p rebote
    p_rebote_lastest_w = system_rebote.groupby('Date')['Porcentaje de rebote'].mean(
    ).reset_index().sort_values('Date', ascending=False).head(number_of_days)

    p_robote_today = ((p_rebote_lastest_w['Porcentaje de rebote'].iloc[0:int(number_of_days/2)].mean(
    )/p_rebote_lastest_w['Porcentaje de rebote'].iloc[int(number_of_days/2):int(number_of_days)].mean())*100)-100
    st.markdown('**Bounce Rate:**')

    # st.write("<style>red{color:red} orange{color:orange}....</style>)
    # color = st.color_picker('Pick A Color', '#00f900')
    st.write(round(p_robote_today, 2), '%')
    fig = px.bar(p_rebote_lastest_w.head(int(number_of_days/2)), x='Date',
                 y='Porcentaje de rebote', color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig, use_container_width=True)
    # sessions
    p_sessions_lastest_w = system_clean_f.groupby('Date')['Sesiones'].sum(
    ).reset_index().sort_values('Date', ascending=False).head(number_of_days)
    p_sessions_today = ((p_sessions_lastest_w['Sesiones'].iloc[0:int(number_of_days/2)].mean(
    )/p_sessions_lastest_w['Sesiones'].iloc[int(number_of_days/2):int(number_of_days)].mean())*100)-100
    st.markdown('**Sessions:**')
    st.write(round(p_sessions_today, 2), '%')
    fig2 = px.bar(p_sessions_lastest_w.head(int(number_of_days/2)), x='Date',
                  y='Sesiones', color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig2, use_container_width=True)
    # average pageviews
    p_pageviews_lastest_w = system_clean_f.groupby('Date')['Número de páginas vistas'].mean(
    ).reset_index().sort_values('Date', ascending=False).head(number_of_days)
    p_pageviews_today = ((p_pageviews_lastest_w['Número de páginas vistas'].iloc[0:int(number_of_days/2)].mean(
    )/p_pageviews_lastest_w['Número de páginas vistas'].iloc[int(number_of_days/2):int(number_of_days)].mean())*100)-100
    st.markdown('**Average Pageviews:**')
    st.write(round(p_pageviews_today, 2), '%')
    fig3 = px.bar(p_pageviews_lastest_w.head(int(number_of_days/2)), x='Date',
                  y='Número de páginas vistas', color_discrete_sequence=px.colors.qualitative.Dark2)
    st.plotly_chart(fig3, use_container_width=True)
