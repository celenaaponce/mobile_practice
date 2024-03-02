import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages import holidays
from st_pages import Page, Section,show_pages, add_page_title
st.session_state['password_correct'] = True
def main():
        login_sidebar_ASL3()
        st.header("Bienvenido a la clase de ASL 3.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        escuela1()

def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }

        </style>
    """, unsafe_allow_html=True)

def login_sidebar_ASL3():
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
        Page("pages/Introduccion_a_ASL_3.py", "Introducción a ASL 3"),
        # Page("pages/Bravo_5.py", "Repaso"),
        # Page("pages/Bravo_6.py", "Colores y Deletrear"),
        Page("pages/Bravo_7.py", "Escuela"),
        Page("pages/holidays_spring_3.py", "Días Festivos")
    ]
)

def escuela1():
    set_styles()
    st.subheader('Lección 7: Escuela')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introduccion </h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/oQQFZSlr-7c')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/U0I58rdwlDkg')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversacion (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/Ey_qhboMTmo')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversacion (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/qa3gM93D85c')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/HhilwM-rUPk')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/axnjssoujJQ')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/656832c8714d964171966867' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/65683015dc1e1641a09708ad' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTaL-csLK4bnmmbonxNSjLb0lgzB22X8rQahAOtdtEo0zRHKgQ6RTWEBwIOw2yy4DXaI6PauEFEDu78/embed?start=false&loop=false&delayms=3000", height=480)
main()
