import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages import holidays
from st_pages import Page, Section,show_pages, add_page_title

def main():
        login_sidebar_ASL2()
        st.header("Bienvenido a la clase de ASL 2.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab2, tab3, tab4, tab5, tab6 = st.tabs([":white[Repaso General]", ":white[Repaso Leccion 1]", ":white[Repaso Leccion 2]", 
                                                                               ":white[Repaso Leccion 3]", ":white[Repaso Leccion 4]"])

        with tab2:
             repaso_general()
        with tab3:
             repaso_lecc1()
        with tab4:
             repaso_lecc2()
        with tab5:
             repaso_lecc3()
        with tab6:
             repaso_lecc4()

def login_sidebar_ASL2():
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
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_2.py", "Introducción a ASL 2"),
        # Page("pages/Bravo_5.py", "Repaso"),
        # Page("pages/Bravo_6.py", "Colores y Deletrear"),
        # Page("pages/Bravo_7.py", "Escuela"),
        Page("pages/holidays_spring_2.py", "Días Festivos")
    ]
)

def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }

        </style>
    """, unsafe_allow_html=True)

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

main()
