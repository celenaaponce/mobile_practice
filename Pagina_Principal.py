import streamlit as st
from PIL import Image
from streamlit_nested_layout import .

image = Image.open('Online world-cuate (2).png')

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
with outer_cols[0]:
    st.markdown("<h1 style='text-align: center; color: white;'>¡Aprender Lengua de Señas Americana en Su Propia Idioma!</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Para padres Latinos de niños Sordos, sé que hay muchos retos.  Hay bastante que aprender, no solo idioma, pero cultura y más. Mi meta es ayudar padres Latinos entender la lengua de señas americana, sin necesitar saber ingles.  Tambien, quiero ayudar encontrar los recursos que necesitan para que sus hijos pueden tener exitó. </h5>", unsafe_allow_html=True)

with outer_cols[1]:
    inner_cols = st.columns([1, 6, 1])
    with inner_cols[1]:
        st.image(image)
    if st.button('Quien Soy'):
        st.write('Go to quien soy page')
