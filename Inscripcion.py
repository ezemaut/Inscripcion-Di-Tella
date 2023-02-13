
USUARIO = ''            # DNI
CONTRASENA = ''        # DDMMYYxxx (fecha nacimiento + ultimos 3 digitos DNI)

Materia1 = ''                   
Materia2 = ''
Materia3 = ''                   
Materia4 = ''
Materia5 = ''

# Poner los links de las materias
# Si queres menos de 5, llenar las que queres y no tocar el resto
# No se peuden hacer 6 materias sin pedir permiso a SPE

# CORRER en consola:
# pip install selenium
# pip install pysimplegui

# Prueben que esten bien el usario y contra antes del horario de inscripcion.
#Correr codigo ANTES de horario de inscripcion

#############################################################################


# CODIGO


##################################################################################



from selenium import webdriver     
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import PySimpleGUI as sg


# Abre Firefox y pone sigedu
driver = webdriver.Firefox()
driver.get('https://sigedu.utdt.edu/utdt/principal/login.jsp')

# Espera que cargue
time.sleep(.5)

# Guarda en las variables las posciones de los componentes para LOGIN
usuario = driver.find_element(By.NAME, "usuario")
password = driver.find_element(By.NAME, "clave")
submit_button = driver.find_element(By.NAME, "conectar")

# Escribe credenciales y entra
usuario.send_keys(USUARIO)
password.send_keys(CONTRASENA)
submit_button.click()

# no se si hace falta
driver.get('https://sigedu.utdt.edu/utdt/alumnos/inscripcion_cursos.jsp')


ls = [Materia1, Materia2, Materia3, Materia4, Materia5]

def inscribir() -> None:
    # Inscribe en materias
    for link in ls:
        if link != '':
            driver.get(link)
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
    
    # Abre pagina que dice donde SI estas inscripto
    driver.get('https://sigedu.utdt.edu/utdt/alumnos/ver_inscripcion.jsp')


#GUI
sg.theme('PythonPlus')

text_esperar = sg.Text("Esperar al horario de inscripción y apretar GO", font=("Helvetica",35))
text_vacio = sg.Text("", font=("Helvetica",20))
text_cerrar = sg.Text("Solo cerrar cuando estes inscripto a las materias", font=("Helvetica",25))
text_volver = sg.Text("Podes volver a apretar GO si lo hiciste antes de tiempo\n\n\n", font=("Helvetica",15))

butt_GO = sg.Button("GO", size=(10,1), font=("Helvetica",35))
butt_Cerrar = sg.Button("Cerrar", size=(10,1), font=("Helvetica",35), disabled=True)

GO_cerrar = butt_GO, butt_Cerrar

layout = [
            [text_esperar],
            [text_vacio],
            [text_cerrar],
            [text_volver],
            [GO_cerrar]
         ]
window = sg.Window("Inscripciones", layout,margins=(200, 200),finalize=True,element_justification='center')

while True:
    event, values = window.read()

    if event == "GO":
            window["Cerrar"].update(disabled=False)
            inscribir()
            time.sleep(.5)
    if event == "Cerrar":
         window.close()
    if event == sg.WIN_CLOSED:
        break




