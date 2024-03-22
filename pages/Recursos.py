import streamlit as st
from PIL import Image
from pages.sidebars import regular_sidebar, set_styles
from streamlit.components.v1 import html
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

outer_col_5 = st.columns([1, 1])            

    
with outer_col_5[0]:
    style_html = set_styles('#C53F3F')
    st.write(style_html, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Recursos</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Recursos para familias latinas con hijos sordos </h5>", unsafe_allow_html=True)

with outer_col_5[1]:
    inner_col_5 = st.columns([1, 6, 1])
    with inner_col_5[1]:
            st.image('https://raw.githubusercontent.com/celenaaponce/sandbox/main/web_img/Selecting%20team-pana.png')

st.divider()
st.markdown("<h3>Manos y Voces</h3> \
              <p><a href='https://www.facebook.com/groups/manosyvoces' target='_blank'>Manos y Voces</a> está dedicada a ayudar \
                a las familias con niños sordos o con dificultades auditivas, de manera imparcial respecto a modos o \
                    metodologías de comunicación.</p>", unsafe_allow_html=True)

st.divider()
st.markdown("<h3>Escuelas para los Sordos</h3>\
              <p><a href='https://www.asd-1817.org/deaf-schools' target='_blank'>Escuelas para los Sordos</a> son escuelas de varías niveles, \
            desde kinder al 12vo grado. Algunas son publicas.  Las que son públicos son gratis y algunos tienen dormitorios donde los niños pueden quedar \
                si no viven cerca. Es un lugar buenisimo para niños sordos para aprender más de su cultura y su idioma.</p>", unsafe_allow_html = True)

st.divider()
st.markdown("<h3>Centros para Sordos</h3>\
              <p><a href='https://www.nad.org/resources/directories/state-agencies-of-deaf-hoh/' target='_blank'>Centros para Sordos</a> son\
                  lugares que ayudan a personas sordas a encontrar recursos de cualquier tipo.  Algunos también tienen actividades u otros \
                    servicios.</p>", unsafe_allow_html=True)

st.divider()
st.markdown("<h3>Council de Manos</h3>\
              <p> <a href='https://www.facebook.com/councildemanos' target='_blank'>Council de Manos</a> es una organización sin \
                ánimo de lucro para la comunidad latinx sorda, originalmente se llamaba Consejo Nacional de Sordos y Hipoacúsicos \
                    Hispano; “NCDHH”. </p>", unsafe_allow_html=True)
