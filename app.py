import streamlit as st
import pandas as pd

st.title('Análisis Simple de Datos')

st.write('Cargando datos ...')

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

st.write('Primeros 5 registros del data dataset: ')
st.write(df.head())

st.write('Resumen estadístico')
st.write(df.describe())

especies = st.selectbox('Selecciona una especie', df['species'].unique())
st.write(df[df['species'] == especies])
