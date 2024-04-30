import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages.sidebars import login_sidebar_ASL1, set_styles
from st_pages import Page, Section,show_pages, add_page_title
from modules.nav import MenuButtons
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
        tab8, tab9 = st.tabs([":white[Banco Pt 1]", ":white[Banco Pt 2]"])

        with tab8:
            banco1()
        with tab9:
             banco2()
        
def banco1():
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
    st.subheader('Lección 9: Banco')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introduccion </h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://www.youtube.com/watch?v=SbosnlVaHsU')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://www.youtube.com/watch?v=jA4GwTECa5M')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversacion (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://www.youtube.com/watch?v=u0hXZ-vBpJ8')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversacion (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/GKPcGD_hrD0')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://www.youtube.com/watch?v=vSVCAHvVYxA')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Carreras para Personaas Sordos</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/BTbqe7AgkyI')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/NPxK-atgF_s')
        st.video('https://youtu.be/NyzYX41Tbcs')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/661d4fbc6190b34cdf780418' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/661d5a8f607cee61aa154c91' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQT1zzV9ZBZuyB6o7Ff5IhHjJOUd7Ni0fQ15cT7XoiF7MdKyCIe4SZUjXfM4mvPR4M1zM6TXCcXu_Do/embed?start=false&loop=false&delayms=3000", height=480)
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/La8kZMUT4mA')
            
def banco2():
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
    st.subheader('Lección 9: Banco')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Vocabulario </h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/NPxK-atgF_s')
    clms22 = st.columns([1,1])
    with clms22[0]:
        st.title('')
        st.markdown('<h5>Más Vocabulario </h5>', unsafe_allow_html=True)
    with clms22[1]:
        st.video('https://youtu.be/NyzYX41Tbcs')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/Tros4qGos-s')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Más Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/byFIxaEHutY')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/BDp8OlEOOFE')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/2Ljs6KdnO3s')
    clms30 = st.columns([1,1])
    with clms30[0]:
        st.title('')
        st.markdown('<h5>Cuento (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms30[1]:    
        st.video('https://www.youtube.com/watch?v=u0hXZ-vBpJ8')
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Cuento (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms31[1]: 
        st.video('https://youtu.be/Dce7myq8rao')
    clms32 = st.columns([1,1])
    with clms32[0]:
        st.title('')
        st.markdown('<h5>Carreras para Personas Sordos</h5>', unsafe_allow_html=True)
    with clms32[1]: 
        st.video('https://www.youtube.com/watch?v=yrrwxrb8JRQ')      
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)

    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/661ebee40c33da0da686b776' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/661ea7be7d0bcf016e521bd2' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRTGMfYP-QC31amUPCsEMYFODxvfZ6uVLBwjpo6sAKgTtw07e23EEF0DMMSmEtBYGGP_xX6X8VGWckv/embed?start=false&loop=false&delayms=3000", height=480)
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/DNb4qnIsi2Y')

main()
