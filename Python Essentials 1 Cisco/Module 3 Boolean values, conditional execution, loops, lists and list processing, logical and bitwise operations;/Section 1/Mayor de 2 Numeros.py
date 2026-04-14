# Solicitamos al usuario dos numeros
num1 = int(input("Dame el valor del primer numero: "))
num2 = int(input("Dame el valor del segundo numero: "))

if num1 > num2:
    print(num1, "Es el numero mas grande")
else:
    print(num2, "Es el numero mas grande")

# Python permite que si solo es una condicional se pueda escribir de la siguiente manera
if num1 > num2: print(num1, "Es el numero mas grande")
else: print(num2, "Es el numero mas grande")
