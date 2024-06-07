import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages.sidebars import regular_sidebar, ChangeButtonColour, set_styles
import streamlit.components.v1 as components
from modules.nav import MenuButtons

st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

MenuButtons('')

m = st.markdown("""
<style>
div.stButton > button:first-child {
  border: none;
  display: block;
  width: 200px; 
  margin: 0 auto;
}
</style>""", unsafe_allow_html=True)


outer_col_2 = st.columns([1, 1])            

with outer_col_2[1]:
    style_html = set_styles('')
    st.write(style_html, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Diccionario</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'> Este diccionario es señas en la lengua de ASL, con videos. También tiene fotos, y voz en español. </h5>", unsafe_allow_html=True)

with outer_col_2[0]:
    inner_col_2 = st.columns([1, 6, 1])
    with inner_col_2[1]:
          st.image('https://raw.githubusercontent.com/celenaaponce/sandbox/main/web_img/dictionary.png')
st.divider()
outer_col = st.columns([1,1])
st.divider()
with outer_col[0]:
    compl = st.button('Diccionario Completo', key='Completo')
    htmlstr = ChangeButtonColour('Diccionario Completo', '#fffff', '#407bff') 
    components.html(f"{htmlstr}", height=0, width=0)
    if compl:
         switch_page('Diccionario_Completo')
with outer_col[1]:
        st.markdown("<h5 style='text-align: center; color: white;'> Mirar el diccionario completo</h5>", unsafe_allow_html=True)

outer_col_3 = st.columns([1,1])
st.divider()
with outer_col_3[0]:
    letra = st.button('Buscar por Letra', key='Letra')
    htmlstr = ChangeButtonColour('Buscar por Letra', '#fffff', '#407bff') 
    components.html(f"{htmlstr}", height=0, width=0)
    if letra:
        switch_page('Diccionario_por_Letra')
with outer_col_3[1]:
         st.markdown("<h5 style='text-align: center; color: white;'> Buscar palabras por letra inicial </h5>", unsafe_allow_html=True)

outer_col_4 = st.columns([1,1])
st.divider()
with outer_col_4[0]:
    tema = st.button('Buscar por Tema', key='Tema')
    htmlstr = ChangeButtonColour('Buscar por Tema', '#fffff', '#407bff') 
    components.html(f"{htmlstr}", height=0, width=0)
    if tema:
         switch_page('Diccionario_por_Tema')
with outer_col_4[1]:
    st.markdown("<h5 style='text-align: center; color: white;'> Buscar palabras por tema </h5>", unsafe_allow_html=True)

outer_col_5 = st.columns([1,1])
st.divider()
with outer_col_5[0]:
    palabra = st.button('Buscar Palabra', key='Palabra')
    htmlstr = ChangeButtonColour('Buscar Palabra', '#fffff', '#407bff') 
    components.html(f"{htmlstr}", height=0, width=0)
    if palabra:
         switch_page('Buscar_Palabra')
with outer_col_5[1]:
    st.markdown("<h5 style='text-align: center; color: white;'> Buscar palabra usando búsqueda</h5>", unsafe_allow_html=True)
