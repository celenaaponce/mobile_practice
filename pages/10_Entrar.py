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
from pages import Primera_Semana

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

classes = {'ASL1': ['allelugo2009@hotmail.com', 'Maria789sy@gmail.com', 'prepez.2013@gmail.com', 'hernandezmarili64@icloud.com', 'ivonnemercadoj@yahoo.com', 'Yetzabelcerrada831@gmail.com','arbe0320@gmail.com'], 
           'ASL2': 'rbriggs',
           'ASL En Casa': ['santyortega588@gmail.com', 'groisabel17@gmail.com', 'carinad1989@gmail.com', 'eloinar493@gmail.com']}

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
    if username in classes['ASL1']:
        login_sidebar()
        st.header("Bienvenido a la clase de ASL 1. \n Se puede mirar nuestro curiculo aqui:")
        tab1, tab2, tab3 = st.tabs(["Primera Semana", "🔒Segunda Semana", "🔒Tercera Semana"])
        with tab1:
             Primera_Semana.primera_semana()
    elif username in classes['ASL2']:
        login_sidebar()
        st.header("Bienvenido a la clase de ASL 2.  Se puede mirar nuestro curiculo aqui:")
        tab1, tab2, tab3 = st.tabs(["Primera Semana", "🔒Segunda Semana", "🔒Tercera Semana"])
        with tab1:
             Primera_Semana.primera_semana()

    else:
        login_sidebar()
        st.header("Bienvenido a la clase de ASL En Casa.  Se puede mirar nuestro curiculo aqui:")
        tab1, tab2, tab3 = st.tabs(["Primera Semana", "🔒Segunda Semana", "🔒Tercera Semana"])
        with tab1:
             Primera_Semana.primera_semana()

elif authentication_status == False:
    st.error('Nombre/contraseña es mal')
    regular_sidebar()
elif authentication_status == None:
    st.warning('Escriba su nombre de usario y contraseña.')
    regular_sidebar()
