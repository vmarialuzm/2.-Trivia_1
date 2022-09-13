#Vamos a crear constantes (como variables pero no cambian su valor) en python,nombre en mayúsculas para no tener que escribir el código del color.
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Vamos a "importar" una librería de python, para usar funciones avanzadas
import random #importamos la librería random
import time

#va a aparecer el número de veces que juguemos la trivia
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
jugador_turnos = []

#Mensaje de bienvenida
print(RED+"*** Bienvenidos a mi primera trivia ***\n")
time.sleep(1)
print("Pondremos a prueba tus Conocimientos"+RESET)
time.sleep(1)

#Preguntemos el nombre al usuario
nombre=input("Ingresa tu nombre: ")
edad=input("Ingresa tu edad: ")
if edad.isnumeric():
  print("Sí, es un número")
else:
  print("No es un número")
time.sleep(1)
#Instrucciones
print(BLUE+"Hola", nombre,"debes escribir la letra de la alternativa correcta y dar enter, por cada pregunta correcta se te asignará un número aleatorio del 5 al 10 y por cada incorrecta se te restará un número aleatorio del 1 al 5"+RESET)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"
time.sleep(1)
#va a aparecer el número de veces que juguemos la trivia
while iniciar_trivia==True:
  #para contar las respuestas correctas e incorrectas   creamos las siguientes variables
  correcta=0
  incorrecta=0
  #Para implementar puntajes, crearemos una nueva variable   llamada "puntaje", la que inicpherializamos en 0.
  puntaje=random.randint(0,10) #Número aleatorio de 0 a 10.
  
  time.sleep(1)
  intentos+=1
  print("\nIntento número: ",intentos)
  input("Presione enter para continuar")
  print(GREEN+"Comenzarás con:",puntaje,"puntos"+RESET)
  
  #Creamos un ciclo para mostrar una carga inicial de 5 segundos
  for numero_carga in range(5,0,-1):
    print(numero_carga)
    time.sleep(1)
  #Pregunta 1
  print(RED+"\n1) ¿En qué año llegó el primer hombre a la luna?"+RESET)
  listaa=[MAGENTA+"a) 1958","b) 1970","c) 1969","d) 1958"+RESET]
  for element in listaa:
    print(element)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  #vamos a aplicar un ciclo de validación
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  #Utilizamos la condicional para decidir si tu respuesta es correcta o incorrecta
  if respuesta_1=="c":
    puntaje+=random.randint(5,10)
    correcta+=1
    print("Muy bien",nombre,"!")
  else:
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto",nombre,"!")
  time.sleep(1)
  print(GREEN+nombre,"llevas",puntaje,"puntos."+RESET)
  time.sleep(2)
  #Pregunta 2
  print(RED+"\n2) ¿Cada cuántos años hay un año bisiesto?"+RESET)
  listab=[MAGENTA+"a) 1","b) 4","c) 3","d) 5"+RESET]
  for element in listab:
    print(element)
  
  respuesta_2=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_2 not in ("a","b","c","d","x"):
    respuesta_2=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_2=="x":
    puntaje+=random.randint(1,5)
    incorrecta+=1
    print("Este es un mensaje secreto")
  elif respuesta_2=="a":
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto!", nombre, "son más años")
  elif respuesta_2=="b":
    puntaje+=random.randint(5,10)
    correcta+=1
    print("Muy bien", nombre,"!")
  elif respuesta_2=="c":
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto!", nombre, "son más años")
  else:
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto!", nombre, "son menos años")
  time.sleep(1)
  print(GREEN+nombre,"llevas",puntaje,"puntos."+RESET)  
  time.sleep(2)  
  #Pregunta 3
  print(RED+"\n3) ¿Quién fundó la empresa spacex en el año 2002?"+RESET)
  listac=[MAGENTA+"a) Jeff Bezos","b) Bill Gates","c) Larry Page","d) Elon Musk"+RESET]
  for element in listac:
    print(element)
  
  respuesta_3=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_3=="d":
    puntaje+=random.randint(5,10)
    correcta+=1
    print("Muy bien",nombre,"!")
  else:
    puntaje-=random.randint(1,5)
    incorrecta+=1
    print("Incorrecto",nombre,"!")
  time.sleep(1)
  print(GREEN+nombre,"llevas",puntaje,"puntos."+RESET)  
  time.sleep(2)
  #Pregunta 4
  print(BLUE+"\nEn esta última pregunta", nombre,"si respondes de manera correcta podrás hasta duplicar tu puntaje...")
  input("Presione enter para continuar"+RESET)
  print(RED+"\n4) ¿Cuál es la estrella más brillante del cielo?"+RESET)
  listad=[MAGENTA+"a) Sirio","b) Sol","c) Halley","d) Venus"+RESET]
  for element in listad:
    print(element)
  
  respuesta_4=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_4 not in ("a","b","c","d","x"):
    respuesta_4=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_4=="a":
    print("Correcto!...")
    puntaje=puntaje*2
    correcta+=1
  elif respuesta_4=="b":
    print("...")
    puntaje=puntaje+5  
    incorrecta+=1
  elif respuesta_4=="c":
    print("Incorrecto!")
    puntaje=puntaje-5
    incorrecta+=1
  else:
    print("Totalmente incorrecto!")
    puntaje=puntaje/2
    incorrecta+=1
  time.sleep(1)
  print(GREEN+nombre,"llevas",puntaje,"puntos."+RESET)  
  time.sleep(2)
  
  #Ruleta de puntaje final
  print(BLUE+"\nJugaremos la ruleta de puntaje final")
  numero_carga2=int(input("\n¿Cuántas veces quieres girar la ruleta? \n"+RESET))
  for ruleta in range(1,numero_carga2+1):
    e=random.randint(1,10)
    if ruleta==numero_carga2:
      print(RED+"Intento final, resultado: "+RESET,e)
      puntaje+=e
      time.sleep(1)
    else:
      print("Intento N°",ruleta,", resultado: ",e)
      time.sleep(1)
  time.sleep(1) 
    
  #Agregamos un mensaje al final de nuestra trivia donde mostraremos el puntaje total obtenido.
  print("\nCantidad de respuestas correctas: ",correcta)
  time.sleep(1)
  print("Cantidad de respuestas incorrectas: ",incorrecta)
  time.sleep(1)
  
  print(GREEN+"\nGracias",nombre,"por jugar mi trivia, alcanzaste",puntaje,"puntos."+RESET)
  
  jugador_turnos.append(puntaje)

  #si deseamos seguir jugando aquí se decide
  print(MAGENTA+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print(YELLOW+"\nSecuencia de puntaje por cada turno: ",jugador_turnos)
   print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
