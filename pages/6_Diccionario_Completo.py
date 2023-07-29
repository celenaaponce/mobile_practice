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

download_csv('1ynYsJEwmJEiCqfDEbTzvBDvHWHKNZeLG', 'Small Preview2.csv')

csv_length = 0    
for chunk in pd.read_csv('Small Preview2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
        data = pd.DataFrame(chunk)
        csv_length += chunk.count()

word_data = data
word_data.columns = ['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino']
word_data.sort_values(by=['Palabra'])
first_50 = word_data.head(offset)
pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

@st.cache_data
def load_data(frame):
  table = frame.to_html(classes='mystyle', escape=False, index=False)
  return table

if 'start' not in st.session_state:
   st.session_state.start = 0

def set_start(i):
   st.session_state.start = i

def back_start(i):
   st.session_state.start = i-2*offset

if st.session_state.start == 0:
  start = st.session_state.start
  table = load_data(first_50)
  html_string = f'''

      <body>
          {table}
      </body>
      '''
  st.markdown(
          html_string,
      unsafe_allow_html=True
  )
  start += offset
  col1, col2, col3 = st.columns([1,1,1])
  st.write("")
  col3.button('Proximas Palabras', on_click=set_start, args=[start])

if st.session_state.start >= offset:
  start = st.session_state.start
  next_list = word_data[start:start+offset]
  table = load_data(next_list)
  html_string = f'''

      <body>
          {table}
      </body>
      '''
  st.markdown(
          html_string,
      unsafe_allow_html=True
  )
  start += offset
  st.write("")
  col1, col2, col3 = st.columns([1,1,1])
  col3.button('Proximas Palabras', on_click=set_start, args=[start])
  col1.button('Palabras Anteriores', on_click=back_start, args=[start])
  col2.button('Regresar al Principio', on_click=set_start, args=[0])
