import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
# from pages import holidays
from st_pages import Page, Section,show_pages, add_page_title

def main():
    login_sidebar_ASL1()
    st.header("Bienvenido a la clase de ASL 1.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab2, tab4 = st.tabs([":white[Conocer la Familia Bravo Pt 1]", 
                                                        ":white[Conocer la Familia Bravo Pt 2]"])
    with tab2:
            segunda_semana()
    with tab4:
            tercera_semana()


def login_sidebar_ASL1():
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
        Page("pages/Introduccion_a_ASL_1.py", "Introducción a ASL 1"),
        Page("pages/Bravo_1.py", "Conocer la Familia Bravo"),
        # Page("pages/Bravo_2.py", "Desayuno"),
        # Page("pages/Bravo_3.py", "¿Dónde está el contról?"),
        Page("pages/holidays_spring.py", "Días Festivos")
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

def segunda_semana():
    
    set_styles()
    login_sidebar_ASL1()
    st.subheader('Conocer La Familia Bravo Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introducción a La Familia (sin subtitlos) 🔇</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/SITwK-RY11c')
    clms22 = st.columns([1,1])
    with clms22[0]:
        st.title('')
        st.markdown('<h5>Introducción a La Familia (con subtitlos) 🔈</h5>', unsafe_allow_html=True)
    with clms22[1]:
        st.video('https://youtu.be/5hp9m0BTTB4?si=eNI9aNMf7O7q8bQY')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/pmLq0Hes-AE')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/tZk1fKC_7hQ')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/pg_A3DOROAk')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/IAzyXBqyBLU')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/HfsmWDTOjys?si=d4Ws78IFcP2fPRyk')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/633642ed68206040f25bc382' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/633750f5389ee741763d8d57' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/63375bff25e87940d4c32e08' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTwTwZCMQMldc_sXEFLb5nMns5knZG9PNmSh_UgUB8e_N-DtLMu-NZeoUCVhZcprTtnDOXq8FRP26Vt/embed?start=false&loop=false&delayms=3000", height=480)

def tercera_semana():
    set_styles()
    # st.subheader('Conocer La Familia Bravo Pt 2')
    # st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    # clms23 = st.columns([1,1])
    # with clms23[0]:
    #     st.title('')
    #     st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    # with clms23[1]:
    #     st.video('https://youtu.be/3XcBL8fEpcI?si=3JZgBz5avB88fQo_')
    # clms24 = st.columns([1,1])
    # with clms24[0]:
    #     st.title('')
    #     st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    # with clms24[1]:    
    #     st.video('https://youtu.be/RAoRBgN_BaQ')
    # clms25 = st.columns([1,1])
    # with clms25[0]:
    #     st.title('')
    #     st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    # with clms25[1]: 
    #     st.video('https://youtu.be/yrFuvImZGH0?si=g63d-f3DI6xKVnqm')
    # clms26 = st.columns([1,1])
    # with clms26[0]:
    #     st.title('')
    #     st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    # with clms26[1]:
    #     st.video('https://youtu.be/LZFrhNALSgg?si=B60ir9iAXZuHtDop')
    # clms29 = st.columns([1,1])
    # with clms29[0]:
    #     st.title('')
    #     st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    # with clms29[1]:
    #     st.video('https://youtu.be/PKULlbXRFic')
    # clms30 = st.columns([1,1])
    # with clms30[0]:
    #     st.title('')
    #     st.markdown('<h5>Cuento (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    # with clms30[1]:    
    #     st.video('https://youtu.be/__ZXhLplISE')
    # clms31 = st.columns([1,1])
    # with clms31[0]:
    #     st.title('')
    #     st.markdown('<h5>Cuento (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    # with clms31[1]: 
    #     st.video('https://youtu.be/5AoLtmMEk8s?si=bJWzu7z8hZs6fzpN')        
    # st.divider()

    # st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    # clms27 = st.columns([1,1])
    # with clms27[0]:
    #     st.title('')
    #     st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    # with clms27[1]:
    #     st.video('https://youtu.be/uGtS3_zEGV8')
    # clms28 = st.columns([1,1])
    # with clms28[0]:
    #     st.title('')
    #     st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    # with clms28[1]:
    #     st.markdown("<a href='https://edpuzzle.com/media/6340a4165be52340dc956cb7' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
    #     st.markdown("<a href='https://edpuzzle.com/media/6340a73092852240f8ac3087' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    # st.divider()
    # components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRtK9-_F-5WfUL0Gg84Z2WUnlEXXsy1yIkz5h6AmrYGL2dt7cat8e8hFw8ih9ru6rio2HBPQb6cLi3D/embed?start=false&loop=false&delayms=3000", height=480)

main()
