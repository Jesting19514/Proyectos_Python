# El + cuando es usado en dos strings se convierte en un operador de concatenacion
# string + string
# Simplemente concatena (pega) dos strings en una sola, puede usarse mas de una vez en una expresion
# Para que funcione como concatenador es necesario que ambos valores sean string

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# El * usado en un string y un numero se convierte en un replicador 
# string * number
# number * string
# Esto duplica el string el mismo numero de veces que el numero
'''
"James" * 3 gives "JamesJamesJames"
3 * "an" gives "ananan"
5 * "2" (or "2" * 5) gives "22222" (not 10!)
'''
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")