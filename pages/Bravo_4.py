import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages.sidebars import login_sidebar_ASL2, set_styles
from modules.nav import MenuButtons
st.markdown("""
    <style>
        div[data-testid="stSidebarNav"]{
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
def main():
    MenuButtons('ASL2')
    st.header("Bienvenido a la clase de ASL 2.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab8, tab9 = st.tabs([":white[Ir de Compras Pt 1]", ":white[Ir de Compras Pt 2]"])

    with tab8:
            sexta_semana()
    with tab9:
            septima_semana()

def sexta_semana():
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
    st.subheader('Ir de Compras Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/QfY4zeab69Q')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/6Dbp71UxqJY')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/pz5LEqddIDQ')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/g7aQQtj_q3E')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/svea2_E319M')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/640e3ec8402db6429355fbc7' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/640e40e2c28bef42d1fbf5b5' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRMkndgYUQ5rjWxVstqfyYliiyF8bVHOwW2LtzR0A7JR4MytscEpWmn-IoWF6a7H85cjoMA8b4EOv_g/embed?start=false&loop=false&delayms=3000", height=480)

def septima_semana():
    style_html = set_styles('#94387f')
    st.write(style_html, unsafe_allow_html=True)
    # st.subheader('¿Dónde está el contról? Pt 2')
    # st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    # clms23 = st.columns([1,1])
    # with clms23[0]:
    #     st.title('')
    #     st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    # with clms23[1]:
    #     st.video('https://youtu.be/w2Q1H8Ajowk')
    # clms24 = st.columns([1,1])
    # with clms24[0]:
    #     st.title('')
    #     st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    # with clms24[1]:    
    #     st.video('https://youtu.be/DPWS7MuTJTA')
    # clms25 = st.columns([1,1])
    # with clms25[0]:
    #     st.title('')
    #     st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    # with clms25[1]: 
    #     st.video('https://youtu.be/i5ieZX-EqVg')
    # clms26 = st.columns([1,1])
    # with clms26[0]:
    #     st.title('')
    #     st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    # with clms26[1]:
    #     st.video('https://youtu.be/v0XQlYYHrhU')
    # clms29 = st.columns([1,1])
    # with clms29[0]:
    #     st.title('')
    #     st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    # with clms29[1]:
    #     st.video('https://youtu.be/8DJyVNDRDcU')
    # clms30 = st.columns([1,1])
    # with clms30[0]:
    #     st.title('')
    #     st.markdown('<h5>Cuento (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    # with clms30[1]:    
    #     st.video('https://youtu.be/qkIXqIf9oNs')
    # clms31 = st.columns([1,1])
    # with clms31[0]:
    #     st.title('')
    #     st.markdown('<h5>Cuento (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    # with clms31[1]: 
    #     st.video('https://youtu.be/9Hm6lIC5F2o')        
    # st.divider()

    # st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    # clms28 = st.columns([1,1])
    # with clms28[0]:
    #     st.title('')
    #     st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    # with clms28[1]:
    #     st.markdown("<a href='https://edpuzzle.com/media/640bd6c89bbb9e42a124866b' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
    #     st.markdown("<a href='https://edpuzzle.com/media/640e37f0b6a56042bd07b94c' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/puzzle.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    # st.divider()
            
    # components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ8stRFQOfu2FuAFsKrcmFSnmB6MZv4hPdR5FLOoKKik-VRNJE8Py2PHiJ-7B2JXBEie2I_CvnwShjR/embed?start=false&loop=false&delayms=3000", height=480)
main()
