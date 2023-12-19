import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages, add_page_title

def main():
    login_sidebar_ASLAtHome2()
    st.header("Bienvenido a la clase de ASL En Casa.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab2, tab4 = st.tabs([":white[Capitulo 1 Pt 1]",  ":white[Capitulo 1 Pt 2]"])

    with tab2:
            segunda_semana()
    with tab4:
            tercera_semana()

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
        Page("pages/holidays_aah.py", "Dias Festivos")
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
    st.subheader('Capitulo 1 Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/F_TOHsNTfwo')
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Libro</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://youtu.be/q7QTDovFA74')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Vocabulario Extra</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://youtu.be/kLiRtHD1Oqc')
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítlos) 🔇</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://youtu.be/YzButzmbrTw')
    clms14 = st.columns([1,1])
    with clms14[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítlos) 🔈</h5>', unsafe_allow_html=True)
    with clms14[1]: 
        st.video('https://youtu.be/BtEIgRvVGg8')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms15 = st.columns([1,1])
    with clms15[0]:
        st.title('')
        st.markdown('<h5>Practicar Vocabulario</h5>', unsafe_allow_html=True)
    with clms15[1]:
        st.video('https://youtu.be/F_TOHsNTfwo')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSb2QAbLy6AheIEJ30YPF-RYjE5gw1Yt7Ovw2wO8Mz2XFUc_MGg2P-8E2i4tlHoiwxXYPGFRE3y1HQn/embed?start=false&loop=false&delayms=3000", height=480)

def tercera_semana():
    st.subheader('Capitulo 1 Pt 2')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/F_TOHsNTfwo')
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://youtu.be/9h0xg41ytx4')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Más Frases</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://youtu.be/sR9PfilyJ54')
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Aun Más Frases</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://youtu.be/IwDGq8ZdXeg')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms15 = st.columns([1,1])
    with clms15[0]:
        st.title('')
        st.markdown('<h5>Nuevo Vocabulario</h5>', unsafe_allow_html=True)
    with clms15[1]:
        st.video('https://youtu.be/7361Wr6W9p4')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSUy7ujstNW4DmMo_nsX34FvycNSLUA8C8UI8Vrp59GzkF4dJloCFW9qmiYwwV2SaYKVzkW5PFZ7MHy/embed?start=false&loop=false&delayms=3000", height=480)

main()
