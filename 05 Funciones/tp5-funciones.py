#Actividad1
def imprimir_hola_mundo(): #Defino la función imprimir_hola_mundo
    print("Hola Mundo!")
#Programa principal
imprimir_hola_mundo()

#Actividad2
def saludar_usuario(nombre): #Defino la función saludar_usuario
    return (f"Hola {nombre}!")
#Programa principal
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#Actividad3
def informacion_personal(nombre, apellido, edad, residencia): #Defino la función informacin_personal
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Actividad4
import math
def calcular_area_circulo(radio): #Defino la función calcular_area_circulo
    return math.pi * radio**2

def calcular_perimetro_circulo(radio): #Defino la función calcular_perimetro_circulo
    return 2 * math.pi * radio
#Programa principal
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}") # Lo trunco en 2 decimales
print(f"El perímetro del círculo es: {perimetro:.2f}") # Lo trunco en 2 decimales

#Actividad5
def segundos_a_horas(segundos): #Defino la función segundos_a_horas
    horas = segundos / 3600
    return horas
#Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas") # Lo trunco en 2 decimales

#Actividad6
def tabla_multiplicar(numero): #Defino la función tabla_multiplicar
    print(f"Tabla de multiplicar del {numero}:")
#Programa principal
    for i in range(1, 11): #Establezco el rango con un For
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero) #Llamo a la función tabla_multiplicar

#Actividad7
def operaciones_basicas(a, b): #Defino la función operaciones_basica
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

#Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(num1, num2)
print(f"Resultados de las operaciones entre {num1} y {num2}:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]:.2f}") #Trunco la división en 2 decimales

#Actividad8
def calcular_imc(peso, altura): #Defino la función calcular_imc
    imc = peso / altura**2
    return imc

#Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros (Utilice un punto para separar la parte decimal): "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}") #Trunco en 2 decimales

#Actividad9
def celsius_a_fahrenheit(celsius): #Defino la función celsius_a_fahrenheit
    fahrenheit = (9/5) * celsius + 32 #Fórmula Celsius a Fahrenheit
    return fahrenheit

#Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit") #Trunco en 2 decimales

#Actividad10
def calcular_promedio(a, b, c): #Defino la función calcular_promedio
    promedio = (a + b + c) / 3
    return promedio

#Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio:.2f}") #Trunco en 2 decimales
