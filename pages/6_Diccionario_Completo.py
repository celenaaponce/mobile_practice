import streamlit as st
import streamlit.components.v1 as com
import base64
import pandas as pd
from pathlib import Path 
import gdown
from st_pages import Page, Section,show_pages, add_page_title

show_pages(
[
    Page("Pagina_Principal.py", "Pagina Principal"),
    Page("pages/1_Diccionario.py", "Diccionario"),
    Page("pages/2_Clases.py", "Clases"),
    Page("pages/3_Libros.py", "Libros"),
    Page("pages/4_Recursos.py", "Recursos"),
    Page("pages/5_Sobre_Yo.py", "Sobre Yo"),
    Page("pages/6_Diccionario_Completo.py", "Diccionario Completo"),
    Page("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra"),
    Page("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema"),
    Page("pages/9_Buscar_Palabra.py", "Buscar Palabra"),
    Page("pages/10_Entrar.py", "Entrar")
])
#formatting
offset = 20
st.set_page_config(layout="wide", page_title="Diccionario Completo")
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with open("css/style.css") as f:
    style = f.read()

with open("css/bootstrap.css") as file:
    boot = file.read()

with open("css/responsive.css") as file2:
    resp = file2.read()

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   

remote_css("https://fonts.googleapis.com/css?family=Poppins:400,700|Raleway:400,600&display=swap")
remote_css("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css")

#session states
if 'download_completo' not in st.session_state:
   st.session_state.download_completo = False
    
if 'start' not in st.session_state:
   st.session_state.start = 0   

def download_csv(file_id, output_file):
    url = 'https://drive.google.com/file/d/1n7QzMyGJanRjU-19AYHTsWseomZi_sFl/view?usp=drive_link'
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    df = pd.read_csv(path)
    for chunk in pd.read_csv(path, names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
      data = pd.DataFrame(chunk)
    # url = f'https://drive.google.com/uc?id={file_id}'
    # gdown.download(url, output_file, quiet=False)
    st.session_state.download_completo = True
    return data
    
if st.session_state.download_completo == False:
    download_csv(st.secrets["diccionario_completo"], 'Small Preview2.csv')

@st.cache_data
def load_words_completo():  
  for chunk in pd.read_csv('Small Preview2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
          data = pd.DataFrame(chunk)
  return data
    
word_data = download_csv(st.secrets["diccionario_completo"], 'Small Preview2.csv')
word_data = word_data[['Palabra', 'Imagen', 'Video', 'Tema', 'Sinómino']]
word_data.sort_values(by=['Palabra'])

#change states
def set_start(i):
   st.session_state.start = i

def back_start(i):
   st.session_state.start = i-2*offset

start = st.session_state.start
max_len = len(word_data)
next_list = word_data[start:offset+start]
table = next_list.to_html(classes='mystyle', escape=False, index=False)
html_string = f'''
    <body>
        {table}
    </body>
    '''
st.markdown(
        html_string,
    unsafe_allow_html=True)
start += offset
col1, col2, col3 = st.columns([1,1,1])
if start == offset:
    increment = col3.button("Proximas Palabras", on_click=set_start, args=[start])

else:              
    increment = col3.button("Proximas Palabras", on_click=set_start, args=[start])
    reset1 = col2.button("Empezar de Nuevo", on_click=set_start, args=[0])
    reset2 = col1.button("Palabras Anteriores", on_click=back_start, args=[start])
