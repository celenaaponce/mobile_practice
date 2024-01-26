import streamlit as st
from PIL import Image

class Register: 
    def __init__(self): 
        self.nombre = None
        self.email = None
        self.telefono = None
        self.clases_antes = None
        self.bravo1 = None
        self.bravo2 = None
        self.bravo3 = None
        self.bravo4 = None
        self.bravo6 = None
        self.bravo7 = None
        self.asl1 = None
        self.asl2 = None
        self.asl3 = None
        self.asl4 = None
        self.hijo_edad = None
        self.lunes1 = None
        self.martes15 = None
        self.martes16 = None
        self.martes7 = None
        self.miercoles6 = None
        self.miercoles7 = None
        self.lunes6 = None
        self.lunes7=None
        self.lunes2 = None
        self.martes2 = None
        self.viernes7=None
        self.martes3 = None
        self.martes730 = None
        self.jueves12 = None
        self.sabado11 = None
        self.lunes7=None
        self.miercoles5 = None
        self.sabadoother12 = None
        self.sabadoother1 = None
        self.domingoother10 = None
        self.domingoother11 = None
        self.domingoother12 = None
        self.llamar=None
        self.texto=None
        self.correo = None

img5pm = Image.open('Form/5pm.jpeg')
img6pm = Image.open('Form/6pm.jpeg')
img7pm = Image.open('Form/7pm.jpeg')
img730pm = Image.open('Form/730pm.jpeg')
img11am = Image.open('Form/11am.jpeg')
img12pm = Image.open('Form/12pm.jpeg')
img1pm = Image.open('Form/1pm.jpeg')
img10am = Image.open('Form/10am.jpeg')
def form_phone():
  r = Register()
  st.header("¿Cómo se llama usted?") 
  st.audio('Form/nombre.m4a')
  r.nombre = st.text_input(label = "", placeholder = "Entrar su nombre", label_visibility= "collapsed")
  st.header("¿Cuál es su correo electronico?")
  st.audio('Form/email.m4a')
  r.email = st.text_input(label = "", placeholder = "Entrar su correo electronico", label_visibility= "collapsed")
  st.header("¿Cuál es su número de teléfono?")
  st.audio('Form/telefono.m4a')
  r.telefono = st.text_input(label = "", placeholder = "Entrar su número de teléfono", label_visibility= "collapsed")
  st.header("¿Usted ha tomado clases de lengua de señas antes?")
  st.audio('Form/clases.m4a')
  r.clases_antes = st.radio(label = "", options = ["Si", "No"], label_visibility= "collapsed")
  st.header("¿Cuál temas ya sabe usted?")
  st.audio('Form/temas.m4a')
  r.bravo1 = st.checkbox("familia y básicos (Bravo 1)")
  st.audio('Form/bravo1.m4a')
  r.bravo2 = st.checkbox("desayuno (Bravo 2)")
  st.audio('Form/bravo2.m4a')
  r.bravo3 = st.checkbox("casa (Bravo 3)")
  st.audio('Form/casa.m4a')
  r.bravo4 = st.checkbox("comida y ir de compras (Bravo 4)")
  st.audio('Form/bravo4.m4a')
  r.bravo6 = st.checkbox("colores y letras (Bravo 6)")
  st.audio('Form/bravo6.m4a')
  r.bravo7 = st.checkbox("escuela (Bravo 7)")
  st.audio('Form/bravo7.m4a')
  r.asl1 = st.checkbox("hora de comer (ASL En Casa 1)")
  st.audio('Form/asl1.m4a')
  r.asl2 = st.checkbox("hora de bañar (ASL En Casa 2)")
  st.audio('Form/asl2.m4a')
  r.asl3 = st.checkbox("hora de cambiar el pañal (ASL En Casa 3)")
  st.audio('Form/asl3.m4a')
  r.asl4 = st.checkbox("hora de leer (ASL En Casa 4)")
  st.audio('Form/asl4.m4a')
  st.header("¿Cuantos años tiene su hijo sordo?")
  st.audio('Form/edad.m4a')
  r.hijo_edad = st.radio(label="", label_visibility = "collapsed", options = ["0-4 años", "5+ años", "Soy maestro"])
  st.divider()
  st.header("¿Cuándo se puede tomar clases? (Escoja todos que se puede)")
  st.subheader("Las horas son de tiempo Pacífico.  Mira a la mapa para saber la hora en su area.")
  st.audio('Form/tiempo.m4a')
  st.subheader("ASL 1 (Primer Semestre)")
  st.audio('Form/primer.m4a')
  r.lunes1 = st.checkbox("Lunes a las 7 pm", key="lunes1")
  st.audio('Form/lunes7.m4a')
  st.image(img7pm, width=300)
  r.martes15 = st.checkbox("Martes a las 5 pm", key="martes15")
  st.audio('Form/martes5.m4a')        
  st.image(img5pm, width=300)
  r.martes16 = st.checkbox("Martes a las 6 pm", key="martes16")
  st.audio('Form/martes6.m4a')
  st.image(img6pm, width=300)
  r.martes7 = st.checkbox("Martes a las 7 pm")
  st.audio('Form/martes7.m4a')      
  st.image(img7pm, width=300)
  r.miercoles6 = st.checkbox("Miércoles a las 6 pm")
  st.audio('Form/miercoles6.m4a') 
  st.image(img6pm, width=300)
  r.miercoles7 = st.checkbox("Miércoles a las 7 pm")
  st.audio('Form/miercoles7.m4a')         
  st.image(img7pm, width=300)
  st.divider()
  st.subheader("ASL 2 (Segundo Semestre)")
  st.audio('Form/segundo.m4a')
  r.lunes5 = st.checkbox("Lunes a las 5 pm")
  st.audio('Form/lunes5.m4a')
  st.image(img5pm, width=300)
  r.lunes6 = st.checkbox("Lunes a las 6 pm")
  st.audio('Form/lunes6.m4a')
  st.image(img6pm, width=300)
  r.lunes2 = st.checkbox("Lunes a las 7 pm", key="lunes2")
  st.audio('Form/lunes7.m4a')        
  st.image(img7pm, width=300)
  r.martes2 = st.checkbox("Martes a las 6 pm", key="martes2")
  st.audio('Form/martes6.m4a')        
  st.image(img6pm, width=300)
  r.viernes7 = st.checkbox("Viernes a las 7 pm")
  st.audio('Form/viernes7.m4a')       
  st.image(img7pm, width=300)
  st.divider
  st.subheader("ASL 3 (Tercer Semestre)")
  st.audio('Form/tercer.m4a') 
  r.martes3 = st.checkbox("Martes a las 5 pm", key="martes3")
  st.audio('Form/martes5.m4a')              
  st.image(img5pm, width=300)
  r.martes730 = st.checkbox("Martes a las 7:30 pm")
  st.audio('Form/martes730.m4a')                     
  st.image(img730pm, width=300)
  r.jueves12 = st.checkbox("Jueves a las 12 pm")
  st.audio('Form/jueves12.m4a')   
  st.image(img12pm, width=300)
  r.sabado11 = st.checkbox("sábado a las 11 am")
  st.audio('Form/sabado11.m4a')        
  st.image(img11am, width=300)
  st.divider()
  st.subheader("ASL En Casa (niños de 0-4 años)")
  st.audio('Form/encasa.m4a') 
  r.lunes7 = st.checkbox("Lunes a las 7 pm")
  st.audio('Form/lunes7.m4a')                
  st.image(img7pm, width=300)
  r.miercoles5 = st.checkbox("Miércoles a las 5 pm")
  st.audio('Form/miercoles5.m4a')       
  st.image(img5pm, width=300)
  st.divider()
  st.subheader("Necesito otra horario.  Estoy disponible...")
  st.audio('Form/otro.m4a')
  r.sabadoother12 = st.checkbox("Sábado a las 12 pm", key='sabadoother12')
  st.audio('Form/sabado12.m4a')      
  st.image(img12pm, width=300)
  r.sabadoother1 = st.checkbox("Sábado a la 1 pm", key='sabadoother1')
  st.audio('Form/sabado1.m4a')     
  st.image(img1pm, width=300)
  r.domingoother10 = st.checkbox("Domingo a las 10 am", key='domingoother10')
  st.audio('Form/domingo10.m4a')        
  st.image(img10am, width=300)
  r.domingoother11 = st.checkbox("Domingo a las 11 am", key='domingoother11')
  st.audio('Form/domingo11.m4a') 
  st.image(img11am, width=300)
  r.domingoother12 = st.checkbox("Domingo a las 12 pm", key='domingoother12')
  st.audio('Form/domingo12.m4a') 
  st.image(img12pm, width=300)
  st.divider()
  st.subheader("¿Cuál es el mejor modo de contacto?")
  st.audio('Form/contacto.m4a')
  r.llamar = st.checkbox("Llamada")
  st.audio('Form/llamada.m4a')  
  r.texto = st.checkbox("Texto")
  st.audio('Form/texto.m4a')  
  r.correo = st.checkbox("Correo Electronico")
  st.audio('Form/correoelectronico.m4a')  
  return r
