import pygame
A = int(input("O valor de A: "))    #para converter em inteiro, pois o input recebe como string#
B = int(input("O valor de B: "))

if A > B:
    print("A é maior que B")
    print("Hello world")
elif B > A:
    print("B é maior que A")
else:
    print("A é igual a B")