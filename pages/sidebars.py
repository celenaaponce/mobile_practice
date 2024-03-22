from st_pages import Page, show_pages
import streamlit as st

def regular_sidebar():
            st.sidebar.page_link("Pagina_Principal.py", label="Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", label="Diccionario")
            st.sidebar.page_link("pages/Clases.py", label="Clases")
            st.sidebar.page_link("pages/Libros.py", label="Libros")
            st.sidebar.page_link("pages/Recursos.py", label="Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", label="Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", label="Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", label="Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", label="Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", label="Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", label="Entrar")
                
def login_sidebar_ASL1():
            st.sidebar.page_link("Pagina_Principal.py", label="Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", label="Diccionario")
            st.sidebar.page_link("pages/Clases.py", label="Clases")
            st.sidebar.page_link("pages/Libros.py", label="Libros")
            st.sidebar.page_link("pages/Recursos.py", label="Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", label="Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", label="Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", label="Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", label="Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", label="Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", label="Entrar")
            st.sidebar.page_link("pages/helper/Introduccion_a_ASL_1.py", label="Introducción a ASL 1")
            st.sidebar.page_link("pages/helper/Bravo_1.py", label="Conocer la Familia Bravo")
            st.sidebar.page_link("pages/helper/holidays_spring.py", label="Días Festivos")
        
def login_sidebar_ASL2():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/Clases.py", "Clases")
            st.sidebar.page_link("pages/Libros.py", "Libros")
            st.sidebar.page_link("pages/Recursos.py", "Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", "Entrar")
            st.sidebar.page_link("pages/helper/Introduccion_a_ASL_2.py", "Introducción a ASL 2")
            st.sidebar.page_link("pages/helper/Bravo_4.py", "Ir de Compras")
            st.sidebar.page_link("pages/helper/holidays_spring_2.py", "Días Festivos")

def login_sidebar_ASL3():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/Clases.py", "Clases")
            st.sidebar.page_link("pages/Libros.py", "Libros")
            st.sidebar.page_link("pages/Recursos.py", "Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", "Entrar")
            st.sidebar.page_link("pages/helper/Introduccion_a_ASL_3.py", "Introducción a ASL 3")
            st.sidebar.page_link("pages/helper/Bravo_7.py", "Escuela")
            st.sidebar.page_link("pages/helper/holidays_spring_3.py", "Días Festivos")
        
def login_sidebar_ASLAtHome2():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/Clases.py", "Clases")
            st.sidebar.page_link("pages/Libros.py", "Libros")
            st.sidebar.page_link("pages/Recursos.py", "Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", "Entrar")
            st.sidebar.page_link("pages/helper/Introduccion_a_ASL_En_Casa.py")
            st.sidebar.page_link("pages/helper/holidays_spring_aah.py", "Días Festivos")
        
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
    return htmlstr
    

def set_styles(background_color):
    style_html = f"""
    <style>
    h5 {{
        margin-top: 20px;
        margin-bottom: 20px;
    }}
    a {{
        background-color: {background_color};
    }}
    </style>
"""
    return style_html

