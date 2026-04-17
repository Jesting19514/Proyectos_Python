'''
Your task is to write a program which reads the number of blocks the builders
 have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – 
if the builders don't have a sufficient number of blocks and cannot complete 
the next layer, they finish their work immediately.
'''

blocks = int(input("Enter the number of blocks: "))

height = 0 # Altura se inicializa en 0
level = 1 # El nivel inicial necesita minimo 1 bloque (Num bloques)

while blocks >= level: # El numero de bloques es mayor que el nivel actual
    blocks -= level # Restas los bloques utilizados para formar el nivel 
    height += 1 # Altura aumenta 1
    level += 1 # Nivel aumenta 1

print("The height of the pyramid:", height)