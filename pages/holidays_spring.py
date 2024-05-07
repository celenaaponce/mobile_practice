import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages.sidebars import login_sidebar_ASL1
from modules.nav import MenuButtons

st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
def main():
    MenuButtons('ASL1')
    st.header("Bienvenido a la clase de ASL 1.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs([ ":white[Primavera]", ":white[Semana Santa]", ":white[Paises Latinos]", ":white[Pascua]", ":white[Día de las Madres]", ":white[Clasificadores]"])

    with tab1:
            spring()
    with tab2:
            semana_santa()
    with tab3:
            pais_latino()
    with tab4:
            pascua()
    with tab5:
            madres()
    with tab6:
            clasificadores()

def spring():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario de la Primavera</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://www.youtube.com/watch?v=1XRJRt2dlNc')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Camino de la Primavera (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=nhRxdkqXghc')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Camino de la Primavera (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://www.youtube.com/watch?v=xs-LBiqID50')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Cuento de la Primavera</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://youtu.be/spE7JQHC9Zw')
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQWQGDfD9frtoRelg1LUY82AfX61Uncc62N2cOlLlR6m_rVaBFQLd0y7sEROoLbOwN3LHV0aCIIcHPA/embed?start=false&loop=false&delayms=3000", height=480)
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/0VXhaIS3ytk')

def semana_santa():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario General</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/ldm6mEvjHsk')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Domingo de Ramos</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/NiVsgq8aE7Y')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Jueves Santo</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://youtu.be/4q3hgVOLsnc')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Viernes Santo</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://youtu.be/4q3hgVOLsnc')  
    clms4 = st.columns([1,1])
    with clms4[0]:
        st.title('')
        st.markdown('<h5>Cuento de Pascua</h5>', unsafe_allow_html=True)
    with clms4[1]:
        st.video('https://youtu.be/RONMK52bc8w') 
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/JbA5HvJg_N0')
        
def pais_latino():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>America Central</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://youtu.be/8MXqNlUBLPE')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>America del Sur</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/2MH7znNtk-o')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Puerto Rico</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://www.youtube.com/watch?v=NNZD9RAgL4w')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Cuba</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://www.youtube.com/watch?v=lDmOnxjPNds')  
    clms4 = st.columns([1,1])
    with clms4[0]:
        st.title('')
        st.markdown('<h5>Republica Dominicana</h5>', unsafe_allow_html=True)
    with clms4[1]:
        st.video('https://www.youtube.com/watch?v=mKTAsHCqDeg') 
    clms5 = st.columns([1,1])
    with clms5[0]:
        st.title('')
        st.markdown('<h5>America del Norte</h5>', unsafe_allow_html=True)
    with clms5[1]:
        st.video('https://youtu.be/v-3nyi1nlO8') 
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/J6KR1Q-WncQ')

def pascua():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://www.youtube.com/watch?v=MnjLnFQwGh0')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Historia de Pascua Religioso</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=RONMK52bc8w')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Mi Conejo de Pascua</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://www.youtube.com/watch?v=4PJhGhRublE')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/stPphI_xp2I')

def madres():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://www.youtube.com/watch?v=b3hjbAaMth0')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Spot Ama a su Mamá</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=TzYfajBnCAQ')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/hf_C7G4fI4I')

def clasificadores():
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Explicación de Clasificadores</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.video('https://www.youtube.com/watch?v=3nOq-Uf2s_8')
    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Clasificadores Semánticos</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://www.youtube.com/watch?v=ey-CIuDQitI')
    clms2 = st.columns([1,1])
    with clms2[0]:
        st.title('')
        st.markdown('<h5>Clasificadores de Instrumentos</h5>', unsafe_allow_html=True)
    with clms2[1]:
        st.video('https://www.youtube.com/watch?v=QLaSaKvpNeI')
    clms3 = st.columns([1,1])
    with clms3[0]:
        st.title('')
        st.markdown('<h5>Juego de Clasificadores</h5>', unsafe_allow_html=True)
    with clms3[1]:
        st.video('https://edpuzzle.com/media/66288bcd6f8573a03611e1c7')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Grabación de la Clase</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/BPX98o0BgBw')
main()

