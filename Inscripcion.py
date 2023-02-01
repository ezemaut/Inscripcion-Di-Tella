
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
# no se si es necesario

# Prueben que esten bien el usario y contra antes del horario de inscripcion.


#############################################################################


# CODIGO


##################################################################################



from selenium import webdriver     
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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

# Inscribe en materias
for link in ls:
    if link != '':
        driver.get(link)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

# Abre pagina que dice donde SI estas inscripto
driver.get('https://sigedu.utdt.edu/utdt/alumnos/ver_inscripcion.jsp')


