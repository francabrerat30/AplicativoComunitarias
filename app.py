import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Ruta Petrolera Ancón",
    page_icon="🛢️",
    layout="wide"
)

#Encabezado principal
st.title("🛢️ Ruta Patrimonial: Los Pozos Petroleros de Ancón")

# Menú Lateral
st.sidebar.header("Navegación")
opcion = st.sidebar.radio(
    "Selecciona una sección:",
    ["Inicio", "Ruta y Pozos Petroleros", "Dashboard Interactivo", "Agendar Visita" ]
)

# --- SECCION: INICIO ---
if opcion == "Inicio":
    st.header("Bienvenido a Ancón: Cuna Petrolera del Ecuador")
    st.write(
        """
        Esta plataforma de turismo comunitario promueve el reconocimiento de la historia
        y el patrimonio industrial de Ancón a través de un recorrido interactivo por sus
        pozos petroleros históricos y activos.
        """
    )
    st.info("💡 **Dato clave:** En Ancón conviven la historia pionera de la extracción petrolera en el país y operaciones que continúan activas hasta el día de hoy.")

    # -- SECCION: RUTA Y POZOS PETROLEROS ---
elif opcion == "Ruta y Pozos Petroleros":
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
elif opcion == "Agendar Visita":
    st.header("📋 Registro de Visitantes")
    st.write("Completa el formulario para agendar una visita guiada con la comunidad de Ancón.")

    with st.form("form_visita"):
        nombre = st.text_input("Nombre completo:")
        correo = st.text_input("Correo electrónico:")
        tipo = st.selectbox("Tipo de visitante:", ["Turista", "Estudiante / Universidad", "Investigador", "Otro"])
        enviado = st.form_submit_button("Registrar Visita")
        if enviado:
            st.success(f"¡Gracias {nombre}! Tu solicitud para la Ruta Patrimonial ha sido registrada.")

