#Actividad1
for i in range(101):  # Itera desde 0 hasta 100
    print(i)  # Imprime cada número en una línea

#Actividad2
numero = input("Ingrese un número entero: ")  # Solicita un número al usuario
cantidad_digitos = len(numero)  # Nos da la longitud de la cadena
print(f"El número ingresado tiene",(cantidad_digitos), "dígitos.")  # Imprime el resultado

#Actividad3
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
suma = 0

for i in range(min(num1, num2) + 1, max(num1, num2)):  # Itera entre los números, sin incluir los extremos
    suma += i  # Suma cada número a la variable suma
print(f"La suma de los números entre" ,(num1), "y" ,(num2), "es: ",(suma))

#Actividad4
suma = 0
numero = -1  # Inicializo desde un número distinto de 0, para que el bucle se ejecute por lo menos una vez

while numero != 0:  # El bucle va a seguir mientras el número sea distinto de 0
    numero = int(input("Ingrese un número entero (0 para terminar): "))  # Solicita un número al usuario
    if numero != 0:  # Verifica que el número no sea 0 antes de sumarlo
        suma += numero  # Suma el número a la variable suma
print(f"La suma total es: ",(suma))  # Imprime la suma total por pantalla

#Actividad5
import random
numero_aleatorio = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
intentos = 0
intento_usuario = -1  # Inicializamos con un valor fuera del rango 0-9

while intento_usuario != numero_aleatorio:  # El bucle continúa hasta que el usuario adivine
    intento_usuario = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if intento_usuario != numero_aleatorio:  # Si el usuario no adivina
        print("Intenta nuevamente.")  # Pide intentar de nuevo

print(f"Adivinó el número en:",(intentos) , "intentos.")

#Actividad6
for i in range(100, -1, -2):  # Itera desde 100 hasta 0 y disminuye de a 2
    print(i)  # Imprime los números pares

#Actividad7
num_positivo = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(num_positivo + 1):  # Itera desde 0 hasta el número positivo inclusive
    suma += i  # Suma cada número
print(f"La suma de los números desde 0 hasta",(num_positivo),"es:",(suma))

#Actividad8
cant_num = 10
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cant_num):  # Itera la cantidad de veces de acuerdo a cantidad de números
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(f"Pares:",(pares),"Impares:",(impares),"Positivos:",(positivos),"Negativos:",(negativos))

#Actividad9
cant_num = 3
suma = 0

for i in range(cant_num): #Itera según la cantidad definida
    num = int(input("Ingrese un número entero: "))
    suma += num #La suma inicia de 0 y se suma el número ingresado por el usuario
media = suma / cant_num #Cálculo de la media
print(f"La media de los números ingresados:",(media)) #Imprime la media por pantalla

#Actividad10
numero = input("Ingrese un número: ")
num_invertido = numero[::-1]  # Invierte la cadena de números
print(f"El número invertido es:",(num_invertido))
