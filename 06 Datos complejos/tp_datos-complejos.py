#Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200 #Agrego nuevas frutas y sus precios
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Actividad 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330 #Actualizo precios
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Actividad 3
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

lista_frutas = list(precios_frutas.keys()) #Creo una lista solo con los nombres de las frutas

print(lista_frutas)

#Actividad 4
contactos = {} #Inicializo contactos como un diccionario vacío
print("Por favor, introduzca 5 contactos:") #Pido que cargue los contactos
for i in range(5):
    nombre = input(f"Introduzca el nombre del contacto {i+1}: ")
    numero = input(f"Introduzca el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

print("Contactos guardados:", contactos)

nombre_consulta = input("Introduzca el nombre del contacto que quiera consultar: ") #Para consultar un número
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"El contacto '{nombre_consulta}' no se encuentra en la agenda.")

#Actividad 5
frase = input("Introduzca una frase: ")

palabras = frase.lower().split() #Convierto la frase a minúsculas y dividirla en palabras

palabras_unicas = set(palabras) #Palabras únicas usando un set
print("Palabras únicas:", palabras_unicas)

recuento_palabras = {} #Diccionario con la cantidad de veces que aparece cada palabra
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
print("Recuento:", recuento_palabras)

#Actividad 6
alumnos = {}

print("Introduzca los nombres de 3 alumnos y sus 3 notas:") #Pido ingresar 3 alumnos y sus notas
for i in range(3):
    nombre_alumno = input(f"Introduzca el nombre del alumno {i+1}: ")
    notas_str = input(f"Introduzca las 3 notas de {nombre_alumno} separadas por comas: ")
    notas = tuple(map(int, notas_str.split(',')))
    alumnos[nombre_alumno] = notas

print("\nPromedios de los alumnos:") #Muestro el promedio de cada alumno
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")

#Actividad 7
arcial1_aprobados = {"Ana", "Juan", "Pedro", "Sofía", "Federico"}
parcial2_aprobados = {"Juan", "María", "Sofía", "Carlos", "Federico"}

ambos_parciales = parcial1_aprobados.intersection(parcial2_aprobados) #Estudiantes que aprobaron ambos parciales (intersección)
print("Aprobaron ambos parciales:", ambos_parciales)

solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados) #Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
print("Aprobaron solo uno de los dos parciales:", solo_uno)

todos_aprobados = parcial1_aprobados.union(parcial2_aprobados) #Lista total de estudiantes que aprobaron al menos un parcial (unión)
print("Lista total de estudiantes que aprobaron al menos un parcial:", todos_aprobados)

#Actividad 8
stock_productos = {}

while True:
    print("- Gestión de Stock -")
    print("1. Consultar stock")
    print("2. Agregar unidades / Nuevo producto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        producto_consulta = input("Introduzca el nombre del producto a consultar: ")
        if producto_consulta in stock_productos:
            print(f"El stock de {producto_consulta} es: {stock_productos[producto_consulta]}")
        else:
            print("El producto no existe en el stock.")
    elif opcion == '2':
        producto_modificar = input("Introduzca el nombre del producto: ")
        cantidad = int(input("Introduzca la cantidad de unidades a agregar: "))
        if producto_modificar in stock_productos:
            stock_productos[producto_modificar] += cantidad
            print(f"Se agregaron {cantidad} unidades a {producto_modificar}. Stock actual: {stock_productos[producto_modificar]}")
        else:
            stock_productos[producto_modificar] = cantidad
            print(f"Se agregó el nuevo producto '{producto_modificar}' con un stock inicial de {cantidad}.")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

#Activiadad 9 
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "14:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Cita con el médico",
    ("jueves", "20:30"): "Entrenamiento"
}

dia_consulta = input("Introduzca el día: ").lower()
hora_consulta = input("Introduzca la hora (ej: 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)

if clave_consulta in agenda:
    print(f"En {dia_consulta} a las {hora_consulta} tiene: {agenda[clave_consulta]}")
else:
    print("No hay actividad programada para esa hora y día.")

#Actividad 10 
paises_capitales_europa = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Portugal": "Lisboa",
    "Grecia": "Atenas",
    "Países Bajos": "Ámsterdam"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales_europa.items()}
print(capitales_paises)

