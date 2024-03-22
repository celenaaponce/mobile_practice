import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from modules.nav import MenuButtons
from pages.sidebars import login_sidebar_ASL1, set_styles
st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
def main():
        MenuButtons('ASL3')
        st.header("Bienvenido a la clase de ASL 3.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab8, tab9 = st.tabs([":white[Escuela Pt 1]", ":white[Escuela Pt 2]"])

        with tab8:
                escuela1()
        with tab9:
                escuela2()

def escuela1():
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
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
        st.video('https://youtu.be/U0I58rdwlDk')
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
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSZrC1cnCuye5H_A68XhXhBj1jBeVSiGdbVDTMa-NI30NP5Xc07czMc5RKwIBZYC265aM0gjoMWGofO/embed?start=false&loop=false&delayms=3000", height=480)

def escuela1():
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
    st.subheader('Lección 7: Escuela')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/tupco5kdfUQ')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversacion (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/LT-Yx0Ka53Y')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversacion (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/K_Qx4pLF7Zo')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/5UbXbxxtvn8')
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/QC2PRsdSplo')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Cuento (sin subtitulos)🔇</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.video('https://youtu.be/q5i0DBAlBec')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Cuento (con subtitulos)🔈</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/ZGrNpeZ3qaA')
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/6tN2j3V6qp4')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/65a58c5d9978312988b1ace3' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/65a58f163eb8bf37437cf57e' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)
main()
