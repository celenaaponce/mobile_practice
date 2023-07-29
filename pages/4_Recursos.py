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
            background-color: #C53F3F;

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

image5 = Image.open('/Users/celenap/streamlit/Selecting team-pana.png')
outer_col_5 = st.columns([1, 1])            

    
with outer_col_5[0]:
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'>Recursos</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Recursos para familias Latinos con hijos Sordos </h5>", unsafe_allow_html=True)

with outer_col_5[1]:
    inner_col_5 = st.columns([1, 6, 1])
    with inner_col_5[1]:
        st.image(image5)

st.divider()
st.markdown("<h3>Manos y Voces</h3> \
              <p><a href='https://www.facebook.com/groups/manosyvoces' target='_blank'>Manos y Voces</a> está dedicada a ayudar \
                a las familias con niños sordos o con dificultades auditivas, de manera imparcial respecto a modos o \
                    metodologías de comunicación.</p>", unsafe_allow_html=True)

st.divider()
st.markdown("<h3>Escuelas para los Sordos</h3>\
              <p><a href='https://www.asd-1817.org/deaf-schools' target='_blank'>Escuelas para los Sordos</a> son escuelas de varias niveles, \
            kinder al 12 grado. Algunos son publicos.  Los que son publicos son gratis y algunos tienen dormitorios donde niños pueden quedar \
                si no viven cerca. Es un lugar buenisimo para niños sordos aprender más de su cultura y su idioma.</p>", unsafe_allow_html = True)

st.divider()
st.markdown("<h3>Centros para Sordos</h3>\
              <p><a href='https://www.nad.org/resources/directories/state-agencies-of-deaf-hoh/' target='_blank'>Centros para Sordos</a> son\
                  lugares que ayudan personas sordos encontrar recursos de cualquier tipo.  Algunos tambien tienen actividades o otros \
                    servicios.</p>", unsafe_allow_html=True)

st.divider()
st.markdown("<h3>Council de Manos</h3>\
              <p> <a href='https://www.facebook.com/councildemanos' target='_blank'>Council de Manos</a> es una organización sin \
                ánimo de lucro para la comunidad latinx sorda, originalmente se llamaba Consejo Nacional de Sordos y Hipoacúsicos \
                    Hispano; “NCDHH”. </p>", unsafe_allow_html=True)