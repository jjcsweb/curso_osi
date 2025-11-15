import streamlit as st

# 1. ⚙️ Inicialización del Estado de Sesión
if 'mi_color' not in st.session_state:
    st.session_state.mi_color = '#00f900'


# 2. 💾 Función de Callback
def guarda_color():
    # El valor del color_picker se mueve a la variable principal
    st.session_state.mi_color = st.session_state.picker_valor
    # Opcional: st.toast es útil para confirmar la acción, pero no es crítico
    st.toast("Color guardado. Recargando la página...")


# 3. 🖼️ Definición del Diálogo
@st.dialog("🎨 Elegir Color HEX")
def elige_color():
    color_actual = st.session_state.mi_color

    # Renderizamos el widget con la clave
    st.color_picker(
        "Elige un nuevo color:",
        value=color_actual,
        key="picker_valor"  # Su valor es accesible como st.session_state.picker_valor
    )

    # Botón que desencadena la acción
    if st.button("Guardar y Cerrar", on_click=guarda_color):
        # NOTA CLAVE: st.stop() detiene la ejecución del DIÁLOGO inmediatamente
        # después del callback. La re-ejecución total del script es manejada
        # por Streamlit debido al cambio en st.session_state.
        st.stop()

    # --- Contenido Principal de la Aplicación ---


st.write(f"#### Aplicación de Selección de Color")

# 4. 🖲️ Botón para Abrir el Diálogo
if st.button('Abrir Selector de Color'):
    elige_color()

st.divider()

# 5. 📊 Uso del Dato Guardado (se renderiza correctamente después del guardado)
color_seleccionado = st.session_state.mi_color

st.subheader("Resultado")
st.write(f"El color seleccionado es: **{color_seleccionado}**")
st.write(
    f"Tipo de dato: `{type(color_seleccionado).__name__}` ({color_seleccionado} es una **cadena de texto** con formato HEX)")

# Demostración práctica
st.markdown(
    f"""
    <div style='background-color: {color_seleccionado}; padding: 10px; border-radius: 5px; color: black;'>
        **Muestra del Color:** {color_seleccionado}
    </div>
    """,
    unsafe_allow_html=True
)