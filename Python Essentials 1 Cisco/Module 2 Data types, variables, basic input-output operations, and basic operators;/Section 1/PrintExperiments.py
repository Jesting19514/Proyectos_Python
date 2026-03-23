print("Hello, Python!")
# Imprimir nombre
print("Erick")

# Causa un error ya que busca una funcion Erick
# print(Erick)

# Causa un error ya que no encuentra los parentesis
# print"Erick"

# Causa un error porque encuentra mas de una instruccion en la linea
# print("Erick") print("Python")

# Con cada instanciacion de print se aplica un newline
print("The itsy bitsy spider climbed up the waterspout.") 
print("Down came the rain and washed the spider out.")

# Se puede usar un print con un argumento vacio para un newline
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

# Tambien se puede usar un argumento de escape para el newLine
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

# Los backslash son argumentos de escape, hacen que el codigo salga por un momento y busque una instruccion especial
# Esto marca error ya que busca la instruccion especial
# print("\")

# La forma correcta de hacerlo es con doble backslash
print("\\")

# Se puede usar mas de un argumento en la funcion separandolos con coma
# Print agrega un espacio entre cada argumento separado por coma automaticamente
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

# Existen argumentos keyword que se pueden usar para modificar el comportamiento de la funcion print
# La funcion print tiene dos argumentos keyword, end y sep
# Por default end es un newline es decir end = "\n" por eso al final de cada print se hace un espaciado
# Pero si modificamos su comportamiento podemos ver que esto ya no se realiza en cambio se agrega lo que nosotros hayamos puesto como keyword
print("My name is", "Python.", end=" ")
print("Monty Python.")

# De la misma forma el keyword sep por default es un espacio es decir sep=" "
# Pero podemos podificar su comportamiento y agregar lo que nosotros queramos como separador de cada argumento de la funcion
print("My", "name", "is", "Monty", "Python.", sep="-")

# Los keywords puedens ser utilizados en un mismo print y sin afectar el siguiente 
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#Los kewords deben ser despues de cualquier argumento posicional, es decir despues de cualquier argumento que no sea un keyword
#print(sep="&", "fish", "chips")

