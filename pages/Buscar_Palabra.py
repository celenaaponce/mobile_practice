import streamlit as st
import pandas as pd
from modules.nav import MenuButtons
from check.spanish_word_freq import SpanishWordFreq
from check.word_chekcer import WordChecker

st.set_page_config(layout="wide", page_title="Buscar Palabra")
MenuButtons('')
st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

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

def replace_dimensions(template):
    x = "width='410'"
    y = "height='317'"    
    return template.replace("width='x'", str(x)).replace("height='y'", str(y))

def replace_dimensions_img(template):
    z = "width=300"  
    return template.replace("width=z", str(z)) 
    
@st.cache_data
def download_csv(file_id, output_file):
    path = f'https://drive.google.com/uc?export=download&id={file_id}'
    for chunk in pd.read_csv(path, names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
      data = pd.DataFrame(chunk)
    st.session_state.download = True
    return data
  
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
  download_csv(st.secrets['diccionario_test'], 'Search List2.csv')

word_data = download_csv(st.secrets['diccionario_test'], 'Search List2.csv')
word_data = word_data[['Palabra', 'Imagen', 'Video', 'Tema', 'Sinómino']]
word_data['Video'] = word_data['Video'].apply(replace_dimensions)
word_data['Imagen'] = word_data['Imagen'].apply(replace_dimensions_img)
word_data = word_data.drop('Tema', axis=1)
st.write("")
st.header("Buscar Palabra")
word = st.text_input("Buscar Palabra", label_visibility="hidden")

word_list = word_data.loc[word_data['Palabra']==word]
word_data['Palabra_no_acc'] = word_data['Palabra'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
word_list_no_acc = word_data.loc[word_data['Palabra_no_acc']==word]
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
    
elif not word_list_no_acc.empty and word != "":
        word_list_no_acc = word_list_no_acc.drop('Palabra_no_acc', axis=1)
        table = word_list_no_acc.to_html(classes='mystyle', escape=False, index=False)

        html_string = f'''

            <body>
                {table}
            </body>
            '''
        st.markdown(
                html_string,
            unsafe_allow_html=True)
else:
    if word != "":
        word_list = word_data.loc[word_data['Palabra'].str.startswith(word)]
        word_list_no_acc = word_data.loc[word_data['Palabra_no_acc'].str.startswith(word)]
        word_list = word_list.drop('Palabra_no_acc', axis=1)
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
        elif not word_list_no_acc.empty:   
            word_list_no_acc = word_list_no_acc.drop('Palabra_no_acc', axis=1)
            table = word_list_no_acc.to_html(classes='mystyle', escape=False, index=False)

            html_string = f'''

                <body>
                    {table}
                </body>
                '''
            st.markdown(
                    html_string,
                unsafe_allow_html=True)
if word_list.empty and word != "" and word_list_no_acc.empty:
    
    filePath = "pages/helper/10000_frecuencias.txt"

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
