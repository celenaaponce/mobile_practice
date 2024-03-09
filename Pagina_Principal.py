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

def set_styles():
    st.write("""
        <style>
        h5 {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
  
image = Image.open('Online world-cuate (2).png')
cont_1 = st.container()
cont_2 = st.container()
cont_3 = st.container()
cont_4 = st.container()
cont_5 = st.container()
outer_cols = st.columns([1, 1])

with cont_1:
    with outer_cols[0]:
        set_styles()
        st.markdown("<h1 style='text-align: center; color: white;'>¡Aprender Lengua de Señas Americana en Su Propia Idioma!</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Para padres latinos de niños sordos, sé que hay muchos retos.  Hay bastante que aprender, no sólo idioma, pero cultura y más. Mi meta es ayudar a padres latinos entender la lengua de señas americana, sin necesitar saber inglés.  También, quiero ayudarles a encontrar los recursos que necesitan para que sus hijos pueden tener éxito. </h5>", unsafe_allow_html=True)
    
    with outer_cols[1]:
        inner_cols = st.columns([1, 6, 1])
        with inner_cols[1]:
            st.image(image)
        quien = st.button('Quien Soy', key='Quien')
        ChangeButtonColour('Quien Soy', '#fffff', '#94387f') 
        if quien:
            switch_page('Sobre_Yo')


st.divider()
image2 = Image.open('dictionary.png')

outer_col_2 = st.columns([1, 1])            
with cont_2:
    
    with outer_col_2[1]:
        set_styles()
        st.markdown("<h2 style='text-align: center; color: white;'>Diccionario</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Buscar señas y frases en un diccionario de español a ASL </h5>", unsafe_allow_html=True)
    
    with outer_col_2[0]:
        inner_col_2 = st.columns([1, 6, 1])
        with inner_col_2[1]:
            st.image(image2)
        dict = st.button('Diccionario', key='Dict')
        ChangeButtonColour('Diccionario', '#fffff', '#407bff') 
        if dict:
            switch_page('Diccionario')

st.divider()
image3 = Image.open('Online learning-rafiki.png')
outer_col_3 = st.columns([1, 1])            
with cont_3:
    
    with outer_col_3[0]:
        set_styles()
        st.markdown("<h2 style='text-align: center; color: white;'>Clases</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Tomar clases gratis en español para aprender lengua de señas americana. </h5>", unsafe_allow_html=True)
    
    with outer_col_3[1]:
        inner_col_3 = st.columns([1, 6, 1])
        with inner_col_3[1]:
            st.image(image3)
        classes = st.button('Clases', key='Clases')
        ChangeButtonColour('Clases', '#fffff', '#92E3A9') 
        if classes:
            switch_page('Clases')

st.divider()
image4 = Image.open('Absorbed in-pana.png')

outer_col_4 = st.columns([1, 1])            
with cont_4:
    
    with outer_col_4[1]:
        set_styles()
        st.markdown("<h2 style='text-align: center; color: white;'>Libros</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Mirar videos de libros en español con ASL </h5>", unsafe_allow_html=True)
    
    with outer_col_4[0]:
        inner_col_4 = st.columns([1, 6, 1])
        with inner_col_4[1]:
            st.image(image4)
        books = st.button('Libros', key='Libros')
        ChangeButtonColour('Libros', '#fffff', '#FF725E') 
        if books:
            switch_page('Libros')

st.divider()
image5 = Image.open('Selecting team-pana.png')
outer_col_5 = st.columns([1, 1])            
with cont_5:
    
    with outer_col_5[0]:
        set_styles()
        st.markdown("<h2 style='text-align: center; color: white;'>Recursos</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Recursos para familias latinas con hijos sordos </h5>", unsafe_allow_html=True)
    
    with outer_col_5[1]:
        inner_col_5 = st.columns([1, 6, 1])
        with inner_col_5[1]:
            st.image(image5)
        resources = st.button('Recursos', key='Recursos')
        ChangeButtonColour('Recursos', '#fffff', '#C53F3F') 
        if resources:
            switch_page('Recursos')
