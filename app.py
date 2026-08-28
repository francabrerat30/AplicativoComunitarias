import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Ruta Petrolera Ancón",
    page_icon="🛢️",
    layout="wide"
)
st.markdown("""
    <style>
    /* Aumenta el tamaño del título de la barra lateral */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
        font-size: 26px !important;
    }
    
    /*Aumenta el tamaño de los textos y opciones de navegación */
    [data-testid="stSidebar"] .stRadio label p {
        font-size: 18px !important;
        font-weight: 500:
    }
    </style>
""", unsafe_allow_html=True)

# --- Navegación y Menú Lateral ---
st.sidebar.title("🛢️ Ruta Ancón")
st.sidebar.markdown("---")
opcion = st.sidebar.radio("Navegación", ["Inicio", "Pozos Patrimoniales", "Dashboard Interactivo", "Agendar Visita"])

# Sección: Inicio (Pantalla de Bienvenida)
if opcion == "Inicio":
    # Encabezado con logos institucionales
    col_logo1, col_titulo, col_logo2 = st.columns([2, 5, 2])

    with col_logo1:
        st.image("assets/Espol_Logo.png", use_container_width=True)

    with col_titulo:
        st.markdown(
            "<h2 style='text-align: center; color: #1B3B48; margin-bottom: 0; '>Ruta Patrimonial de la Cuna del Petróleo Ecuatoriano</h2>",
            unsafe_allow_html=True
        )
    with col_logo2:
        st.image("assets/gad_ancon.png", use_container_width=True)

    st.divider()

    #Banner de la ruta
    st.image("assets/Balacin.png", use_container_width=True, caption="Pozo Ancón 1 y paisaje Patrimonial")

    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Año de Descubrimiento", value="1911")
    with col2:
        st.metric(label="Pozo Emblemático", value="Ancón 1")
    with col3:
        st.metric(label="Ubicación", value="Santa Elena, Ec")
    with col4:
        st.metric(label="Estado del Campo", value="Activo / Patrimonial")

    st.markdown("---")

    #Información en columnas interactivas
    col_izq, col_der = st.columns([2 ,1])

    with col_izq:
        st.markdown("### 📌 Sobre la Ruta Turística")
        st.write("""
        Esta aplicación fue desarrollada como parte de un proyecto comunitaria para **fomentar el turismo patrimonial e industrial** en la parroquia San José de Ancón.
        
        A través de esta plataforma interactiva podrás:
        * **Explorar el catálogo de pozos activos e históricos** con su ficha técnica y ubicación geográfica.
        * **Analizar indicadores clave de producción e historia** a través de un Dashboard en Power BI.
        * **PLanificar tu recorrido guiado** mediante el mapa de navegación oficial.
        """)

        st.info("💡 **Dato Curioso:** El Pozo Ancón 1 marcó el inicio de la era petrolera industrial en el Ecuador el 5 de noviembre de 1911.")

    with col_der:
        st.markdown("### 🗺️ Acceso Rápido")
        st.success("✔ **Guía turística interactiva** disponible 24/7.")
        st.warning("📍 **Ubicación:** Parroquia Ancón, Península de Santa Elena.")

        #Botón informativo
        st.markdown("### ¿Listo para explorar?")
        st.write("Utiliza el menú lateral para navegar por los diferentes módulos de la plataforma.")




    # -- SECCION: RUTA Y POZOS PETROLEROS ---
elif opcion == "Pozos Patrimoniales":
    st.header("🗺️ Ruta Patrimonial en Google Maps")
    st.write("Sigue el mapa oficial diseñado para el recorrido turístico e histórico en Ancón:")

    # Enlace/Botón a Google Maps
    google_maps_url = "https://maps.app.goo.gl/c5AzUDDup22AFMGw9?g_st=ic"
    st.link_button("📍 Abrir Ruta Completa en Google Maps", google_maps_url, type="primary")

    st.markdown("---")

    st.header("🛢️ Catálogo e Historia de los Pozos Petroleros")
    st.write("Selecciona un pozo o punto de interés para conocer su historia y ver su estado actual.")

    # Diccionario de datos de los pozos
    pozos = {
        "Pozo Ancón 1 (Ancón N° 1)":{
            "estado": "Hito Histórico Patrimonial",
            "historia": """
                Perforado el 5 de noviembre de 1911, es el primer pozo petrolero comercial del Ecuador.
                Representa el nacimiento de la industria hidrocarburífera en el país y marca el inicio
                del desarrollo urbano y social del campamento de Ancón.
                """,
            "imagen": "assets/PozoAncon1.png" # URL de ejemplo
        },
        "Pozo Activo - Balancín en Producción":{
            "estado": "En Producción Activa",
            "historia": """
                Este pozo cuenta con un sistema de extracción por bombeo mecánico (balancín o 'nodding donkey').
                Demuestra cómo la extracción tradicional se mantiene operativa y eficiente tras décadas de operación en la cuenca.
                """,
            "imagen": "assets/Balacin.png"  # URL de ejemplo
        },
        "Campamento Inglés / Zona Patrimonial":{
            "estado": "Patrimonio Arquitectónico e Industrial",
            "historia": """
                Sector que conserva la arquitectura de estilo colonial e inglés traída por los administradores
                de la Anglo Ecuadorian Oilfields. Es un testimonio vivo del estilo de vida y la organización social de la época.
                """,
            "imagen": "assets/barrioIngles.jpg"  # URL de ejemplo
        }
    }

    # Selector interactivo de pozos
    pozo_seleccionado = st.selectbox("Selecciona un pozo o punto de la ruta:", list(pozos.keys()))

    # Mostrar la información del pozo seleccionado
    datos = pozos[pozo_seleccionado]

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(pozo_seleccionado)
        st.badge(datos["estado"])
        st.write("### Historia y Relevancia:")
        st.write(datos["historia"])

    with col2:
        st.write("### Imagen Actual / Estado:")
        st.image(datos["imagen"], caption=f"{pozo_seleccionado}", use_container_width=True)

# --- SECCION: DASHBOARD INTERACTIVO ---
elif opcion == "Dashboard Interactivo":
    st.header("📊 Dahsboard de Control y Análisis - Ancón")
    st.write("Explora las métricas e indicadores de la ruta patrimonial y pozos petroleros.")

    powerbi_url = "https://app.powerbi.com/links/T1PFX9DnUw?ctid=b7af8caf-83d8-4644-85ae-317c545223c1&pbi_source=linkShare"
    components.iframe(src=powerbi_url, width=1100, height=600, scrolling=True)

# --- SECCION: AGENDAR VISITA ---
elif opcion == "Agendar Visita / Schedule Visit":
    st.header("📋 Registro de Visitantes")
    st.write("Completa el formulario para agendar una visita guiada con la comunidad de Ancón.")

    with st.form("form_visita"):
        nombre = st.text_input("Nombre completo / Name and Last name:")
        correo = st.text_input("Correo electrónico / email:")
        tipo = st.selectbox("Tipo de visitante / type of visitor:", ["Turista / tourist", "Estudiante (student) / Universidad (university)", "Investigador / researcher", "Otro / others"])
        enviado = st.form_submit_button("Registrar Visita")
        if enviado:
            st.success(f"¡Gracias {nombre}! Tu solicitud para la Ruta Patrimonial ha sido registrada.")

