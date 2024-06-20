import pandas as pd
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #4f3fbc;'>Dashboard de Dados da COVID-19 no Rio de Janeiro</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #4f3fbc'>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

largura_coluna1 = 350
altura_coluna1 = 500
largura_coluna2 = 500
altura_coluna2 = 500


col1, col2 = st.columns([largura_coluna1, largura_coluna2])

with col1:
    st.markdown("<h3 style='text-align: center; font-size: 18px; color: #4f3fbc;'>Mapa do Rio de Janeiro com Pontos</h3>", unsafe_allow_html=True)
    df = pd.read_csv('/content/dados2.csv')
    df_cleaned = df.dropna(subset=['lat', 'lon'])

    center_lat, center_lon = -22.9068, -43.1729
    m = folium.Map(location=[center_lat, center_lon], zoom_start=11, control_scale=True, width='90%', height=600, use_container_width=True)

    heat_data = [[row['lat'], row['lon']] for index, row in df_cleaned.iterrows()]

    HeatMap(heat_data).add_to(m)

    folium_static(m)
with col2:
    grafico_evolucao_width = 325
    grafico_evolucao_height = 35

    grafico_evolucao2_width = 325
    grafico_evolucao2_height = 35

    grafico_barra1_width = 290
    grafico_barra1_height = 30

    grafico_pizza_width = 160
    grafico_pizza_height = 30

    grafico_barra2_width = 290
    grafico_barra2_height = 30

    grafico_barra3_width = 300
    grafico_barra3_height = 32

    grafico_barra4_width = 280
    grafico_barra4_height = 30

    col_graficos_evolucao = st.columns([1,1])
    with col_graficos_evolucao[0]:
        st.image('/content/grafico_evolucao.png', width=grafico_evolucao_width, use_column_width=False)
    with col_graficos_evolucao[1]:
        st.image('/content/grafico_evolucao2.png', width=grafico_evolucao2_width, use_column_width=False)

    col_outros_graficos = st.columns([1,1,1])
    with col_outros_graficos[0]:
        st.image('/content/grafico_barra1.png', width=grafico_barra1_width, use_column_width=False)
    with col_outros_graficos[1]:
        st.image('/content/grafico_pizza.png', width=grafico_pizza_width, use_column_width=False)
    with col_outros_graficos[2]:
        st.image('/content/grafico_barra2.png', width=grafico_barra2_width, use_column_width=False)

    col_graficos_barras = st.columns([1,1])
    with col_graficos_barras[0]:
        st.image('/content/grafico_barra3.png', width=grafico_barra3_width, use_column_width=False)
    with col_graficos_barras[1]:
        st.image('/content/grafico_barra4.png', width=grafico_barra4_width, use_column_width=False)
