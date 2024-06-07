import streamlit as st
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

outer_col_4 = st.columns([1, 1])      
with outer_col_4[1]:
    style_html = set_styles('#FF725E')
    st.write(style_html, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Libros</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: center; color: white;'>Mirar videos de libros en español con ASL </h5>", unsafe_allow_html=True)

with outer_col_4[0]:
    inner_col_4 = st.columns([1, 6, 1])
    with inner_col_4[1]:
        st.image('https://raw.githubusercontent.com/celenaaponce/sandbox/main/web_img/Absorbed%20in-pana.png')


outer_col = st.columns([1,1])
with outer_col[0]:
    st.markdown("<a href='https://youtu.be/trV9g7OWAss?si=JDXrHR_5RjPnjYTa' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/jirafas%20no%20pueden%20bailar.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/mkgxSLa_QFE' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/la%20arana%20muy%20ocupada.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/qp9jl0ECUwA' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/banarse.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/AShZlHInWEU' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/eresunavaca.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/iZU9UJeOjOU' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/lindobebecito.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/Z-qNfedG3Hk' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/oceanocolorido.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://www.youtube.com/watch?v=62NbByFKX7Y' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/charla.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/q7QTDovFA74' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/meal.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/4PJhGhRublE' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/bunny.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/TzYfajBnCAQ' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/spot.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/spE7JQHC9Zw' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/spring.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/ce7ftN5dVJs' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/Ananaya.png'></a>", unsafe_allow_html=True)
with outer_col[1]:
    st.markdown("<a href='https://youtu.be/xqJVGpVjJZg' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/el%20libro%20de%20colores%20de%20coneja%20blanca.jpeg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://www.youtube.com/watch?v=wQCkUbaZLQQ' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/como%20dan%20las%20buenas%20noches%20los%20dinosaurios.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/tvyr6wu4dL4' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/cabezaapie.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/HA29CwpR_-0' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/escuela.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/zLrhnfSa8cc' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/munecas.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/4i582v8lTdI' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/muertos.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/4TmdTAaPYdA' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/bath.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/P9Iqri1OHd4' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/valentin.png'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/k3RtcrTMl-Q' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/poop.jpg'></a>", unsafe_allow_html=True)
    st.markdown("<a href='https://youtu.be/RONMK52bc8w' target='_blank'><img width='300' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/images/pascua.webp'></a>", unsafe_allow_html=True)



