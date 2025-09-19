import matplotlib.pyplot as plt
import eulers
import rk4
import numpy as np

def fnc(x,y):
    return np.sin(x+y)

a = 0
b = 1
x0 = 2
h = .1
y = eulers.feuler(fnc,x0,a,b,h)
print(y)

y2 = eulers.beuler(fnc,x0,a,b,h)
print("Backwards Euler Soln:\n")
print(y2)

# rk4 solution
y3 = rk4.solver(fnc,x0=x0,a=a,b=b,h=h)
print("Runge-Kutta 4 Solution: \n")
print(y3) 