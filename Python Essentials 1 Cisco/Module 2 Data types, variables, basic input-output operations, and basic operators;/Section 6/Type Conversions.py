# No solo se puede convertir un string a valores numericos si no tambien biseversa
# str(number) convierte numeros a string

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))