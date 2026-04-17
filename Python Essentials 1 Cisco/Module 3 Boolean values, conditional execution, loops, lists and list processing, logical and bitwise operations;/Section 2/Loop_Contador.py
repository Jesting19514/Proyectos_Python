# Podemos hacer uso de variables para ejecutar un loop la cantidad de veces que necesitemos
# Decrementando el valor de esta variable y siendo esta misma la condicion de salida
counter = 5 # Cantidad de veces que se ejecutara
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# Aunque este ejemplo es mas corto se mas dificil de entender leyendo por lo que 
# No es recomendable hacer uso de esta 
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)