import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages
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
Page("pages/10_Entrar.py", "Entrar")
])
def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }

        </style>
    """, unsafe_allow_html=True)

def primera_semana():
    set_styles()
    st.subheader('Primera Semana: Introducción')
    cont_2 = st.container()

    outer_col_2 = st.columns([4, 1])            
    with cont_2:
        
        with outer_col_2[0]:
            st.markdown("<h4 style='text-align: center; color: white;'><u>Recursos</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://www.asd-1817.org/deaf-schools' target='_blank'>Escuelas para los Sordos</a> en EEUU </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://www.diglo.com/vibrating-clocks-and-watches/alarm-clocks;d=3;c=31;s=311' target='_blank'>Alarma de Reloj</a> para personas Sordos </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://www.diglo.com/shop-by-alert-trigger/doorbell-and-door-knock;d=3;c=32;s=323' target='_blank'>Timbre</a> con luz para personas Sordos </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://www.diglo.com/shop-by-alert-trigger/smoke-and-fire;d=3;c=32;s=328' target='_blank'>Alarma de Incendios</a> para personas Sordos </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://purplevrs.com/espanol' target='_blank'>Telefono de Video</a> para personas Sordos </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://apps.apple.com/us/app/intersign-asl-learn-now/id1567327543' target='_blank'>App para aprender</a> para iPhone </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://play.google.com/store/apps/details?id=intersign.learn.asl&hl=en_US&gl=US' target='_blank'>App para aprender</a> para Android </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/Pt2_EjmtUp8' target='_blank'>Historia de ASL</a></h5>", unsafe_allow_html=True)

            st.divider()
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def segunda_semana():
    set_styles()
    cont_2 = st.container()

    outer_col_2 = st.columns([4, 1])            
    with cont_2:
        
        with outer_col_2[0]:
            st.markdown("<h3 style='text-align: center; color: white;'><u>Videos</u></h3>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/c1T1CoU0luo' target='_blank'>Introducción</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 1</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/CD9CUAlcRW4' target='_blank'>Vocabulario y Frases</a> </h5>", unsafe_allow_html=True)    
            st.markdown("<h5> <a href='https://youtu.be/a6bMKje9kOY' target='_blank'>Diálogo (sin subtítlos)</a> </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://youtu.be/fVmnEqqhlpw' target='_blank'>Diálogo (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/tZk1fKC_7hQ' target='_blank'>Conversación (sin subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/5gYPPZFOO6M' target='_blank'>Conversación (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 2</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/qxd4OUEOCJg' target='_blank'>Vocabulario y Frases</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/_SDd08h_UEM' target='_blank'>Diálogo (sin subtítlos)</a> </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://youtu.be/KOUtXRQ3kFw' target='_blank'>Diálogo (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/JHFhfpjI3CE' target='_blank'>Conversación (sin subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/x494aKUmEKM' target='_blank'>Conversación (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 3</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/_kva3v4OB2E' target='_blank'>Vocabulario</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/IQyhNdrhuR8' target='_blank'>Frases</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/z1EEtsE79-w' target='_blank'>Diálogo (sin subtítlos)</a> </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://youtu.be/5QM2LGdQWvs' target='_blank'>Diálogo (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/8-9YtAezNAE' target='_blank'>Conversación (sin subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/XeXLA8-rWyo' target='_blank'>Conversación (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 4</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/OZL7UyN6wSw' target='_blank'>Vocabulario</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/ZABG-Zl5qzE' target='_blank'>Frases</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/beZlTXitb0g' target='_blank'>Diálogo (sin subtítlos)</a> </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://youtu.be/beZlTXitb0g' target='_blank'>Diálogo (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/qktiKSw2kpQ' target='_blank'>Conversación (sin subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/9sbNxysfxx0' target='_blank'>Conversación (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<h5> <a href='https://youtu.be/t7HzlXNmFJc' target='_blank'>Cultura</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/nBCvy22r6bo' target='_blank'>Gramática</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/a0s8Zw6T3Fw' target='_blank'>Cuento (sin subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/GLXz2s5jBAw' target='_blank'>Cuento (con subtítulos)</a> </h5>", unsafe_allow_html=True)
            st.divider()

            st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
        
            st.markdown("<h5> <a href='https://youtu.be/sVyvzKH_Nsg' target='_blank'>Vocabulario</a> para la semana que viene</h5>", unsafe_allow_html=True)
            st.divider()
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ1DBN424b45UbbrNNEHmSvzFqMDfsnLSR2nLK2eS93kdLU3bdQep_btALoKoWxZu0K644csijPRwuP/embed?start=false&loop=false&delayms=3000", height=480)
