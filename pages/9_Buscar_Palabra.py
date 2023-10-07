import streamlit as st
import pandas as pd
import sys
import gdown
sys.path.append('streamlit_website/check')

from check.spanish_word_freq import SpanishWordFreq
from check.word_chekcer import WordChecker

st.set_page_config(layout="wide", page_title="Buscar Palabra")

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
# Add css to make text bigger
st.markdown(
    """
    <style>
    write {
        font-size: 5rem !important;
    }
    input {
        font-size: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def download_csv(file_id, output_file):
    st.write('downloading')
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
    st.session_state.download = True
  
@st.cache_data
def load_words():
  csv_length = 0    
  for chunk in pd.read_csv('Search List2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
        data = pd.DataFrame(chunk)
  return data
    
with open("css/style.css") as f:
    style = f.read()

with open("css/bootstrap.css") as file:
    boot = file.read()

with open("css/responsive.css") as file2:
    resp = file2.read()
    
if 'download' not in st.session_state:
   st.session_state.download = False
    
#start with download
if st.session_state.download == False:
  download_csv(st.secrets['diccionario_letras'], 'Search List2.csv')

word_data = load_words()
word_data = word_data[['Palabra', 'Imagen', 'Video', 'Tema', 'Sinómino']]

st.write("")
st.header("Buscar Palabra")
word = st.text_input("Buscar Palabra", label_visibility="hidden")

word_list = word_data.loc[word_data['Palabra']==word]

if not word_list.empty:
    table = word_list.to_html(classes='mystyle', escape=False, index=False)

    html_string = f'''

        <body>
            {table}
        </body>
        '''
    st.markdown(
            html_string,
        unsafe_allow_html=True)
    
else:
    word_data['Palabra'] = word_data['Palabra'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    word_list = word_data.loc[word_data['Palabra']==word]
    table = word_list.to_html(classes='mystyle', escape=False, index=False)

    html_string = f'''

        <body>
            {table}
        </body>
        '''
    st.markdown(
            html_string,
        unsafe_allow_html=True)
    
if word_list.empty and word != "":
    filePath = "pages/10000_frecuencias.txt"

    spanishWords = SpanishWordFreq(filePath)
    
    wordChecker = WordChecker(spanishWords.words, spanishWords.totalFreq)
         
    list = wordChecker.getCorrection(word.lower())

    st.write(f"La palabra {word} no exista en este diccionario")
    suggestions = ""
    for item in list:
        if item != word:
            suggestions += item + ' o '
    if suggestions[:-3] != "":
        st.write(f"¿Usted quiere buscar {suggestions[:-3]}?")
