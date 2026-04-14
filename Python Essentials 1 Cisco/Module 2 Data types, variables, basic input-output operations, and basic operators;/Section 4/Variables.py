# No se necesita declarar una variable antes de usarla, en el momento en el que se le asigna un valor esta es creada con la siguiente sintaxis
# nombre_variable = valor
var = 1
print(var)

# Puedes usar la cantidad que quieras de variables que necesites para lograr tu cometido 
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

# No puedes usar una variable que a la que no le ha sido asignado ningun valor

# print(var2) # Esto es un error ya que var2 no tiene ningun valor asignado

# Puedes combinar texto y variables haciendo uso del operador de suma + por ejemplo
var = "3.8.5"
print("Python version: " + var)

# Para actualizar el valor de una variable existente solo debes usar el operador de igualdad =
var = "3.8.6"
print("Python version: " + var)

var = 1
print(var)
var = var + 1
print(var)

# Si queremos sacar el cuadrado de una variable o hacer algun contador python nos ofrece atajos que acen mas facil el codigo
x = x * 2 # Es lo mismo
x *= 2

sheep = sheep + 1 # Es lo mismo
sheep += 1

# Se usa de esta forma cuando se tiene algo como variable = variable operador expression 
# Se convierte en variable operador= expresion, estos son algunos ejemplos 
i = i + 2 * j 
i += 2 * j

var = var / 2 
var/= 2

rem= rem % 10
rem %= 10

j = j -( i + var + rem )
j -= (i + var + rem)

x = x ** 2 
x **= 2 

