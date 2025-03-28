import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header('Análisis de Datos de Vehículos')

# Crear un botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma de la columna 'odometer'
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para odómetro vs precio')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

# Desafío adicional: Casillas de verificación para elegir qué gráfico mostrar
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
    # Crear el histograma de la columna 'odometer'
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # Si la casilla está seleccionada
    st.write('Construir un gráfico de dispersión para odómetro vs precio')
    
    # Crear el gráfico de dispersión
    fig_scatter_check = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter_check, use_container_width=True)
