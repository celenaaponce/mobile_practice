import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit.components.v1 import html
from pages.sidebars import regular_sidebar, set_styles
from modules.nav import MenuButtons
st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
MenuButtons('')

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)



m = st.markdown("""
<style>
div.stButton > button:first-child {
  border: none;
  display: block;
  width: 200px; 
  margin: 0 auto;
}
</style>""", unsafe_allow_html=True)
image3 = Image.open('./web_img/celena2.jpeg')
outer_col_3 = st.columns([1, 1])            

with outer_col_3[0]:
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Quien Soy</h2>", unsafe_allow_html=True)

    st.markdown("<p> Me llamo Celena Ponce.  Crecí en Vancouver, WA.  Hablo español, lengua de señas americana e inglés.\
                He trabajado con la comunidad sorda por 10 años.  He trabajado para Purple, una de las companias de \
                teléfonos de video para personas sordas.  También tengo certificado como intérprete de español en el \
                estado de Washington.  Enseño clases de lengua de señas americana en español para CDHY.\
              </p>", unsafe_allow_html=True)

with outer_col_3[1]:
    inner_col_3 = st.columns([1, 6, 1])
    with inner_col_3[1]:
        st.image(image3)
        st.markdown("Correo Electrónico: celena.a.ponce@gmail.com")

