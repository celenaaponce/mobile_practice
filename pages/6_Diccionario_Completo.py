import streamlit as st
import streamlit.components.v1 as com
import base64
import pandas as pd
from pathlib import Path 
import gdown

offset = 50
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
placeholder = st.empty()
page_one = st.empty()
page_two = st.empty()
with open("css/style.css") as f:
    style = f.read()

with open("css/bootstrap.css") as file:
    boot = file.read()

with open("css/responsive.css") as file2:
    resp = file2.read()

if 'download' not in st.session_state:
   st.session_state.download = False
    
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   

remote_css("https://fonts.googleapis.com/css?family=Poppins:400,700|Raleway:400,600&display=swap")
remote_css("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css")
    
def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
    st.session_state.download = True
    
if st.session_state.download == False:
    download_csv('1ynYsJEwmJEiCqfDEbTzvBDvHWHKNZeLG', 'Small Preview2.csv')

@st.cache_data
def load_words_completo():
  csv_length = 0    
  for chunk in pd.read_csv('Small Preview2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
          data = pd.DataFrame(chunk)
  return data
    
word_data = load_words_completo()
word_data.sort_values(by=['Palabra'])

if 'start' not in st.session_state:
   st.session_state.start = 0

def set_start(i):
   st.session_state.start = i

def back_start(i):
   st.session_state.start = i-2*offset

# if st.session_state.start == 0:
#   st.write(st.session_state.download)
#   start = st.session_state.start
#   table = first_50.to_html(classes='mystyle', escape=False, index=False)
#   html_string = f'''

#       <body>
#           {table}
#       </body>
#       '''
#   st.markdown(
#           html_string,
#       unsafe_allow_html=True
#   )
#   start += offset
#   col1, col2, col3 = st.columns([1,1,1])
#   st.write("")
#   col3.button('Proximas Palabras', on_click=set_start, args=[start])

# if st.session_state.start >= offset:
#   st.write(st.session_state.download)
#   start = st.session_state.start
#   next_list = word_data[start:start+offset]
#   table = next_list.to_html(classes='mystyle', escape=False, index=False)
#   html_string = f'''

#       <body>
#           {table}
#       </body>
#       '''
#   st.markdown(
#           html_string,
#       unsafe_allow_html=True
#   )
#   start += offset
#   st.write("")
#   col1, col2, col3 = st.columns([1,1,1])
#   col3.button('Proximas Palabras', on_click=set_start, args=[start])
#   col1.button('Palabras Anteriores', on_click=back_start, args=[start])
#   col2.button('Regresar al Principio', on_click=set_start, args=[0])

if st.session_state.start == 0:
    page_two.empty()
    placeholder.empty()
    with page_one.container():
        start = st.session_state.start
        max_len = len(word_data)
        next_list = word_data[0:offset]
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
        increment = col3.button("Proximas Palabras", on_click=set_start, args=[start])
        reset1 = col2.button("Empezar de Nuevo", key="First", on_click=set_start, args=[0])
                
if st.session_state.start != 0:
    page_one.empty()
    with page_two.container():
        start = st.session_state.start
        next_list = word_data[start:start+offset]
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
        increment = col3.button("Proximas Palabras", on_click=set_start, args=[start])
        reset1 = col2.button("Empezar de Nuevo", on_click=set_start, args=[0])
        reset2 = st.button("Palabras Anteriores", on_click=back_start, args=[start])
