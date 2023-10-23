import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components

def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }
        </style>
    """, unsafe_allow_html=True)

def primera_semana():
    set_styles()
    st.subheader('Primera Semana: Introducción')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Recursos</u></h4>", unsafe_allow_html=True)
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Escuelas para los Sordos en EEUU</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.markdown("<a href='https://www.asd-1817.org/deaf-schools' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-20%20at%205.21.38%20PM.png' width= '200' height = '100' /></a>", unsafe_allow_html=True)
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Alarma de Reloj para personas Sordos</h5>', unsafe_allow_html=True)
    with clms31[1]:
        st.markdown("<a href='https://www.diglo.com/vibrating-clocks-and-watches/alarm-clocks;d=3;c=31;s=311' target='_blank'><img style='float: right;' src='https://m.media-amazon.com/images/I/7100+aehKvL._AC_SY300_SX300_.jpg' width='200' height='100'/></a>", unsafe_allow_html=True)     
    clms32 = st.columns([1,1])
    with clms32[0]:
        st.title('')
        st.markdown('<h5>Timbre con luz para personas Sordos</h5>', unsafe_allow_html=True)
    with clms32[1]:    
        st.markdown("<a href='https://www.diglo.com/shop-by-alert-trigger/doorbell-and-door-knock;d=3;c=32;s=323' target='_blank'><img style='float: right;' src = 'https://m.media-amazon.com/images/I/310R2UqXt0L._AC_.jpg' width = '200' height = '100'/></a>", unsafe_allow_html=True)     
    clms33 = st.columns([1,1])
    with clms33[0]:
        st.title('')
        st.markdown('<h5>Alarma de Incendios para personas Sordos</h5>', unsafe_allow_html=True)
    with clms33[1]:     
        st.markdown("<a href='https://www.diglo.com/shop-by-alert-trigger/smoke-and-fire;d=3;c=32;s=328' target='_blank'><img style='float: right;' src='https://m.media-amazon.com/images/I/41JvpGHNyKL.__AC_SX300_SY300_QL70_FMwebp_.jpg' width='200' height = '100'/></a>", unsafe_allow_html=True)
    clms34 = st.columns([1,1])
    with clms34[0]:
        st.title('')
        st.markdown('<h5>Teléfono de Vídeo para personas Sordos</h5>', unsafe_allow_html=True)
    with clms34[1]:         
        st.markdown("<a href='https://purplevrs.com/espanol' target='_blank'><img style='float: right;' src='https://www.purplevrs.com/media/1282/video-quality-slide-v2-450x450.png' width='150' height = '100'/></a>", unsafe_allow_html=True)
    clms35 = st.columns([1,1])
    with clms35[0]:
        st.title('')
        st.markdown('<h5>App para aprender para iPhone </h5>', unsafe_allow_html=True)
    with clms35[1]:      
        st.markdown("<a href='https://apps.apple.com/us/app/intersign-asl-learn-now/id1567327543' target='_blank'><img style='float: right;' src='https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/25/02/e4/2502e491-82e5-8ee1-b462-78f521e117f1/AppIcon-1x_U007emarketing-0-7-0-85-220.png/460x0w.webp' height='100' width='100'/></a>", unsafe_allow_html=True)
    clms36 = st.columns([1,1])
    with clms36[0]:
        st.title('')
        st.markdown('<h5>App para aprender para Android</h5>', unsafe_allow_html=True)
    with clms36[1]:     
        st.markdown("<a href='https://play.google.com/store/apps/details?id=intersign.learn.asl&hl=en_US&gl=US' target='_blank'><img style='float: right;' src='https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/25/02/e4/2502e491-82e5-8ee1-b462-78f521e117f1/AppIcon-1x_U007emarketing-0-7-0-85-220.png/460x0w.webp' height='100' width='100'/></a>", unsafe_allow_html=True)
    clms37 = st.columns([1,1])
    with clms37[0]:
        st.title('')
        st.markdown('<h5>Historia de ASL</h5>', unsafe_allow_html=True)
    with clms37[1]: 
        st.video('https://youtu.be/Pt2_EjmtUp8')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms38 = st.columns([1,1])
    with clms38[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms38[1]: 
        st.video('https://youtu.be/dJBLpQFhujo')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def segunda_semana():
    set_styles()
    st.subheader('Segunda Semana: Conocer La Familia Bravo')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introduccion a La Familia (sin subtitlos) 🔇</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/SITwK-RY11c')
    clms22 = st.columns([1,1])
    with clms22[0]:
        st.title('')
        st.markdown('<h5>Introduccion a La Familia (con subtitlos) 🔈</h5>', unsafe_allow_html=True)
    with clms22[1]:
        st.video('https://youtu.be/gK3cUfN1Lfw')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/TnwmFK1Odqo')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversacion (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/tZk1fKC_7hQ')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversacion (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/5gYPPZFOO6M')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/tKMpJxq7wNk')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/WsoxPTw9j9U')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/633642ed68206040f25bc382' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/633750f5389ee741763d8d57' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/63375bff25e87940d4c32e08' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQd8Y-xcWg9rS517V1gkm3m7O_sEKq_OSo4nQxS2RI2TFew0eR1yjqb1_mhLUfZ9CW1hrApe8mbHNLj/embed?start=false&loop=false&delayms=3000", height=480)
