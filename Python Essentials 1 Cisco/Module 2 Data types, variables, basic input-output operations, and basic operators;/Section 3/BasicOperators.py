# Exponentes
# Representados con 3 asteriscos (***)
# Cuando los dos argumentos son integers el resultado sera un integer tambien
# Cuando al menos uno de los argumentos sea float el resultado sera float
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# Multiplicacion
# Representados con un asterisco (*)
# Sigue las mismas reglas de integers vs float 
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# Division 
# Representados con un slash (/)
# El resultado siempre devuelve un float
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# Division de Integers
# Representado con dos slashes (//)
# Los resultados siempre son redondeados siempre al entero mas cercano
# Sigue las reglas de integers vs float
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# Hay un problema con esto ya que no nos da resultados exactos  por ejemplo
print(6 // 4) # El resultado es 1 ya que son integers
print(6. // 4) # El resultado tambien es uno ya que es redondeado aunque el resultado real deberia ser 1.5

# De la misma manera si usamos numeros negativos esto es aun mas obvio 
print(-6 // 4) # El resultado es -2 ya que el resultado real es -1.5 pero se redondea al entero mas cercano que es -2
print(6. // -4) # El resultado es -2 ya que el resultado real es -1.5 pero se redondea al entero mas cercano que es -2

# Remainder
# Representado con un porcentaje (%)
# Esto nos entrega el resto que queda de la division
print(14 % 4) # 2

'''
14 // 4 gives 3 → Division;
3 * 4 gives 12 → Se multiplica el resultado de la division por el divisor;
14 - 12 gives 2 → Esto es el resto.
'''
print(12 % 4.5)

'''
3.0 – not 3 but 3.0. The rule still works:
12 // 4.5 gives 2.0,
2.0 * 4.5 gives 9.0,
12 - 9.0 gives 3.0.
'''
# Suma
# Representado co un signo de mas (+)
# Sigue la regla de Integer vs Float
print(-4 + 4)
print(-4. + 8)

# Resta
# Representado con un signo de menos (-)
# Este es un operador especial ya que tambien nos sirve para representar numeros negativos
# Sigue la regla de Integer vs Float
print(-4 - 4)
print(4. - 8)
print(-1.1)

# Prioridad de los operadores
# Siguen las reglas de jerarquia de operaciones matematicas
# Si son operaciones con el mismo nivel de jerarquia se realizan de izquierda a derecha
print(9 % 6 % 2)

# Por alguna razon los exponenciales usan una jerarquia diferente a los demas operadores, ya que se realizan de derecha a izquierda
print(2 ** 2 ** 3)

print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

# Tambien podemos usar parentesis para cambiar la jerarquia de las operaciones o para simplificar la lectura del codigo
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
    

# Ejemplos de funcionamiento
print((2 ** 4), (2 * 4.), (2 * 4))
    
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
 