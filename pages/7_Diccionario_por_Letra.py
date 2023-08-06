import streamlit as st
import base64
import pandas as pd
from pathlib import Path 
import os
import requests
import gdown
from time import sleep
from st_click_detector import click_detector

##constants
alpha_num = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
             12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
             22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'otra'}

alpha_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

##page configs
st.set_page_config(layout="wide", page_title="Diccionario Por Letra")

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

#initialize states
if 'download_letter' not in st.session_state:
   st.session_state.download_letter = False
  
if 'letter' not in st.session_state:
   st.session_state.letter = ""

if 'offset' not in st.session_state:
   st.session_state.offset = 0

if 'prev_letter' not in st.session_state:
   st.session_state.prev_letter = -1

if 'count' not in st.session_state:
  st.session_state.count = 0
  
def empty():
    placeholder.empty()
    sleep(0.01)

@st.cache_data
def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
    st.session_state.download_letter = True
  
@st.cache_data
def load_words_letra():
  csv_length = 0    
  for chunk in pd.read_csv('Search List2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
          data = pd.DataFrame(chunk)
  return data

def set_start(i):
   st.session_state.letter = i

def set_offset(i):
   st.session_state.offset = i

def set_prev(i):
   st.session_state.prev_letter = i

def back_offset(i):
   st.session_state.offset = i - 10

def reset_start():
   set_start("")

placeholder = st.empty()

placeholder_2 = st.empty()

def images(size):
      content= f"""
         <br>
         <br>
         <a href='#' id='Image 1'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/a.gif'></a>
         <a href='#' id='Image 2'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/b.gif'></a>
         <a href='#' id='Image 3'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/c.gif'></a>
         <a href='#' id='Image 4'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/d.gif'></a>
         <a href='#' id='Image 5'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/e.gif'></a>
         <a href='#' id='Image 6'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/f.gif'></a>
         <a href='#' id='Image 7'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/g.gif'></a>
         <a href='#' id='Image 8'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/h.gif'></a>
         <a href='#' id='Image 9'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/i.gif'></a>
         <a href='#' id='Image 10'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/j.gif'></a>
         <a href='#' id='Image 11'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/k.gif'></a>
         <a href='#' id='Image 12'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/l.gif'></a>
         <a href='#' id='Image 13'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/m.gif'></a>
         <a href='#' id='Image 14'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/n.gif'></a>
         <a href='#' id='Image 15'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/o.gif'></a>
         <a href='#' id='Image 16'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/p.gif'></a>
         <a href='#' id='Image 17'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/q.gif'></a>
         <a href='#' id='Image 18'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/r.gif'></a>
         <a href='#' id='Image 19'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/s.gif'></a>
         <a href='#' id='Image 20'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/t.gif'></a>
         <a href='#' id='Image 21'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/u.gif'></a>
         <a href='#' id='Image 22'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/v.gif'></a>
         <a href='#' id='Image 23'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/w.gif'></a>
         <a href='#' id='Image 24'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/x.gif'></a>
         <a href='#' id='Image 25'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/y.gif'></a>
         <a href='#' id='Image 26'><img width='{size}%' src='https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/z.gif'></a>
         <a href='#' id='Image 27'><img width='{size}%' src='https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_1414/BabySignLanguage/DictionaryPages/another-webp.webp'></a>
         """

      clicked = click_detector(content)
      return clicked

def print_list(next_list):
    with placeholder_2.container():
      table = next_list.to_html(classes='mystyle', escape=False, index=False)
      html_string = f'''
  
          <body>
              {table}
          </body>
          '''
      st.markdown(
              html_string,
          unsafe_allow_html=True)
  
#start with download
if st.session_state.download_letter == False:
  download_csv('1bii0vusXl-640sgVhRK2NVj8XCZtGgDx', 'Search List2.csv')
word_data = load_words_letra()


#set up main page with images  
empty()
with placeholder.container():
  clicked = images(10)
  set_start(clicked[6:])

#clicking logic
if st.session_state.letter == '27': 
    set_prev(st.session_state.letter)
    alpha_list = word_data[~word_data.Palabra.str.startswith(alpha_tuple)]
    alpha_list.sort_values(by=['Palabra'])
    max_len = len(alpha_list)
    next_list = alpha_list[0:10]
    print_list(next_list)

if st.session_state.letter != "":
  letter = alpha_num[int(st.session_state.letter)]
  alpha_list = word_data.loc[word_data['Palabra'].str.startswith(letter, na=False)]
  alpha_list.sort_values(by=['Palabra'])
  max_len = len(alpha_list)

  if st.session_state.prev_letter != st.session_state.letter:
    set_prev(st.session_state.letter)
    next_list = alpha_list[0:10]
    offset = st.session_state.offset

  if st.session_state.prev_letter == st.session_state.letter:
    next_list = alpha_list[st.session_state.offset:st.session_state.offset+10]
    offset = st.session_state.offset+10
  print_list(next_list)
  col1, col2, col3 = st.columns([1,1,1])
  if offset < max_len:
      col3.button('Proximas Palabras', on_click=set_offset, args=[st.session_state.offset+10])
  if st.session_state.offset >= 10:
      col1.button('Palabras Anteriores', on_click = back_offset, args=[st.session_state.offset])
