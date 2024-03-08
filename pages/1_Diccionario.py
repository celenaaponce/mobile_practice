import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, Section,show_pages, add_page_title
st.session_state['password_correct'] = False
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
def set_styles():
    st.write("""
        <style>
        h5 {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

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

m = st.markdown("""
<style>
div.stButton > button:first-child {
  border: none;
  display: block;
  width: 200px; 
  margin: 0 auto;
}
</style>""", unsafe_allow_html=True)
image2 = Image.open('dictionary.png')

outer_col_2 = st.columns([1, 1])            

with outer_col_2[1]:
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'>Diccionario</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'> Este diccionario es señas en la lengua de ASL, con videos. También tiene fotos, y voz en español. </h5>", unsafe_allow_html=True)

with outer_col_2[0]:
    inner_col_2 = st.columns([1, 6, 1])
    with inner_col_2[1]:
        st.image(image2)
st.divider()
outer_col = st.columns([1,1])
st.divider()
with outer_col[0]:
    compl = st.button('Diccionario Completo', key='Completo')
    ChangeButtonColour('Diccionario Completo', '#fffff', '#407bff') 
    if compl:
         switch_page('Diccionario_Completo')
with outer_col[1]:
        st.markdown("<h5 style='text-align: center; color: white;'> Mirar el diccionario completo</h5>", unsafe_allow_html=True)

outer_col_3 = st.columns([1,1])
st.divider()
with outer_col_3[0]:
    letra = st.button('Buscar por Letra', key='Letra')
    ChangeButtonColour('Buscar por Letra', '#fffff', '#407bff') 
    if letra:
        switch_page('Diccionario_por_Letra')
with outer_col_3[1]:
         st.markdown("<h5 style='text-align: center; color: white;'> Buscar palabras por letra inicial </h5>", unsafe_allow_html=True)

outer_col_4 = st.columns([1,1])
st.divider()
with outer_col_4[0]:
    tema = st.button('Buscar por Tema', key='Tema')
    ChangeButtonColour('Buscar por Tema', '#fffff', '#407bff') 
    if tema:
         switch_page('Diccionario_por_Tema')
with outer_col_4[1]:
    st.markdown("<h5 style='text-align: center; color: white;'> Buscar palabras por tema </h5>", unsafe_allow_html=True)

outer_col_5 = st.columns([1,1])
st.divider()
with outer_col_5[0]:
    palabra = st.button('Buscar Palabra', key='Palabra')
    ChangeButtonColour('Buscar Palabra', '#fffff', '#407bff') 
    if palabra:
         switch_page('Buscar_Palabra')
with outer_col_5[1]:
    st.markdown("<h5 style='text-align: center; color: white;'> Buscar palabra usando búsqueda</h5>", unsafe_allow_html=True)
