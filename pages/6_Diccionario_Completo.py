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

with open("streamlit_website/css/style.css") as f:
    style = f.read()

with open("streamlit_website/css/bootstrap.css") as file:
    boot = file.read()

with open("streamlit_website/css/responsive.css") as file2:
    resp = file2.read()

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)   

remote_css("https://fonts.googleapis.com/css?family=Poppins:400,700|Raleway:400,600&display=swap")
remote_css("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css")
def create_bulleted_list(lst):

    if type(lst) == str:
        lst = lst.split(',')
    tag = "<ul>"
    for word in lst:
       if word != 'nan':
        tag += "<li>{}</li>".format(word)
    tag += "</ul>"

    return tag
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width=150>".format(
      img_to_bytes(img_path)
    )
    return img_html
    
def download_csv(file_id, output_file):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_file, quiet=False)

download_csv('1ynYsJEwmJEiCqfDEbTzvBDvHWHKNZeLG', 'Small Preview2.csv')
st.success("File downloaded successfully!")


csv_length = 0    
for chunk in pd.read_csv('Small Preview2.csv', names=['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino'], chunksize=10000, skiprows=1):
        data = pd.DataFrame(chunk)
        csv_length += chunk.count()

word_data = data
# groupby_column = 'word'
# aggregate_column = 'theme'
# agg_df = word_data.groupby(groupby_column).aggregate({aggregate_column: list})
# df_alias = word_data.drop(columns=aggregate_column).set_index(groupby_column)
# word_data = agg_df.join(df_alias).reset_index(groupby_column).drop_duplicates(groupby_column).reset_index(drop=True)
# word_data.columns = ['word', 'theme', 'link', 'image', 'synonym']
# word_data = word_data.rename(columns={"word": "Palabra", "theme": "Tema", "link": "Enlace", "image": "Imagen", "synonym": "Sinómino"})
# for index, row in word_data.iterrows():
#   link = row['Enlace']
#   lst = row['Tema']
#   tag = create_bulleted_list(lst)
#   try:
#     lst2 = row['Sinónimo']
#     tag2 = create_bulleted_list(lst2)
#     word_data.at[index, 'Sinómino'] = tag2
#   except:
#      word_data.at[index, 'Sinómino'] = "<ul>""</ul>"
#   word_data.at[index, 'Tema'] = tag

#   word_data.at[index, 'Enlace'] = f"<iframe width='210' height='158' src=https://www.youtube.com/embed/{link}></iframe>"
#   if type(row['Imagen']) != float:
#     word_data.at[index, 'Imagen'] = img_to_html('images/dict/{}'.format(row['Imagen']))
#   else:
#     word_data.at[index, 'Imagen'] =  "<ul>""</ul>"

word_data.columns = ['Palabra', 'Tema', 'Video', 'Imagen', 'Sinómino']
word_data.sort_values(by=['Palabra'])
first_50 = word_data.head(offset)
pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

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
