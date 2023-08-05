import streamlit as st
import streamlit.components.v1 as com
import base64
import pandas as pd
from pathlib import Path 
import gdown

offset = 50

#session states
if 'download' not in st.session_state:
   st.session_state.download = False
    
if 'start' not in st.session_state:
   st.session_state.start = 0   
     
def download_csv(file_id, output_file):
    st.write('state', st.session_state.download)
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
    st.session_state.download = True
    
if st.session_state.download == False:
    download_csv('1ynYsJEwmJEiCqfDEbTzvBDvHWHKNZeLG', 'Small Preview2.csv')

@st.cache_data
def load_words_completo():   
  for chunk in pd.read_csv('Small Preview2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
          data = pd.DataFrame(chunk)
  return data
    
word_data = load_words_completo()
word_data.sort_values(by=['Palabra'])

#change states
def set_start(i):
   st.session_state.start = i

def back_start(i):
   st.session_state.start = i-2*offset

start = st.session_state.start
max_len = len(word_data)
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
reset1 = col2.button("Empezar de Nuevo", key="First", on_click=set_start, args=[0])
                
if start != offset:
    reset2 = st.button("Palabras Anteriores", on_click=back_start, args=[start])
