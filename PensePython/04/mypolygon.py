import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def arc(t, r, angle):
    # calcula o comprimento do arco
    comprimento = 2 * math.pi * r * (angle / 360)
    print(comprimento)
    # calcula o número de lados
    n = int(angle / 4 + 1)
    print(n)
    # calcula o comprimento de cada lado
    length = comprimento / n
    print(length)
    # desenha o arco
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

def circle(t, r):
    arc(t, r, 360)

bob = turtle.Turtle()
# square(bob, 300)
# polygon(bob, 7, 100)
# circle(bob, 150)
arc(bob, 150, 90)
turtle.mainloop()
