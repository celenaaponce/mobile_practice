import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components

def halloween():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Halloween</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/prquPHmJ3Wk')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Cuento de Halloween (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/wTmywEvbzyk')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Cuento de Halloween (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://www.youtube.com/watch?v=Bhqg_XfKif0')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Cancion de Halloween</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://youtu.be/UR5sbc6vHBY')

    clms4 = st.columns([1,1])
    with clms4[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Dia de los Muertos</h5>', unsafe_allow_html=True)
    with clms4[1]:
        st.video('https://youtu.be/ehEf4nFMXE0')
    clms5 = st.columns([1,1])
    with clms5[0]:
        st.title('')
        st.markdown('<h5>Libro de Dia de los Muertos</h5>', unsafe_allow_html=True)
    with clms5[1]:
        st.video('https://youtu.be/4i582v8lTdI')

def thanksgiving():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Día de Acción de Gracias</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/ii2RYsx7rMY')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Cuento de Día de Acción de Gracias (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/N18FVr_dbLI')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Cuento de Halloween (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://youtu.be/hHpTDEn4w2E')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Libro: Pavo en Problemas</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://youtu.be/TjEJVm4imlY')
    clms4 = st.columns([1,1])
    with clms4[0]:
        st.title('')
        st.markdown('<h5>Hand Talk</h5>', unsafe_allow_html=True)
    with clms4[1]:
        st.video('https://youtu.be/5Hh-vZB5REI')
    clms5 = st.columns([1,1])
    with clms5[0]:
        st.title('')
        st.markdown('<h5>La Cena Silenciosa</h5>', unsafe_allow_html=True)
    with clms5[1]:
        st.video('https://youtu.be/pKmaGwUBScA')
