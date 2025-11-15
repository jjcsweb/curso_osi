import streamlit as st
import os

ruta_archivo = ""
def div_green():
    st.markdown(
        "<hr style='border:1px solid #4CAF50; border-radius:1px;'>",
        unsafe_allow_html=True)
def div_blue():
    st.markdown(
        "<hr style='border:1px solid #3B66D4; border-radius:3px;'>",
        unsafe_allow_html=True)

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, "r") as file:
        contenido = file.read()
        # Renderiza el contenido en la aplicación Streamlit
        st.markdown(contenido)

