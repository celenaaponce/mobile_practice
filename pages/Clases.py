import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from pages.sidebars import regular_sidebar, ChangeButtonColour, set_styles
from streamlit.components.v1 import html
import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles
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

outer_col_3 = st.columns([1, 1])            

with outer_col_3[0]:
    style_html = set_styles('#92E3A9')
    st.write(style_html, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Clases</h1>", unsafe_allow_html=True)

    st.markdown("<p> Con <a href='https://www.cdhy.wa.gov' target='_blank'>CDHY</a> ofrezco clases todo el año.  Empezando el 26 de febrero, tenemos clases cada semana, ofrecidas en linea.  Las clases son individuales y a su nivel.  ¡También son gratis!  Si quiere mirar clases del pasado, puede <a href='https://www.youtube.com/playlist?list=PLAsRcYXV-4XDbhawYIWMukc53mP-zbRqv' target='_blank'>mirar las clases.</a> </p>", unsafe_allow_html=True)

with outer_col_3[1]:
    inner_col_3 = st.columns([1, 6, 1])
    with inner_col_3[1]:
            st.image('https://raw.githubusercontent.com/celenaaponce/sandbox/main/web_img/Online%20learning-rafiki.png')
    st.button('Registrarse para Clases', key='Clases', on_click = open_page, args =('https://aslparalatinos.streamlit.app/Registrar%20para%20Clases',))
    htmlstr = ChangeButtonColour('Registrarse para Clases', '#fffff', '#92E3A9') 
    components.html(f"{htmlstr}", height=0, width=0)
