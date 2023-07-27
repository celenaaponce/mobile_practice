import streamlit as st
from PIL import Image

def set_image_size():
    st.write("""
        <style>
        img {
            max-width: 100%;
            height: auto;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
  
image = Image.open('Online world-cuate (2).png')

col1, col2 = st.columns(2)
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
with col1:
    st.title('¡Aprender Lengua de Señas Americana en Su Propia Idioma!')
    st.caption('Para padres Latinos de niños Sordos, sé que hay muchos retos.  Hay bastante que aprender, no solo idioma, pero cultura y más. Mi meta es ayudar padres Latinos entender la lengua de señas americana, sin necesitar saber ingles.  Tambien, quiero ayudar encontrar los recursos que necesitan para que sus hijos pueden tener exitó.')

with col2:
    set_image_size()
    st.image(image, width=153)
    if st.button('Quien Soy'):
        st.write('Go to quien soy page')
