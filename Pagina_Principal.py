import streamlit as st
from PIL import Image

def set_styles():
    st.write("""
        <style>
        h5 {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
  
image = Image.open('Online world-cuate (2).png')
cont_1 = st.container()
cont_2 = st.container()
outer_cols = st.columns([1, 1])
m = st.markdown("""
<style>
div.stButton > button:first-child {
  background-color: #94387F;
  color: #ffffff;
  border: none;
  display: block;
  width: 200px; 
  margin: 0 auto;
}
</style>""", unsafe_allow_html=True)
with cont_1:
    with outer_cols[0]:
        set_styles()
        st.markdown("<h1 style='text-align: center; color: white;'>¡Aprender Lengua de Señas Americana en Su Propia Idioma!</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Para padres Latinos de niños Sordos, sé que hay muchos retos.  Hay bastante que aprender, no solo idioma, pero cultura y más. Mi meta es ayudar padres Latinos entender la lengua de señas americana, sin necesitar saber ingles.  Tambien, quiero ayudar encontrar los recursos que necesitan para que sus hijos pueden tener exitó. </h5>", unsafe_allow_html=True)
    
    with outer_cols[1]:
        inner_cols = st.columns([1, 6, 1])
        with inner_cols[1]:
            st.image(image)
        if st.button('Quien Soy'):
            st.write('Go to quien soy page')
outer_col_2 = st.columns([1, 1])            
with cont_2:
    with outer_col_2[0]:
        inner_col_2 = st.columns([1, 6, 1])
        with inner_col_2[1]:
            st.image(image)
        if st.button('Quien Soy'):
            st.write('Go to quien soy page')
    
    with outer_col_2[1]:
        set_styles()
        st.markdown("<h1 style='text-align: center; color: white;'>¡Aprender Lengua de Señas Americana en Su Propia Idioma!</h1>", unsafe_allow_html=True)
    
        st.markdown("<h5 style='text-align: center; color: white;'>Para padres Latinos de niños Sordos, sé que hay muchos retos.  Hay bastante que aprender, no solo idioma, pero cultura y más. Mi meta es ayudar padres Latinos entender la lengua de señas americana, sin necesitar saber ingles.  Tambien, quiero ayudar encontrar los recursos que necesitan para que sus hijos pueden tener exitó. </h5>", unsafe_allow_html=True)
