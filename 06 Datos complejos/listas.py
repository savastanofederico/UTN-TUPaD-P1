#Actividad1
multiplos_de_4 = list(range(4, 101, 4))  # Creamos una lista con múltiplos de 4 usando range
print("Lista de múltiplos de 4:", multiplos_de_4)  # Imprime la lista

#Actividad2
elementos_favoritos = ["cine", "comida", "música", "viajar", "vacaciones"]  # Creo una lista con 5 elementos
penultimo = elementos_favoritos[-2]  # Accedo al penúltimo elemento usando indexación negativa
print("Lista:", elementos_favoritos)  # Imprimo lista
print("Penúltimo elemento:", penultimo)  # Imprimo el penúltimo elemento

#Actividad3
lista_vacia = []  # Creo una lista vacía
lista_vacia.append("papa")  
lista_vacia.append("cebolla")  
lista_vacia.append("banana")  
print("Lista con append:", lista_vacia)  # Imprimo la lista

#Actividad4
animales = ["perro", "gato", "conejo", "pez"] # Creo la lista animales
animales[1] = "loro" # Reemplazo el segundo valor con "loro"
animales[-1] = "oso" # Reemplazo el último valor con "oso" 
print("Lista animales modificada:", animales) 

#Actividad5
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)
# Explicación: este programa toma la lista "numeros" y encuentra el valor máximo de la lista usando la función max(), después elimina ese valor máximo e imprime la lista actualizada

#Actividad6
numeros_dea5 = list(range(10, 31, 5)) # Creo la lista con saltos de 5 usando range
print("Lista con saltos de a 5:", numeros_dea5)  
print("Primeros dos números:", numeros_dea5[:2]) # Imprimo los primeros dos elementos usando slicing

#Actividad7
autos = ["sedan", "polo", "suran", "gol"] # Creo la lista autos
autos[1:3] = ["4x4", "tractor"] # Reemplazo los valores en los índices 1 y 2
print("Lista autos modificada:", autos) # Imprimo la lista

#Actividad8
dobles = [] # Creo la lista vacía dobles
dobles.append(5 * 2) # Agrego el doble de 5
dobles.append(10 * 2) 
dobles.append(15 * 2) 
print("Lista de dobles:", dobles) # Imprimo la lista dobles

#Actividad9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]  # Creo la lista compras
compras[2].append("jugo")  # Agrego jugo a la lista del tercer cliente
compras[1][1] = "tallarines"  # Reemplazo fideos por tallarines
compras[0].remove("pan")  # Elimino pan de la lista del primer cliente
print("Lista compras modificada:", compras)  # Imprimo la lista

#Actividad10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False] # Creo la lista anidada
print("Lista anidada:", lista_anidada) # Imprimo la lista anidada
