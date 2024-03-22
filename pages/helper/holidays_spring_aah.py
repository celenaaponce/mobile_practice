import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages.sidebars import login_sidebar_ASLAtHome2
st.write(st.session_state)
def main():
    login_sidebar_ASLAtHome2()
    st.header("Bienvenido a la clase de ASL En Casa.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab1, = st.tabs([ ":white[Primavera]"])

    with tab1:
            spring()


def spring():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de la Primavera</h5>', unsafe_allow_html=True)
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
    with clms3[1]:
        st.video('https://youtu.be/spE7JQHC9Zw')
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQWQGDfD9frtoRelg1LUY82AfX61Uncc62N2cOlLlR6m_rVaBFQLd0y7sEROoLbOwN3LHV0aCIIcHPA/embed?start=false&loop=false&delayms=3000", height=480)



main()
