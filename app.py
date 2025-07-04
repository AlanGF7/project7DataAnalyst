import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de vehículos utilizados en Estados Unidos")

car_data = pd.read_csv('vehicles_us.csv')

build_histogram = st.checkbox('Mostrar histograma')

if build_histogram:
    st.write('Creación de un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: "odometer" vs "price"')
    fig2 = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="type",
        hover_data=["model_year"]
    )
    st.plotly_chart(fig2, use_container_width=True)
