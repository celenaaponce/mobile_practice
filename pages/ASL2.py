import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages
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
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def repaso_general():
    clms2 = st.columns([1,1])
    with clms2[0]:
      st.title('')
      st.title('')
      st.subheader('Introducción')
    with clms2[1]:
      st.video('https://youtu.be/c1T1CoU0luo')
    clms26=st.columns([1,1])
    with clms26[0]:
      st.title('')
      st.title('')
      st.subheader('Cultura')
    with clms26[1]:
      st.video('https://youtu.be/t7HzlXNmFJc')
    clms27=st.columns([1,1])
    with clms27[0]:
      st.title('')
      st.title('')
      st.subheader('Gramática')
    with clms27[1]:
      st.video('https://youtu.be/nBCvy22r6bo')
    clms28=st.columns([1,1])
    with clms28[0]:
      st.title('')
      st.title('')
      st.subheader('Cuento (sin subtítulos) 🔇')
    with clms28[1]:
      st.video('https://youtu.be/a0s8Zw6T3Fw')  
    clms29=st.columns([1,1])
    with clms29[0]:
      st.title('')
      st.title('')
      st.subheader('Cuento (con subtítulos) 🔈')
    with clms29[1]:
      st.video('https://youtu.be/GLXz2s5jBAw')    
    st.divider()

def repaso_lecc1():
    st.markdown("<h3 style='text-align: center; color: white;'><u>Lección 1</u></h3>", unsafe_allow_html=True)
    clms3 = st.columns([1,1])
    with clms3[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario y Frases')
    with clms3[1]:
      st.video('https://youtu.be/CD9CUAlcRW4')
    clms4 = st.columns([1,1])
    with clms4[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (sin subtítlos) 🔇')
    with clms4[1]:
      st.video('https://youtu.be/a6bMKje9kOY')
    clms5 = st.columns([1,1])
    with clms5[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítulos) 🔈')
    with clms5[1]:
      st.video('https://youtu.be/fVmnEqqhlpw')

    clms6 = st.columns([1,1])
    with clms6[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms6[1]:
      st.video('https://youtu.be/tZk1fKC_7hQ')
    clms7 = st.columns([1,1])
    with clms7[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms7[1]:
      st.video('https://youtu.be/5gYPPZFOO6M')

def repaso_lecc2():
    st.markdown("<h3 style='text-align: center; color: white;'><u>Lección 2</u></h3>", unsafe_allow_html=True)
    clms8 = st.columns([1,1])
    with clms8[0]:
        st.title('')
        st.title('')
        st.subheader('Vocabulario y Frases')

    with clms8[1]:
        st.video('https://youtu.be/qxd4OUEOCJg')
    clms9 = st.columns([1,1])
    with clms9[0]:
        st.title('')
        st.title('')
        st.subheader('Diálogo (sin subtítlos) 🔇')  
    with clms9[1]:
        st.video('https://youtu.be/_SDd08h_UEM')
    clms10=st.columns([1,1])
    with clms10[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítulos) 🔈')
    with clms10[1]:
      st.video('https://youtu.be/KOUtXRQ3kFw')
    clms11=st.columns([1,1])
    with clms11[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms11[1]:
      st.video('https://youtu.be/JHFhfpjI3CE')
    clms12=st.columns([1,1])
    with clms12[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms12[1]:
      st.video('https://youtu.be/x494aKUmEKM')

def repaso_lecc3():
    st.markdown("<h3 style='text-align: center; color: white;'><u>Lección 3</u></h3>", unsafe_allow_html=True)
    clms13=st.columns([1,1])
    with clms13[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario')
    with clms13[1]:
      st.video('https://youtu.be/_kva3v4OB2E')
    clms14=st.columns([1,1])
    with clms14[0]:
      st.title('')
      st.title('')
      st.subheader('Frases')
    with clms14[1]:
      st.video('https://youtu.be/IQyhNdrhuR8')
    clms15=st.columns([1,1])
    with clms15[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (sin subtítlos) 🔇')
    with clms15[1]:
      st.video('https://youtu.be/z1EEtsE79-w')
    clms16=st.columns([1,1])
    with clms16[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítlos) 🔈')
    with clms16[1]:
      st.video('https://youtu.be/5QM2LGdQWvs')
    clms17=st.columns([1,1])
    with clms17[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms17[1]:
      st.video('https://youtu.be/8-9YtAezNAE')
    clms18=st.columns([1,1])
    with clms18[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms18[1]:
      st.video('https://youtu.be/XeXLA8-rWyo')
    clms19=st.columns([1,1])

def repaso_lecc4():
    st.markdown("<h3 style='text-align: center; color: white;'><u>Lección 4</u></h3>", unsafe_allow_html=True)
    clms20=st.columns([1,1])
    with clms20[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario')
    with clms20[1]:
      st.video('https://youtu.be/OZL7UyN6wSw')
    clms21 = st.columns([1,1])
    with clms21[0]:
      st.title('')
      st.title('')
      st.subheader('Frases')
    with clms21[1]:
      st.video('https://youtu.be/CpQNPG2ZxtQ')
    clms22=st.columns([1,1])
    with clms22[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (sin subtítlos) 🔇')
    with clms22[1]:
      st.video('https://youtu.be/beZlTXitb0g')
    clms23=st.columns([1,1])
    with clms23[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítlos)')
    with clms23[1]:
      st.video('https://youtu.be/ZABG-Zl5qzE?si=JW6JDpHmrYmp_pRt')
    clms24=st.columns([1,1])
    with clms24[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms24[1]:
      st.video('https://youtu.be/qktiKSw2kpQ')
    clms25=st.columns([1,1])
    with clms25[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms25[1]:
      st.video('https://youtu.be/qktiKSw2kpQ')
    st.divider()
    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms30=st.columns([1,1])
    with clms30[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario para la semana que viene')
    with clms30[1]:
      st.video('https://youtu.be/sVyvzKH_Nsg')  
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ1DBN424b45UbbrNNEHmSvzFqMDfsnLSR2nLK2eS93kdLU3bdQep_btALoKoWxZu0K644csijPRwuP/embed?start=false&loop=false&delayms=3000", height=480)

def colores():
    set_styles()
    st.subheader('Lección 6: Colores')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introduccion 🔇</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/WEhwFHOw6lI')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/sVyvzKH_Nsg')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversacion (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/h53mMpcm858')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversacion (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/yX6p56ur8RI')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/LUPeVp1Kbwg')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/tMqFbxcjx2o')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/6535ed2547faa53fdf53a7b9' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/6535ed4ea59f3e4030d8a224' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/6535f557ac44ed3fd6871438' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vS-egJOarNNRcNvBhPhStuG04-I0IXmy9eflIea8NagDNyx574U7FK8skAPB_9SP0u_W-3CIL67w62D/embed?start=false&loop=false&delayms=3000", height=480)

def deletrear():
    set_styles()
    st.subheader('Lección 6: Deletrear')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Vocabulario </h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/tMqFbxcjx2o')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/JrtFuHaFp90')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Entender Deletrear </h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/122DzyFbysE')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Cuento del Alfabeto</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/G_clys0BzVM')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/jDeJWEgCnF0')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/0q9CCJWzFfU')
    clms30 = st.columns([1,1])
    with clms30[0]:
        st.title('')
        st.markdown('<h5>Cuento (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms30[1]:    
        st.video('https://youtu.be/VNnV8okNbP8')
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Cuento (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms31[1]: 
        st.video('https://youtu.be/P8IFhqRgEdI')        
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/4kpYIF-edx0')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/6561ba3bf53b4c415ee4ec79' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/6561c188f996c941653fc5a0' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQXb3L7FrMl7nGhW4MFw_6CT2CKW5MKOBCyI0x9HoNvGuLdhMqcN1fecVAXi2xRkTavM_dwXx1r1RQJ/embed?start=false&loop=false&delayms=3000", height=480)

def escuela1():
    set_styles()
    st.subheader('Lección 7: Escuela')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introduccion </h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/oQQFZSlr-7c')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicacion</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/U0I58rdwlDkg')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversacion (sin subtitulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/Ey_qhboMTmo')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversacion (con subtitulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/qa3gM93D85c')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/HhilwM-rUPk')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/axnjssoujJQ')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/656832c8714d964171966867' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/65683015dc1e1641a09708ad' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTaL-csLK4bnmmbonxNSjLb0lgzB22X8rQahAOtdtEo0zRHKgQ6RTWEBwIOw2yy4DXaI6PauEFEDu78/embed?start=false&loop=false&delayms=3000", height=480)
