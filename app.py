import streamlit as st

st.set_page_config(
    page_title="Curso OSI",
    page_icon="👋",
    initial_sidebar_state="collapsed", # Key parameter here
    layout="wide", # Optional: can also set layout to "wide"

)

st.logo("fuentes/imagenes/rojo.png")
st.subheader(f" 📥 *CURSO DE OPERADOR DE SISTEMAS INFORMÁTICOS*")

def run_app():

    pages = {
    " 🗁  DIRECTORIO RAIZ ": [
        st.Page("home.py", title="Home", icon="💼"),
        st.Page("trabajo.py", title="Trabajo", icon="🚧"),



    ],
    "🗁  PAGINAS ": [

        st.Page("pages/playground.py", title="Patio de juegos", icon="🚧"),
        st.Page("fuentes/tools/colores.py", title="Colores", icon="🎨"),

    ],
    }

    pg = st.navigation(pages)
    pg.run()

if __name__ == '__main__':
    run_app() # Ejecutas la función que contiene pg.run()


