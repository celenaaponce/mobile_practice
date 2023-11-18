import streamlit_authenticator as stauth
import yaml
import gdown
from yaml.loader import SafeLoader
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from st_pages import Page, Section,show_pages, add_page_title
from streamlit.source_util import get_pages
import streamlit.components.v1 as components
from pages import ASL1
from pages import ASL2
from pages import ASLAtHome
from pages import holidays

def regular_sidebar():
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
        
def login_sidebar():
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
    ]
)
        
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        function goTo(page) {{
        page_links = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a')
        page_links.forEach((link) => {{
            if (link.text == page) {{
                link.click()
            }}
        }})
    }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }
        </style>
    """, unsafe_allow_html=True)

@st.cache_data
def download_yaml():
        file_id = st.secrets['yaml']
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, 'info.yaml', quiet=False)
        with open('info.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config

config = download_yaml()
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Entrar', 'main')

if authentication_status:
    authenticator.logout('Salir', 'main')
    st.title(f'Bienvenido *{name}*')
    if username in st.secrets.ASL1:
        login_sidebar()
        st.header("Bienvenido a la clase de ASL 1.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([":red[Primera Semana]", ":orange[Conocer la Familia Bravo Pt 1]", ":orange[Halloween/Dia de los Muertos]", 
                                                            ":green[Conocer la Familia Bravo Pt 2]", ":blue[Desayuno Pt 1]", ":purple[Desayuno Pt 2]", ":black[Dia de Accion de Gracias]"])
        with tab1:
             ASL1.primera_semana()
        with tab2:
             ASL1.segunda_semana()
        with tab3:
             holidays.halloween()
        with tab4:
             ASL1.tercera_semana()
        with tab5:
             ASL1.cuarta_semana()
        with tab6:
             ASL1.quinta_semana()
        with tab7:
             holidays.thanksgiving()
    elif username in st.secrets['ASL2']:
        login_sidebar()
        st.header("Bienvenido a la clase de ASL 2.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([":red[Primera Semana]", ":orange[Repaso General]", ":orange[Repaso Leccion 1]", ":orange[Repaso Leccion 2]", 
                                                                               ":orange[Repaso Leccion 3]", ":orange[Repaso Leccion 4]", ":orange[Halloween/Dia de los Muertos]", 
                                                                               ":green[Colores]", ":blue[Deletrear]", ":white[Dia de Accion de Gracias]"])
        with tab1:
             ASL2.primera_semana()
        with tab2:
             ASL2.repaso_general()
        with tab3:
             ASL2.repaso_lecc1()
        with tab4:
             ASL2.repaso_lecc2()
        with tab5:
             ASL2.repaso_lecc3()
        with tab6:
             ASL2.repaso_lecc4()
        with tab7:
             holidays.halloween()
        with tab8:
             ASL2.colores()
        with tab9:
             ASL2.deletrear()
        with tab10:
             holidays.thanksgiving()

    else:
        login_sidebar()
        st.header("Bienvenido a la clase de ASL En Casa.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([":red[Primera Semana]", ":orange[Capitulo 1 Pt 1]", ":orange[Halloween/Dia de los Muertos]", 
                                                            ":green[Capitulo 1 Pt 2]", ":blue[Capitulo 2 Pt 1]", ":purple[Capitulo 2 Pt 2]", ":black[Dia de Accion de Gracias]"])
        with tab1:
             ASLAtHome.primera_semana()
        with tab2:
             ASLAtHome.segunda_semana()
        with tab3:
             holidays.halloween()
        with tab4:
             ASLAtHome.tercera_semana()
        with tab5:
             ASLAtHome.cuarta_semana()
        with tab6:
             ASLAtHome.quinta_semana()
        with tab7:
            holidays.thanksgiving()

elif authentication_status == False:
    st.error('Nombre/contraseña es mal')
    regular_sidebar()
elif authentication_status == None:
    st.warning('Escriba su nombre de usario y contraseña.')
    regular_sidebar()
