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
    Page("pages/10_Entrar.py", "Entrar"),
    Page("pages/11_Form.py", "Registrar para Clases")
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

outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://www.youtube.com/watch?v=cfetJAwPAho' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/jirafas%20no%20pueden%20bailar.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/mkgxSLa_QFE' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/la%20arana%20muy%20ocupada.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/qp9jl0ECUwA' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/banarse.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/AShZlHInWEU' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/eresunavaca.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/X-DT_SDXxO4' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/lindobebecito.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/Z-qNfedG3Hk' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/oceancolorido.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://www.youtube.com/watch?v=62NbByFKX7Y' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/charla.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/q7QTDovFA74' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/meal.png'></a>", unsafe_allow_html=True)

with outer_col[1]:
    st.markdown("<a href='https://youtu.be/xqJVGpVjJZg' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/el%20libro%20de%20colores%20de%20coneja%20blanca.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://www.youtube.com/watch?v=wQCkUbaZLQQ' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/como%20dan%20las%20buenas%20noches%20los%20dinosaurios.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/tvyr6wu4dL4' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/cabezaapie.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/HA29CwpR_-0' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/escuela.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/zLrhnfSa8cc' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/munecas.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/4i582v8lTdI' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/muertos.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/4TmdTAaPYdA' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/bath.png'></a>", unsafe_allow_html=True)

