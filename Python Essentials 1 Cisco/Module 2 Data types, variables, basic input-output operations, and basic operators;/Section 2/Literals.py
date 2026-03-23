# Aunque a simple vista parezcan iguales internamente en la memoria de la computadora estan almacenados de forma diferente
print("2") # String una serie de letras
print(2) # Integer se convierte en una serie de bits que la computadora puede entender y manipular matematicamente

# Tambien podemos hacer uso de numeros hexadecimales y python automaticamente los convertira
print(0o123)

# Si queremos escribir un string que contenga comillas necesitamos hacer uso de una de estas dos tecnicas
print("I like \"Monty Python\"") # Backslash es un caracter de escape que le dice a python que el siguiente caracter es parte del string y no el final del string
print('I like "Monty Python"') # Comilla simple es otra forma de escribir el string, pero es importante que cierre de la misma manera

# Este ejemplo funciona ya que true tiene un valor de 1 y false tiene un valor de 0 (Booleanos)
print(True > False)
print(True < False)

"""
Write a one-line piece of code, using the print() function, 
as well as the newline and escape characters, to match the expected result outputted on three lines.
"I'm"
""learning""
"""
#"""Python"""


print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")