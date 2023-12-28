import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages, add_page_title

def main():
    login_sidebar_ASLAtHome2()
    st.header("Bienvenido a la clase de ASL En Casa.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([ ":white[Halloween/Dia de los Muertos]", 
                                                        ":white[Dia de Accion de Gracias]", ":white[Invierno]", ":white[Navidad]",
                         ":white[Año Nuevo]", ":white[Dia de los 3 Reyes]"])

    with tab1:
            halloween()
    with tab2:
            thanksgiving()
    with tab3:
            winter()
    with tab4:
            christmas()
    with tab5:
            new_year()
    with tab6:
            three_king_day()


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
        Page("pages/holidays_aah.py", "Dias Festivos")
    ]
)

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
    st.divider()
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
        
def christmas():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Navidad</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/0Fq2sIfjA5M')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Cuento de Navidad</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/4sGozFsfAnc')

def winter():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Invierno</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/KKiMMFbQPxQ')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Cuento de Invierno</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/zLrhnfSa8cc')

def new_year():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de Año Nuevo</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/sgR34pRPga8')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Cuento de Año Nuevo</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=Z7atC7dX_Ig')

def three_king_day():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Cuento de Dia de Los 3 Reyes</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/SS6FgPqm3RU')

main()
