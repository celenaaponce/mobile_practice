import streamlit as st
from streamlit import session_state as ss
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from modules.nav import MenuButtons

st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
CONFIG_FILENAME = 'pages/config.yaml'

if 'is_register' not in ss:
    ss.is_register = False


with open(CONFIG_FILENAME) as file:
    config = yaml.load(file, Loader=SafeLoader)


def add_role(username_to_add_role, new_role='user'):
    with open(CONFIG_FILENAME) as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Check if the necessary keys exist before modifying the config
    if 'credentials' in config and 'usernames' in config['credentials'] and username_to_add_role in config['credentials']['usernames']:
        config['credentials']['usernames'][username_to_add_role]['role'] = new_role

        with open(CONFIG_FILENAME, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)


def get_roles():
    """Gets user roles based on config file."""
    with open(CONFIG_FILENAME) as file:
        config = yaml.load(file, Loader=SafeLoader)

    if config is not None:
        cred = config['credentials']
    else:
        cred = {}

    return {username: user_info['role'] for username, user_info in cred['usernames'].items() if 'role' in user_info}


st.header('Procesando...')


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login(location='main')

if ss["authentication_status"]:
    authenticator.logout(location='main')    
    st.write(f'Welcome *{ss["name"]}*')

elif ss["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif ss["authentication_status"] is None:
    st.warning('Please enter your username and password')



# We call below code in case of registration, reset password, etc.
with open(CONFIG_FILENAME, 'w') as file:
    yaml.dump(config, file, default_flow_style=False)



# Call this late because we show the page navigator depending on who logged in.
MenuButtons(get_roles())
