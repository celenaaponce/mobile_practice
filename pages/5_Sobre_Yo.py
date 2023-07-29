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
            background-color: #94387f;

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
image3 = Image.open('celena2.jpeg')
outer_col_3 = st.columns([1, 1])            

with outer_col_3[0]:
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'>Sobre Yo</h2>", unsafe_allow_html=True)

    st.markdown("<p> Me llamo Celena Ponce.  Crecí en Vancouver, WA.  Hablo español, lengua de señas americana e inglés.\
                He trabajado con la comunidad sorda por 10 años.  He trabajado por Purple, una de las companias de \
                teléfonos de video para personas Sordas.  Tambien tengo certificado como intérprete de español en el \
                estado de Washington.  Enseño clases de lengua de señas americana en español para CDHY.\
              </p>", unsafe_allow_html=True)

with outer_col_3[1]:
    inner_col_3 = st.columns([1, 6, 1])
    with inner_col_3[1]:
        st.image(image3)
        st.markdown("Correo Electronico: celena.a.ponce@gmail.com")

