# El else en un loop siempre se ejectura una vez sin importar si a entrado
# el loop o no

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# No entra al LOOP

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
