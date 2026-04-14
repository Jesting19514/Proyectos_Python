# La funcion input() es capaz de leer datos ingresados por el usuario y 
# regresar los que mismos datos al programa en ejecucion
print("Tell me anything...")
# Input se usa normalmente sin argumentos y cambiara la consola al modo de escritura y los datos seran enviados al programa
# Se tiene que asignar el input a una variable de otra forma los datos seran perdidos
anything = input()
print("Hmm...", anything, "... Really?")


# La funcion input con un argumento
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# El resultado del input es un string
# Aqui marcara un error ya que esta tratando de realizar operaciones con un string
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Type Casting (Conversion de tipos)
# Asignamos el tipo de valor que queremos que se convierta el input
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Aunque util tiene algunos errores si se intenta ingresar numeros negativos aunque es un error no los ignora
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)