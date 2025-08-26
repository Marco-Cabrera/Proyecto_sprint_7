import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')
disp_button = st.button('Construir Diagrama de dispersión')

if hist_button:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig = go.Figure(data=[go.Histogram(x=df['odometer'])])
        st.plotly_chart(fig, use_container_width=True)

if disp_button:
        st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
        fig = px.scatter(
        df,
        x="odometer", # Eje X
        y="price"     # Eje Y
        )   
        st.plotly_chart(fig, use_container_width=True)

