import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages, add_page_title
from modules.nav import MenuButtons
from pages.sidebars import set_styles
st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
def main():
    MenuButtons("ASLEnCasa")
    set_styles("#94387f")
    st.header("Bienvenido a la clase de ASL En Casa.")
    st.header("Se puede mirar nuestro curriculo aqui:")
#     tab2 = st.tabs([":white[Capítulo 2]"])

#     with tab2:
#             segunda_semana()

# def segunda_semana():
    st.subheader('Capítulo 2')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=RNjed7e9vXM')
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Clasificadores</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtube.com/watch?v=I-i1Hsp_h-s&t=18sM')    
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Frases de Practica</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://www.youtube.com/watch?v=TLBdOJycKug')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Frases Receptivas</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://www.youtube.com/watch?v=S_Pjl6Lqzi4&t=5s')
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Escenarios</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://www.youtube.com/watch?v=r8fk2V9PeXQ&t=3s')
    st.divider()
    st.subheader("Extras")
    clms14 = st.columns([1,1])
    with clms14[0]:
        st.title('')
        st.markdown('<h5>Libro</h5>', unsafe_allow_html=True)
    with clms14[1]: 
        st.video('https://www.youtube.com/watch?v=qp9jl0ECUwA')
    clms15 = st.columns([1,1])
    with clms15[0]:
        st.title('')
        st.markdown('<h5>Frases Extra</h5>', unsafe_allow_html=True)
    with clms15[1]: 
        st.video('https://www.youtube.com/watch?v=CcxmBTfDlMo')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms18 = st.columns([1,1])
    with clms18[0]:
        st.title('')
        st.markdown('<h5>Practicar Vocabulario</h5>', unsafe_allow_html=True)
    with clms18[1]:
        st.video('https://www.youtube.com/watch?v=RNjed7e9vXM')
    clms19 = st.columns([1,1])
    with clms19[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la Semana que Viene</h5>', unsafe_allow_html=True)
    with clms19[1]:
        st.video('https://youtu.be/9q4e_fQB6No')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vT7ivxIqAqCRPzOxAn5dHtu8vnp2-qZ7qcX2GKvBF38GLR1GkytUeJAw6-OEZUWkfR3xKLeDGQpc1Hm/embed?start=false&loop=false&delayms=3000", height=480)
    clms20 = st.columns([1,1])
    with clms20[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms20[1]: 
        st.video('https://youtu.be/OvM35kf_S-4')
    st.divider()

    

main()
