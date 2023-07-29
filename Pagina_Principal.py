import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

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
  
image = Image.open('/Users/celenap/streamlit/Online world-cuate (2).png')
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
    
        st.markdown("<h5 style='text-align: center; color: white;'>Para padres Latinos de niños Sordos, sé que hay muchos retos.  Hay bastante que aprender, no solo idioma, pero cultura y más. Mi meta es ayudar padres Latinos entender la lengua de señas americana, sin necesitar saber ingles.  Tambien, quiero ayudar encontrar los recursos que necesitan para que sus hijos pueden tener exitó. </h5>", unsafe_allow_html=True)
    
    with outer_cols[1]:
        inner_cols = st.columns([1, 6, 1])
        with inner_cols[1]:
            st.image(image)
        st.button('Quien Soy', key='Quien')
        ChangeButtonColour('Quien Soy', '#fffff', '#94387f') 


st.divider()
image2 = Image.open('/Users/celenap/streamlit/dictionary.png')

outer_col_2 = st.columns([1, 1])            
with cont_2:
    
    with outer_col_2[1]:
        set_styles()
        st.markdown("<h2 style='text-align: center; color: white;'>Diccionario</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Buscar señas y frases en un diccionario de Español a ASL </h5>", unsafe_allow_html=True)
    
    with outer_col_2[0]:
        inner_col_2 = st.columns([1, 6, 1])
        with inner_col_2[1]:
            st.image(image2)
        st.button('Diccionario', key='Dict')
        ChangeButtonColour('Diccionario', '#fffff', '#407bff') 

st.divider()
image3 = Image.open('/Users/celenap/streamlit/Online learning-rafiki.png')
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
        st.button('Clases', key='Clases')
        ChangeButtonColour('Clases', '#fffff', '#92E3A9') 

st.divider()
image4 = Image.open('/Users/celenap/streamlit/Absorbed in-pana.png')

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
        st.button('Libros', key='Libros')
        ChangeButtonColour('Libros', '#fffff', '#FF725E') 

st.divider()
image5 = Image.open('/Users/celenap/streamlit/Selecting team-pana.png')
outer_col_5 = st.columns([1, 1])            
with cont_5:
    
    with outer_col_5[0]:
        set_styles()
        st.markdown("<h2 style='text-align: center; color: white;'>Recursos</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Recursos para familias Latinos con hijos Sordos </h5>", unsafe_allow_html=True)
    
    with outer_col_5[1]:
        inner_col_5 = st.columns([1, 6, 1])
        with inner_col_5[1]:
            st.image(image5)
        st.button('Recursos', key='Recursos')
        ChangeButtonColour('Recursos', '#fffff', '#C53F3F') 
