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

    st.subheader('Capítulo 4')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=qX72alKwe1M')
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Frases de Practica</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://www.youtube.com/watch?v=tcPR9q6sxlA')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Frases Receptivas</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://www.youtube.com/watch?v=5Jt49cdUc84&t=8s')
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Escenarios</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://www.youtube.com/watch?v=fwbn2vYIveY&t=3s')
    st.divider()
    st.subheader("Extras")
    clms14 = st.columns([1,1])
    with clms14[0]:
        st.title('')
        st.markdown('<h5>Como Leer Con Su Hijo Sordo</h5>', unsafe_allow_html=True)
    with clms14[1]: 
        st.video('https://www.youtube.com/watch?v=PirgLzr0BOA')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms18 = st.columns([1,1])
    with clms18[0]:
        st.title('')
        st.markdown('<h5>Practicar Vocabulario</h5>', unsafe_allow_html=True)
    with clms18[1]:
        st.video('https://www.youtube.com/watch?v=qX72alKwe1M')

    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQnb6_M5EJCXqEnke11F29Smr1LW7ylcLsu8NNtmrsx9MMsBsBYjJ5n6krU0CUu6l4ip1ol7FruN82O/embed?start=false&loop=false&delayms=3000", height=480)
    # clms20 = st.columns([1,1])
    # with clms20[0]:
    #     st.title('')
    #     st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    # with clms20[1]: 
    #     st.video('https://youtu.be/TghVvxNlXIc')
    st.divider()

    

main()
