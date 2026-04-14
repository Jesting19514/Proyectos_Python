# El usuario ingresa los valores de los numeros
num1 = int(input("Ingresa el primer numero "))
num2 = int(input("Ingresa el segundo numero "))
num3 = int(input("Ingresa el tercer numero "))

# Comparamos si el primer numero es mayor que el segundo
if num1 > num2 :
    # Dentro de esta misma confirmacion comparamos si ahora tambien es mayor que el tercero
    if num1 > num3:
        print(num1, "Es el numero mas grande")
    # Si no es mayor que el tercero entonces el tercero es el mayor de todos
    else:
        print(num3, "Es el numero mas grande")
elif num2 > num1 :
    if num2 >num3:
        print(num2, "Es el numero mas grande")
    else:
        print(num3, "Es el numero mas grande")

# Python cuenta con una funcion llamada max que nos permite conocer el mayor numero 

numero_mayor = max(num1,num2,num3)

print("El numero mas grande con MAX es: ",numero_mayor)

# De la misma forma ofrece la funcion llamada min para conocer el menor

numero_menor = min(num1,num2,num3)

print("El numero menor con MIN es ",numero_menor)