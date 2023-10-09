import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit.components.v1 import html
from st_pages import Page, Section,show_pages, add_page_title

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
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

def set_styles():
    st.write("""
        <style>
        h5 {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        a {
            background-color: #FF725E;

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
image4 = Image.open('Absorbed in-pana.png')
outer_col_4 = st.columns([1, 1])      
with outer_col_4[1]:
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'>Libros</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Mirar videos de libros en español con ASL </h5>", unsafe_allow_html=True)

with outer_col_4[0]:
    inner_col_4 = st.columns([1, 6, 1])
    with inner_col_4[1]:
        st.image(image4)
image = Image.open('jirafas no pueden bailar.jpg')
image2 = Image.open('la arana muy ocupada.jpg')
image3 = Image.open('el libro de colores de coneja blanca.jpeg')
image5 = Image.open('como dan las buenas noches los dinosaurios.jpg')
outer_col = st.columns([1,1])
with outer_col[0]:
    st.image(image)
    st.button('Jirafas no Pueden Bailar', key='Jirafas', on_click = open_page, args =('https://www.youtube.com/watch?v=cfetJAwPAho',))
    ChangeButtonColour('Jirafas no Pueden Bailar', '#fffff', '#FF725E') 

    st.image(image2)
    st.button('La Araña Muy Ocupada', key='Araña', on_click = open_page, args = ('https://www.youtube.com/watch?v=u37prsL9Rik',))
    ChangeButtonColour('La Araña Muy Ocupada', '#fffff', '#FF725E') 

with outer_col[1]:
    st.image(image3)
    st.button('El Libro de Colores de Coneja Blanca', key = 'Coneja', on_click = open_page, args=('https://www.youtube.com/watch?v=2qgjqhVc5Aw',))
    ChangeButtonColour('El Libro de Colores de Coneja Blanca', '#fffff', '#FF725E') 

    st.image(image5)
    st.button('Como Dan Las Buenas Noches Los Dinosaurios', key = 'Dino', on_click = open_page, args = ('https://www.youtube.com/watch?v=wQCkUbaZLQQ',))
    ChangeButtonColour('Como Dan Las Buenas Noches Los Dinosaurios', '#fffff', '#FF725E') 
