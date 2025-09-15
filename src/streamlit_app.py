import streamlit as st
import pandas as pd
import geopandas as gpd


# Configuración inicial

st.set_page_config(
    page_title="Acceso Hospitales Perú",
    page_icon="🏥",
    layout="wide"
)


# Pestañas principales

tab1, tab2, tab3 = st.tabs(["🗂️ Descripción de los Datos", "🗺️ Mapas Estáticos", "🌍 Mapas Dinámicos"])


# Pestaña 1: Descripción de los datos

with tab1:
    st.header("Descripción de los Datos")
    st.markdown("""
    **Unidad de análisis:** Hospitales públicos operativos en el Perú  
    **Fuentes de datos:** MINSA – IPRESS (subconjunto operativo), Centros Poblados (CCPP – IGN)  
    **Reglas de filtrado:** Solo hospitales operativos con latitud y longitud válidas  
    """)

    # Cargar resumen departamental
    dept_summary = pd.read_csv("output/dept_summary.csv")

    st.subheader("Tabla Resumen por Departamento")
    st.dataframe(dept_summary)

    st.markdown("### Gráfico de barras por departamento")
    st.image("output/dept_barras.png", caption="Número de hospitales por departamento")


# Pestaña 2: Mapas estáticos

with tab2:
    st.header("📊 Mapas estáticos y análisis departamental")


    st.markdown("### Mapa 1: Hospitales por distrito")
    st.image("output/Coropleta_Distrital.png")

    st.markdown("### Mapa 2: Distritos sin hospitales")
    st.image("output/distritos_sin_hosp.png")

    st.markdown("### Mapa 3: Top 10 distritos con más hospitales")
    st.image("output/top10_distritos.png")


# Pestaña 3: Mapas dinámicos

with tab3:
    st.header("Mapas Dinámicos")

    # Coropleta nacional con marcadores
    st.markdown("### Coropleta + Marcadores")
    st.components.v1.html(open("output/Coropleta_Distrital.html", "r", encoding="utf-8").read(), height=600)

    # Mapas de proximidad
    st.markdown("### Proximidad - Lima")
    col1, col2 = st.columns(2)
    with col1:
        st.components.v1.html(open("output/Lima_min.html", "r", encoding="utf-8").read(), height=400)
    with col2:
        st.components.v1.html(open("output/Lima_max.html", "r", encoding="utf-8").read(), height=400)

    st.markdown("### Proximidad - Loreto")
    col3, col4 = st.columns(2)
    with col3:
        st.components.v1.html(open("output/Loreto_min.html", "r", encoding="utf-8").read(), height=400)
    with col4:
        st.components.v1.html(open("output/Loreto_max.html", "r", encoding="utf-8").read(), height=400)
