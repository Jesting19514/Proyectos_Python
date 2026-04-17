# El else dentro de los ciclo for mantiene el ultimo valor 
for i in range(5):
    print(i)
else:
    print("else:", i)

# El loop no se ejecuta ni una sola vez
# Si la variable de control no se crea antes del loop no existira para la e
# Ejecucion del else
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
