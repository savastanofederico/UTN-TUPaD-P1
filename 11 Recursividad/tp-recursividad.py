#Ejercicio 1
import math
def factorial_recursivo(n):
    
    if n == 0 or n == 1: #Caso base
        return 1
    else: #Instancia recursiva
        return n * factorial_recursivo(n - 1)

#Algoritmo genérico
try:
    numero_limite_factorial = int(input("Ingrese un número entero positivo para calcular factoriales: "))
    if numero_limite_factorial < 0:
        print("Por favor, ingrese un número no negativo.")
    else:
        for i in range(1, numero_limite_factorial + 1):
            print(f"El factorial de {i} es: {factorial_recursivo(i)}")
except ValueError:
    print("Ingreso inválido. Por favor, ingrese un número entero.")

#Ejercicio 2
def fibonacci_recursivo(pos):
    
    if pos <= 0: #Casos base
        return 0
    elif pos == 1:
        return 1
    else:  # Instancia recursiva
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

#Algoritmo genérico
try:
    posicion_limite_fib = int(input("Ingrese la posición límite para la serie de Fibonacci: "))
    if posicion_limite_fib < 0:
        print("Por favor, ingrese una posición no negativa.")
    else:
        print(f"Serie de Fibonacci hasta la posición {posicion_limite_fib}:")
        for i in range(posicion_limite_fib + 1):
            print(f"F({i}) = {fibonacci_recursivo(i)}")
except ValueError:
    print("Ingreso inválido. Por favor, ingrese un número entero.")

#Ejercicio 3

def potencia_recursiva(base, exponente):
    if exponente == 0: #Caso base 1
        return 1
    elif exponente == 1: #Caso base 2
        return base
    elif exponente > 1: #Instancia recursiva
        return base * potencia_recursiva(base, exponente - 1)

#Algoritmo genérico
try:
    base = float(input("Ingrese un número para la base: "))
    exponente = int(input("Ingrese un número entero para el exponente: "))
    resultado_potencia = potencia_recursiva(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado_potencia}")
except ValueError:
    print("Entrada inválida. Por favor, ingrese números válidos.")

#Ejercicio 4
def decimal_a_binario_recursivo(decimal):
    if decimal == 0: #Casos base
        return "0"
    elif decimal == 1: 
        return "1"
    else: #Instancia recursiva
        resto = decimal % 2
        cociente = decimal // 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

# Algoritmo genérico
try:
    num_decimal = int(input("Ingrese un número entero positivo en base decimal para convertir a binario: "))
    if num_decimal < 0:
        print("Por favor, ingrese un número entero positivo.")
    elif num_decimal == 0: # Caso especial para el 0 si la función no lo maneja directamente al inicio de la recursión.
        print(f"El número {num_decimal} en binario es: 0")
    else:
        binario_resultante = decimal_a_binario_recursivo(num_decimal)
        print(f"El número {num_decimal} en binario es: {binario_resultante}")
except ValueError:
    print("Ingreso inválido. Por favor, ingrese un número entero")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1: #Caso base
        return True
    else: #Instancia recursiva
        if palabra[0] == palabra[-1]: #Llamada recursiva a la función
            return es_palindromo(palabra[1:-1])
        else:
            return False

# Algoritmo genérico
palabra_ingresada = input("Ingrese una palabra para verificar si es un palíndromo: ").lower() #Convierto a minúsculas la entrada del usuario
if es_palindromo(palabra_ingresada):
    print(f"'{palabra_ingresada}' Es un palíndromo.")
else:
    print(f"'{palabra_ingresada}' No es un palíndromo.")

#Ejercicio 6
def suma_digitos(n):
    if n < 10: #Caso base
        return n
    else: #Instancia recursiva
        return (n % 10) + suma_digitos(n // 10)

# Algoritmo genérico
try:
    num_a_sumar = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
    if num_a_sumar < 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        resultado_suma_digitos = suma_digitos(num_a_sumar)
        print(f"La suma de los dígitos de {num_a_sumar} es: {resultado_suma_digitos}")
except ValueError:
    print("Ingreso inválido. Por favor, ingrese un número entero.")

#Ejercicio 7
def contar_bloques(n):
    if n <= 0: #Caso base
        return 0
    elif n == 1:
        return 1
    else: #Instancia recursiva
        return n + contar_bloques(n - 1)

#Algoritmo genérico
try:
    num_bloques_base = int(input("Ingrese el número de bloques para el nivel más bajo de la pirámide: "))
    if num_bloques_base < 0:
        print("Por favor, ingrese un número no negativo de bloques.")
    else:
        total_bloques = contar_bloques(num_bloques_base)
        print(f"Para una pirámide con {num_bloques_base} bloques en la base, se necesitan {total_bloques} bloques en total")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero")

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0: #Caso base
        return 0
    else: #Instancia recursiva
        ultimo_digito = numero % 10 #Obtiene el último dígito del número

        conteo = 1 if ultimo_digito == digito else 0 #Comprueba si el último dígito es el que estamos buscando
        
        return conteo + contar_digito(numero // 10, digito)

# Algoritmo genérico
print("--- Ejercicio 8: Contar Dígito ---")
try:
    num_principal = int(input("Ingrese el número entero positivo (ej. 12233421): "))
    digito_buscar = int(input("Ingrese el dígito a buscar (entre 0 y 9): "))

    if not (0 <= digito_buscar <= 9):
        print("El dígito a buscar debe estar entre 0 y 9.")
    elif num_principal < 0:
        print("El número principal debe ser entero positivo.")
    elif num_principal == 0 and digito_buscar == 0: # Caso especial: contar 0s en el número 0
        print(f"El dígito {digito_buscar} aparece 1 vez en el número {num_principal}.")
    else:
        resultado_conteo = contar_digito(num_principal, digito_buscar)
        print(f"El dígito {digito_buscar} aparece {resultado_conteo} veces en el número {num_principal}")
except ValueError:
    print("Ingreso inválido. Por favor, ingrese números enteros")




