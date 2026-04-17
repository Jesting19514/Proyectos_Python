'''
Podemos hacer uso de for para realizar ciertas tareas dentro de nuestro codigo
Por ejemplo si quisieramos un loop de 100 con while seria asi 

i = 0
while i < 100:
    # do_something()
    i += 1

El ciclo for nos permite contar de forma mas directa 
'''
# for i in range(10):
#     print("The value of i is currently", i)
# El rango puede tener dos argumentos no solo uno 
for i in range(2, 8): #El primero es el inicial y el ultimo el primer valor que no sera tomado en cuenta
    print("The value of i is currently", i)

# La funcion for en el rango puede aceptar 3 argumentos 
for i in range(2, 8, 3):# El tercer valor es un incremento, un valor agregado a la variable cada ciclo
    print("The value of i is currently", i)

# Si el rango generado en la funcion esta vacio el loop no inicia
for i in range(1, 1):
    print("The value of i is currently", i)
# El valor del segundo valor siempre tiene que ser mayor al primero para ejecutarse
for i in range(2, 1):
    print("The value of i is currently", i)

