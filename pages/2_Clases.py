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
            background-color: #92E3A9;

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
image3 = Image.open('Online learning-rafiki.png')
outer_col_3 = st.columns([1, 1])            

with outer_col_3[0]:
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'>Clases</h1>", unsafe_allow_html=True)

    st.markdown("<p> Con <a href='https://www.cdhy.wa.gov' target='_blank'>CDHY</a> ofrezco clases todo el año.  Ahorita tenemos clases un vez a la mes, ofrecido en linea.  Durante el año escolar, tenemos clases cada semana.  Las clases son individuos y a su nivel.  ¡Tambien son gratis!  Si quiere mirar clases del pasado, se puede <a href='https://www.youtube.com/playlist?list=PLAsRcYXV-4XDbhawYIWMukc53mP-zbRqv' target='_blank'>mirar las clases.</a> </p>", unsafe_allow_html=True)

with outer_col_3[1]:
    inner_col_3 = st.columns([1, 6, 1])
    with inner_col_3[1]:
        st.image(image3)
    st.button('Registrar para Clases', key='Clases', on_click = open_page, args =('https://forms.gle/JUcjHnvhpGVrg6t17',))
    ChangeButtonColour('Registrar para Clases', '#fffff', '#92E3A9') 
