import streamlit as st
import pandas as pd
import gdown
from st_click_detector import click_detector
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
st.set_page_config(layout="wide", page_title="Diccionario Por Tema")
increment = None
reset1 = False
reset2 = False
placeholder = st.empty()
page_one = st.empty()
page_two = st.empty()

if "count" not in st.session_state:
    st.session_state.count = 0

if "clicked" not in st.session_state:
    st.session_state.clicked = ""
    
if 'download_tema' not in st.session_state:
    st.session_state.download_tema = False

themes = {1: 'Plano de Casa', 2: 'Día de los Muertos', 4: 'Dia de San Valentin', 3: 'Halloween', 5: 'Primavera', 6: 'Quehaceres', 7: 'Exterior de Casa', 8: 'Más Comida', 9: 'Día de Acción de Gracias', 
          10: 'Frutas', 11: 'Verduras', 12: 'Carnes', 13: 'Interior de Casa', 14: 'Bravo 1', 15: 'Bravo 2', 16: 'Bravo 3', 17: 'Bravo 4', 18: 'Números', 19: "Pascua", 20: "Colores"}

def get_content(size):
      content= f"""
        <style>{style}</style>
        <style>{boot}</style>
        <style>{resp}</style>
        <div class="image-container">

        <div class="cat-container">
         <a href='#' id='Image 1'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1556156653-e5a7c69cc263?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80'></a>
         <p class="caption">Plano de Casa</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 2'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1601325979086-d54da2c7419c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80'></a>
         <p class="caption">Día de los Muertos</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 3'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1508361001413-7a9dca21d08a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aGFsbG93ZWVufGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Halloween</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 4'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1581022295087-35e593704911?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dmFsZW50aW5lcyUyMGRheXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Día de San Valentin</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 5'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1490750967868-88aa4486c946?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c3ByaW5nfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Primavera</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 6'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1582479429421-321775166674?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDJ8fGNob3Jlc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Quehaceres</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 7'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1588880331179-bc9b93a8cb5e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8b3V0c2lkZSUyMG9mJTIwaG91c2V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Exterior de Casa</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 8'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1498837167922-ddd27525d352?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGZvb2R8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Más Comida</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 9'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1605926637412-b0cd5a3e3543?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dGhhbmtzZ2l2aW5nfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Día de Acción de Gracias</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 10'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1619566636858-adf3ef46400b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ZnJ1aXR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Frutas</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 11'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1566385101042-1a0aa0c1268c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHZlZ2V0YWJsZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Verduras</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 12'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bWVhdHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Carnes</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 13'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1591247378418-c77f1532d2f8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8aW5zaWRlJTIwaG91c2V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Interior de Casa</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 14'><img class = "cat" width='{size}%' src='https://org-dcmp-staticassets.s3.us-east-1.amazonaws.com/posterimages/1287_1.jpg'></a>
         <p class="caption">Bravo 1</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 15'><img class = "cat" width='{size}%' src='https://org-dcmp-staticassets.s3.us-east-1.amazonaws.com/posterimages/1242_1.jpg'></a>
         <p class="caption">Bravo 2</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 16'><img class = "cat" width='{size}%' src='https://org-dcmp-staticassets.s3.us-east-1.amazonaws.com/posterimages/1329_1.jpg'></a>
         <p class="caption">Bravo 3</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 17'><img class = "cat" width='{size}%' src='https://org-dcmp-staticassets.s3.us-east-1.amazonaws.com/posterimages/1283_1.jpg'></a>
         <p class="caption">Bravo 4</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 18'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1502570149819-b2260483d302?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bnVtYmVyc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Números</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 19'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1551524612-4b158646bc05?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGVhc3RlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Pascua</p> 
         </div>
        <div class="cat-container">
         <a href='#' id='Image 20'><img class = "cat" width='{size}%' src='https://images.unsplash.com/photo-1500042600524-37ecb686c775?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Y29sb3JzfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60'></a>
         <p class="caption">Colores</p> 
         </div>
         """
      return content

def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)
    st.session_state.download = True

@st.cache_data
def load_words_tema():
  csv_length = 0    
  for chunk in pd.read_csv('Themes2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
        data = pd.DataFrame(chunk)
  data = data[['Palabra', 'Imagen', 'Video', 'Tema', 'Sinómino']]
  return data

with open("css/style.css") as f:
    style = f.read()

with open("css/bootstrap.css") as file:
    boot = file.read()

with open("css/responsive.css") as file2:
    resp = file2.read()

#start with download
if st.session_state.download_tema == False:
  download_csv(st.secrets['diccionario_tema'], 'Themes2.csv')
  st.session_state.download_tema = True
    
word_data = load_words_tema()

if st.session_state.clicked == "":
    size = 20
    with placeholder.container():
      content = get_content(size)
      clicked = click_detector(content)

    st.session_state.clicked = clicked

if st.session_state.clicked != "" and not (reset1 or reset2):
    page_two.empty()
    placeholder.empty()
    word_data = load_words_tema()
    tema = themes[int(st.session_state.clicked[6:])]
    alpha_list = word_data.loc[word_data['Tema']== tema]
    alpha_list.sort_values(by=['Tema'])
    max_len = len(alpha_list)
    next_list = alpha_list[0:10]
    table = next_list.to_html(classes='mystyle', escape=False, index=False)
    html_string = f'''

        <body>
            {table}
        </body>
        '''
    with page_one.container():
        st.markdown(
                html_string,
            unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        increment = col3.button("Proximas Palabras")
        reset1 = col2.button("Empezar de Nuevo", key="First")
           
if increment:
    page_one.empty()
    word_data = load_words_tema()
    tema = themes[int(st.session_state.clicked[6:])]
    alpha_list = word_data.loc[word_data['Tema']== tema]
    alpha_list.sort_values(by=['Tema'])
    max_len = len(alpha_list)
    next_list = alpha_list[10:]
    table = next_list.to_html(classes='mystyle', escape=False, index=False)
    html_string = f'''
        <body>
            {table}
        </body>
        '''
    with page_two.container():
        st.markdown(
                html_string,
            unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        reset2 = col1.button("Palabras Anteriores", key="Second")
        reset1 = col2.button("Empezar de Nuevo")

if reset1 or reset2:
    page_one.empty()
    page_two.empty()
    st.session_state.count = 0
    st.session_state.clicked = ""
    size = 20
    with placeholder.container():
        content = get_content(size)
        clicked = click_detector(content)

