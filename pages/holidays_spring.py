import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages, add_page_title

def main():
    login_sidebar_ASL1()
    st.header("Bienvenido a la clase de ASL 1.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab1, = st.tabs([ ":white[Primavera]"])

    with tab1:
            spring()



def login_sidebar_ASL1():
        show_pages(
    [
        Page("Pagina_Principal.py", "Pagina Principal"),
        Page("pages/1_Diccionario.py", "Diccionario"),
        Page("pages/2_Clases.py", "Clases"),
        Page("pages/3_Libros.py", "Libros"),
        Page("pages/4_Recursos.py", "Recursos"),
        Page("pages/5_Sobre_Yo.py", "Sobre Yo"),
        Page("pages/6_Diccionario_Completo.py", "Diccionario Completo"),
        Page("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra"),
        Page("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema"),
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_1.py", "Introducción a ASL 1"),
        # Page("pages/Bravo_1.py", "Conocer la Familia Bravo"),
        # Page("pages/Bravo_2.py", "Desayuno"),
        # Page("pages/Bravo_3.py", "¿Dónde está el contról?"),
        Page("pages/holidays_spring.py", "Días Festivos")
    ]
)

def spring():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Spring</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://www.youtube.com/watch?v=1XRJRt2dlNc')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Camino de la Primavera (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=nhRxdkqXghc')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Camino de la Primavera (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://www.youtube.com/watch?v=xs-LBiqID50')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Cuento de la Primavera</h5>', unsafe_allow_html=True)
    # with clms3[1]:
    #     st.video('https://youtu.be/UR5sbc6vHBY')
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQWQGDfD9frtoRelg1LUY82AfX61Uncc62N2cOlLlR6m_rVaBFQLd0y7sEROoLbOwN3LHV0aCIIcHPA/embed?start=false&loop=false&delayms=3000", height=480)



main()
