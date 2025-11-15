import streamlit as st

def read_markdown_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


image_path = "fuentes/imagenes/logo.jpg"

# Botón para abrir la imagen en un popup
@st.dialog("kldjfl")
def imagen():
    if st.button("Ver imagen"):
        st.image("fuentes/imagenes/logo.jpg")

tab1_content = read_markdown_file("fuentes/imagenes/ver.md")
tab1, tab2 = st.tabs(["Markdown Tab", "Other Tab"])

with tab1:
    st.markdown(tab1_content)
    # Enlace usando `st.write()` con formato Markdown
    # Enlace en imagen usando Markdown
    st.markdown("[![Texto alternativo](fuentes/imagenes/internet.jpg)](https://www.google.com)")


with tab2:
    st.write("This is tab2!")
    #imagen()
    st.markdown(
        '''
        <a href='https://www.google.com' target='_blank'>
            <img src='https://ideogram.ai/assets/progressive-image/balanced/response/4NvwvnJlTseI9yyqDxw_vg' alt='Imagen 3' width='150'>
        </a>
        ''',
        unsafe_allow_html=True
    )
