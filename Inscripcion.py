
USUARIO = ''            # DNI
CONTRASEÑA = ''        # DDMMYYxxx (fecha nacimiento + ultimos 3 digitos DNI)

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

#GUI
sg.theme('PythonPlus')

### PANTALLA Start ### (Aparece solo si vaica (or))
text_Username = sg.Text("Username:  ", font=("Helvetica",35))
in_text_User = sg.In('', key = "-IN_User-")
text_Contraseña = sg.Text("Contraseña:", font=("Helvetica",35))
in_text_Pass = sg.In('', key = "-IN_Pass-")
butt_OK_start = sg.Button("OK", key = "OK_start", size=(10,1), font=("Helvetica",35), bind_return_key=True)
text_info_start = sg.T("\n\n\nUsername   = DNI\nContraseña = DDMMYYxxx (fecha nacimiento + ultimos 3 digitos DNI)", font=("Helvetica",15))

linea1 = [text_Username, in_text_User]
linea2 = [text_Contraseña, in_text_Pass]
espacio_start = [sg.T("\n\n")]
linea3 = [sg.Push(), butt_OK_start, sg.Push()]
linea4= [text_info_start]

layout_START = [
                linea1,
                linea2,
                espacio_start,
                linea3,
                linea4]

### PANTALLA Links ### (Aparece solo si vaica (and))
Text_linea1_links = sg.T(f"User: {USUARIO}\tContraseña: {CONTRASEÑA}", key = 'link_linea1')
Txt_Mat1_links = sg.T("Link 1:", font=("Helvetica",25))
Txt_Mat2_links = sg.T("Link 2:", font=("Helvetica",25))
Txt_Mat3_links = sg.T("Link 3:", font=("Helvetica",25))
Txt_Mat4_links = sg.T("Link 4:", font=("Helvetica",25))
Txt_Mat5_links = sg.T("Link 5:", font=("Helvetica",25))
In_Mat1_links = sg.In('', key = "-IN_Link1-", size=(60,1))
In_Mat2_links = sg.In('', key = "-IN_Link2-", size=(60,1))
In_Mat3_links = sg.In('', key = "-IN_Link3-", size=(60,1))
In_Mat4_links = sg.In('', key = "-IN_Link4-", size=(60,1))
In_Mat5_links = sg.In('', key = "-IN_Link5-", size=(60,1))

linea1 = [sg.Push(), Text_linea1_links, sg.Push()]
linea2 = [sg.Push(),Txt_Mat1_links, In_Mat1_links,sg.Push()]
linea3 = [sg.Push(),Txt_Mat2_links, In_Mat2_links,sg.Push()]
linea4 = [sg.Push(),Txt_Mat3_links, In_Mat3_links,sg.Push()]
linea5 = [sg.Push(),Txt_Mat4_links, In_Mat4_links,sg.Push()]
linea6 = [sg.Push(),Txt_Mat5_links, In_Mat5_links,sg.Push()]
linea6_5 = [sg.T("",key= "Vacio_link")]
linea7 = [sg.Button("OK", key = "OK_link", size=(10,1), font=("Helvetica",35), bind_return_key=True
                    ), sg.Button("Atras", key = "Atras_link", size=(10,1), font=("Helvetica",35))]

layout_LINKS = [linea1,
                linea2,
                linea3,
                linea4,
                linea5,
                linea6,
                linea6_5,
                linea7]

### PANTALLA GO ###
text_esperar = [sg.Push(), sg.Text("Esperar al horario de inscripción y\n\tapretar GO", font=("Helvetica",40)), sg.Push()]
text_vacio = sg.Text("", font=("Helvetica",20))
text_cerrar = [sg.Push(),sg.Text("Solo cerrar cuando estes inscripto a las materias", font=("Helvetica",25)), sg.Push()]
text_volver = [sg.Push(),sg.Text("Podes volver a apretar GO si lo hiciste antes de tiempo\n\n\n", font=("Helvetica",15)), sg.Push()]
butt_GO = sg.Button("GO", size=(10,1), font=("Helvetica",35), bind_return_key=True, key ='GO')
butt_Cerrar = sg.Button("Cerrar", size=(10,1), font=("Helvetica",35), disabled=True)
GO_cerrar = [sg.Push()]
GO_cerrar.append(butt_GO)
GO_cerrar.append(butt_Cerrar)
GO_cerrar.append(sg.Push())

layout_GO = [
            text_esperar,
            [text_vacio],
            text_cerrar,
            text_volver,
            GO_cerrar
         ]

layout1 = sg.Column(layout_START, visible=False, key='-COL1-')
layout2 = sg.Column(layout_LINKS, visible=False, key='-COL2-')
layout3 = sg.Column(layout_GO, visible=False, key='-COL3-')


layout = [[layout1, layout2, layout3]]
window = sg.Window("Inscripciones", layout,margins=(200, 200),finalize=True,element_justification='center')
EXIT = 0

if len(USUARIO) == 0 or len(CONTRASEÑA) == 0:
    window['-COL1-'].update(visible=True)
    while True:
        event, values = window.read()
        if event == "OK_start":
            if len(values["-IN_User-"]) > 0:
                USUARIO = values["-IN_User-"]
            if len(values["-IN_Pass-"]) > 0:    
                CONTRASEÑA = values['-IN_Pass-']
            window['-COL1-'].update(visible=False)
            window['link_linea1'].update(f"User: {USUARIO}\tContraseña: {CONTRASEÑA}")
            break
        if event == sg.WIN_CLOSED:
            EXIT = 1
            break

Materias_vacias:bool = len(Materia1) == 0 and len(Materia2) == 0 and len(Materia3) == 0 and len(Materia4) == 0 and len(Materia5) == 0

if Materias_vacias and EXIT == 0:
    window['-COL2-'].update(visible=True)
    while True:
        event, values = window.read()
        if event == "OK_link":
            Materia1 = values["-IN_Link1-"]                   
            Materia2 = values["-IN_Link2-"]
            Materia3 = values["-IN_Link3-"]                   
            Materia4 = values["-IN_Link4-"]
            Materia5 = values["-IN_Link5-"]
            window['-COL2-'].update(visible=False)
            break
        if event == 'Atras_link':
            window['-COL2-'].update(visible=False)
            window['-COL1-'].update(visible=True)
        if event == "OK_start":
            if len(values["-IN_User-"]) > 0:
                USUARIO = values["-IN_User-"]
            if len(values["-IN_Pass-"]) > 0:    
                CONTRASEÑA = values['-IN_Pass-']
            window['-COL1-'].update(visible=False)
            window['-COL2-'].update(visible=True)
            window['link_linea1'].update(f"User: {USUARIO}\tContraseña: {CONTRASEÑA}")
        if event == sg.WIN_CLOSED:
            EXIT = 1
            break

if EXIT == 0:
    window['-COL3-'].update(visible=True)

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
    password.send_keys(CONTRASEÑA)
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

while True and EXIT == 0:
    event, values = window.read()
    if event == "GO":
            window["Cerrar"].update(disabled=False)
            inscribir()
            time.sleep(.5)
    if event == "Cerrar":
         window.close()
    if event == sg.WIN_CLOSED:
        EXIT = 1
        break




