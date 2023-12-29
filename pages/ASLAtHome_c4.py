import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages, add_page_title



def main():
    login_sidebar_ASLAtHome2()
    st.header("Bienvenido a la clase de ASL En Casa.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    capitulo_4()

def login_sidebar_ASLAtHome2():
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
        Page("pages/Introduccion_a_ASL_En_Casa.py"),
        Page("pages/ASLAtHome_c1.py", "Capitulo 1"),
        Page("pages/ASLAtHome_c2.py", "Capitulo 2"),
        Page("pages/ASLAtHome_c3.py", "Capitulo 3"),
        Page("pages/ASLAtHome_c4.py", "Capitulo 4"),
        Page("pages/holidays_aah.py", "Dias Festivos")
    ]
)

def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }
        </style>
    """, unsafe_allow_html=True)

def capitulo_3():
    st.subheader('Capitulo 4')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=ox9d05hOxUM')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Frases Para Copear</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://youtu.be/6UP388b2p9s')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Práctica Receptiva</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://youtu.be/xHqGfn6-xzI')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Escenarios</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://www.youtube.com/watch?v=ox9d05hOxUM')
    clms4 = st.columns([1,1])
    with clms4[0]:
        st.title('')
        st.markdown('<h5>Como leer a niño sordo</h5>', unsafe_allow_html=True)
    with clms4[1]:
        st.video('https://youtu.be/PirgLzr0BOA')
    clms5 = st.columns([1,1])
    with clms5[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de el Dia Nevado</h5>', unsafe_allow_html=True)
    with clms5[1]:
        st.video('https://www.youtube.com/watch?v=_paypYwl8Oo')
    clms6 = st.columns([1,1])
    with clms6[0]:
        st.title('')
        st.markdown('<h5>El Dia Nevado</h5>', unsafe_allow_html=True)
    with clms6[1]:
        st.video('https://www.youtube.com/watch?v=ocMIAUvK3i8')

    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSAB3eeDRKzUfStyCMo3G51Yjb87A9akyTuMkoZdYDddmgDG7szu9cebdQiAHnZb2VwoVn2ltOexam9/embed?start=false&loop=false&delayms=3000", height=480)

main()
