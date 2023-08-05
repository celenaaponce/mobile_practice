import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])
df.sort_values(by=['Palabra'])

next_list = df[0:50]
table = next_list.to_html(classes='mystyle', escape=False, index=False)
html_string = f'''
    <body>
        {table}
    </body>
    '''
st.markdown(
        html_string,
    unsafe_allow_html=True)
