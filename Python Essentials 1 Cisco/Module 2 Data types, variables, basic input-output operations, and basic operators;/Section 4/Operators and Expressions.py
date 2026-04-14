"""
Your task is to complete the code in order to evaluate the following expression:

3x3 - 2x2 + 3x - 1

The result should be assigned to y.

"""
# x = 0     y = -1.0
x =  0
x = float(x)
cube = x ** 3
double = x ** 2
y = ((3 * cube)-(2*double)+(3*x)-1)
print("y =", y)

# x = 1     y = 3.0
x =  1
x = float(x)
cube = x ** 3
double = x ** 2
y = ((3 * cube)-(2*double)+(3*x)-1)
print("y =", y)

# x = -1     y = -9.0
x =  -1
x = float(x)
cube = x ** 3
double = x ** 2
y = ((3 * cube)-(2*double)+(3*x)-1)
print("y =", y)
