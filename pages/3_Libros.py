import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit.components.v1 import html

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
image4 = Image.open('/Users/celenap/streamlit/Absorbed in-pana.png')
outer_col_4 = st.columns([1, 1])      
with outer_col_4[1]:
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'>Libros</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Mirar videos de libros en español con ASL </h5>", unsafe_allow_html=True)

with outer_col_4[0]:
    inner_col_4 = st.columns([1, 6, 1])
    with inner_col_4[1]:
        st.image(image4)
image = Image.open('/Users/celenap/streamlit/jirafas no pueden bailar.jpg')
image2 = Image.open('/Users/celenap/streamlit/la arana muy ocupada.jpg')
image3 = Image.open('/Users/celenap/streamlit/el libro de colores de coneja blanca.jpeg')
image5 = Image.open('/Users/celenap/streamlit/como dan las buenas noches los dinosaurios.jpg')
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