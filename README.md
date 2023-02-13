# Inscripcion-Di-Tella


En el .py tambien estan las instrucciones. 


1. En consola (Si es primera vez):
    pip install Selenium 
    pip install pysimplegui

2. Rellenar las variables USUARIO, CONTRASENA y Materias.
      * Usuario = DNI
      * CONTRASENA = DDMMYYxxx, DDMMYY fecha de nacimiento 1/1/2000 -> 010100; xxx -> ultimos 3 digitos del DNI
      * materias = el link que se consigue desde inscripciones en sigedu. click derecho y copy link
      * Si no necesitas 5 materias, dejar variables extras como estan. ej: ... Materia4 = 'link', Materia5 = ''.
      
3. Correr antes de horario de inscripcion

4. Apretar GO en horario de inscripcion



No esta probado en situacion real. Si no hay cupo, no te va a dejar inscribir aunque uses el codigo. 


El codigo esta escrito para Firefox, si prefieren otro browser hay que cambiar 1 (una) linea. Linea 41:

    driver = webdriver.Firefox()   
    
Por: 
    
    driver = webdriver.Edge()
    driver = webdriver.Safari()
    driver = webdriver.Chrome()
    
 Solo probe con Firefox, no se como funcionan los otros.
 
 #MUY IMPORTANTE:
 
 fijarse si no te dejo inscribirte a alguna materia. La ultima pagina que se abre te deberia mostrar en que materias te pudiste inscribir.
 
