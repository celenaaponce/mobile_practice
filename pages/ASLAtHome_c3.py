import streamlit as st
import streamlit.components.v1 as components
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
    st.subheader('Capítulo 3')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=ch6EnFZSbi0')
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Frases de Practica</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://www.youtube.com/watch?v=ENnJh7BPziY')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Frases Receptivas</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://www.youtube.com/watch?v=ktU8QATOD2s&t=4s')
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Escenarios</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://www.youtube.com/watch?v=wjwPXfInUjs&t=2s')
    st.divider()
    st.subheader("Extras")
    clms14 = st.columns([1,1])
    with clms14[0]:
        st.title('')
        st.markdown('<h5>Libro</h5>', unsafe_allow_html=True)
    with clms14[1]: 
        st.video('https://www.youtube.com/watch?v=W8fJHacPZbw')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms18 = st.columns([1,1])
    with clms18[0]:
        st.title('')
        st.markdown('<h5>Practicar Vocabulario</h5>', unsafe_allow_html=True)
    with clms18[1]:
        st.video('https://www.youtube.com/watch?v=ch6EnFZSbi0')
    clms19 = st.columns([1,1])
    with clms19[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la Semana que Viene</h5>', unsafe_allow_html=True)
    with clms19[1]:
        st.video('https://youtu.be/FXdio2mVsKo')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTBSkeRMDCYb23VjibQuy3rU0mEDXY9Sc9UOkE3UpRTtAEqZkvleiz2iwhrCpdZx55Je4ydLBZ909LM/embed?start=false&loop=false&delayms=3000", height=480)
    clms20 = st.columns([1,1])
    with clms20[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms20[1]: 
        st.video('https://youtu.be/TghVvxNlXIc')
    st.divider()

    

main()
