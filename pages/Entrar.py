
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages.sidebars import regular_sidebar, login_sidebar_ASL1, login_sidebar_ASL2, login_sidebar_ASL3, login_sidebar_ASLAtHome2

import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles

if 'password_correct' not in ss:
    ss.password_correct = False
MenuButtons()

st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state['password'] == st.secrets['password']:
                st.session_state["password_correct"] = True
        else:
                st.session_state["password_correct"] = False
with st.form("Credentials"):

    option = st.selectbox(
            '¿Cual clase?',
            ('ASL 1', 'ASL 2', 'ASL 3', 'ASL En Casa'), key='option')
    st.text_input("Contraseña", type="password", key="password")
    st.form_submit_button("Entrar", on_click=password_entered)
if st.session_state.password_correct == True:    
    if st.session_state['option'] == 'ASL 1':
        # MenuButtons('ASL1')
        st.switch_page('./pages/Introduccion_a_ASL_1.py')
    
    elif st.session_state['option'] == 'ASL 2':

        st.switch_page("./pages/Introduccion_a_ASL_2.py")
        
    elif st.session_state['option'] == 'ASL En Casa':

        switch_page("./pages/Introduccion_a_ASL_En_Casa")
    
    elif st.session_state['option'] == 'ASL 3':

        st.switch_page("./pages/Introduccion_a_ASL_3.py")
# else:

#     st.write('wrong password')
