
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages
import string
st.session_state['password_correct'] = False
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
            Page("pages/10_Entrar.py", "Entrar"),
            Page("pages/11_Form.py", "Registrar para Clases")
        ])
                
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
        Page("pages/11_Form.py", "Registrar para Clases"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_1.py", "Introducción a ASL 1"),
        # Page("pages/Bravo_1.py", "Conocer la Familia Bravo"),
        # Page("pages/Bravo_2.py", "Desayuno"),
        # Page("pages/Bravo_3.py", "¿Dónde está el contról?"),
        Page("pages/holidays.py", "Días Festivos")
    ]
)
        
def login_sidebar_ASL2():
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
        Page("pages/11_Form.py", "Registrar para Clases"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_2.py", "Introducción a ASL 2"),
        # Page("pages/Bravo_5.py", "Repaso"),
        # Page("pages/Bravo_6.py", "Colores y Deletrear"),
        # Page("pages/Bravo_7.py", "Escuela"),
        Page("pages/holidays_2.py", "Días Festivos")
    ]
)
        
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
        Page("pages/11_Form.py", "Registrar para Clases"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_En_Casa.py"),
        # Page("pages/ASLAtHome_c1.py", "Capitulo 1"),
        # Page("pages/ASLAtHome_c2.py", "Capitulo 2")
    ]
)

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.write(st.secrets['password'])
            option = st.selectbox(
                    '¿Cual clase?',
                    ('ASL 1', 'ASL 2', 'ASL 3', 'ASL En Casa'), key='option')
            st.text_input("Contraseña", type="password", key="password")
            st.form_submit_button("Entrar", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state['password'] == st.secrets['password']:
                    st.session_state["password_correct"] = True
        else:
                st.session_state["password_correct"] = False
    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()

    return False

if not check_password():
    st.stop()

if 'option' in st.session_state.keys():
        classoption = st.session_state['option']
else:       
        classoption = ""
        check_password()
if classoption == 'ASL 1':
    login_sidebar_ASL1()
    switch_page("Introducción_a_ASL_1")

elif classoption == 'ASL 2':
        login_sidebar_ASL2()
        switch_page("Introducción_a_ASL_2")
    
elif classoption == 'ASL En Casa':
    login_sidebar_ASLAtHome2()
    switch_page("Introduccion_a_ASL_En_Casa")
else:
        regular_sidebar()
        check_password()
