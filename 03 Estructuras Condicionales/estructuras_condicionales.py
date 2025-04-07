#Actividad1
edad = int(input("Ingrese su edad: "))  # Solicita la edad al usuario 
if edad >= 18:  # Verifica si la edad es mayor o igual a 18
    print("Es mayor de edad")  # Imprime el mensaje si es mayor de edad

#Actividad2
nota = float(input("Ingrese su nota: "))  # Solicita la nota al usuario
if nota >= 6:  # Verifica si la nota es mayor o igual a 6
    print("Aprobado")  # Imprime "Aprobado" si la nota es mayor o igual a 6
else:  # Si la nota no es mayor o igual a 6
    print("Desaprobado")  # Imprime "Desaprobado"

#Actividad3
numero = int(input("Ingrese un número: "))  # Solicita un número al usuario
if numero % 2 == 0:  # Verifica si el número es par
    print("Ha ingresado un número par")  # Imprime mensaje de número par
else:  # Si el número no es par
    print("Por favor, ingrese un número par")  # Pide ingresar un número par

#Actividad4
edad = int(input("Ingrese su edad: "))  # Solicita la edad al usuario
if edad < 12:  # Verifica si es menor de 12 años
    print("Niño/a")  # Imprime "Niño/a"
elif 12 <= edad < 18:  # Verifica si está entre 12 y 17 años
    print("Adolescente")  # Imprime "Adolescente"
elif 18 <= edad < 30:  # Verifica si está entre 18 y 29 años
    print("Adulto/a joven")  # Imprime "Adulto/a joven"
else:  # Si tiene 30 años o más
    print("Adulto/a")  # Imprime "Adulto/a"

#Actividad5
contrasena = input("Ingrese su contraseña: ")  # Solicita la contraseña

if 8 <= len(contrasena) <= 14:  # Verifica si la longitud está entre 8 y 14 caracteres
    print("Ha ingresado una contraseña correcta")  # Imprime mensaje de contraseña válida
else:  # Si la longitud no es correcta
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")  # Solicita una contraseña válida

#Actividad6
import random  # Importa el módulo random para crear números aleatorios
from statistics import mode, median, mean  # Importa funciones estadísticas

numeros_aleatorios = (random.randint(1, 100) for i in range(50))  # Genera 50 números aleatorios entre 1 y 100
media = mean(numeros_aleatorios)  # Calcula la media
mediana = median(numeros_aleatorios)  # Calcula la mediana
moda = mode(numeros_aleatorios)  # Calcula la moda

if media > mediana > moda:  # Verifica sesgo positivo
    print("Sesgo positivo")
elif media < mediana < moda:  # Verifica sesgo negativo
    print("Sesgo negativo")
else:  # Si no hay sesgo
    print("Sin sesgo")

#Actividad7
palabra = input("Ingrese una frase o palabra: ")  # Solicita una frase al usuario
if palabra[-1].lower() in "aeiou":  # Verifica si el último carácter es una vocal
    print(palabra + "!")  # Agrega un signo de exclamación si termina en vocal
else:  # Si no termina en vocal
    print(palabra)  # Imprime la frase como la ingresó el usuario

#Actividad8
nombre = input("Ingrese su nombre: ")  # Solicita el nombre
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para la inicial en mayúscula: "))  # Solicita la opción según el formato que quiera el usuario
if opcion == 1:  # Si la opción es 1
    print(nombre.upper())  # Imprime el nombre en mayúsculas
elif opcion == 2:  # Si la opción es 2
    print(nombre.lower())  # Imprime el nombre en minúsculas
elif opcion == 3:  # Si la opción es 3
    print(nombre.title())  # Imprime el nombre con la inicial en mayúscula
else:  # Si la opción no es ninguna de las anteriores mencionadas
    print("Opción incorrecta")  # Imprime mensaje de error

#Actividad9
magnitud = float(input("Ingrese la magnitud del terremoto: "))  # Solicita la magnitud
if magnitud < 3:  # Verifica la magnitud
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad10
hemisferio = input("Ingrese el hemisferio (N/S): ") # Solicita el hemisferio
mes = int(input("Ingrese el mes del año en número: "))  # Solicita el mes
dia = int(input("Ingrese el día en número: "))  # Solicita el día
if hemisferio == "N":  # Si el hemisferio es norte
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:  # Verifica las fechas
        print("invierno")  # Imprime la estación correspondiente
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("primavera")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("verano")
    else:
        print("otoño")
elif hemisferio == "S":  # Si el hemisferio es sur
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("verano")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("otoño")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("invierno")
    else:
        print("primavera")
else:  # Si el hemisferio no es válido
    print("Hemisferio inválido")




