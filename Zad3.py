#-*- coding: utf-8 -*-
from math import sqrt
def kwadratowa(a,b,c,x):
    return a*x**2+b*x+c

    
def miejsca_zerowe(a,b,c):
    delta=b**2-4*a*c
    if delta > 0:
        x1=(-b-sqrt(delta))/2*a
        x2=(-b+sqrt(delta))/2*a
        return x1, x2
    elif delta == 0:
        x3 = -b/2*a
        return x3
    elif delta<0:
        return "Brak miejsc zerowych"

a=-2
b=7
c=8

for x in xrange(-10,10):
    print kwadratowa(a,b,c,x)

print"Dla  parametr�w Zad1=%3.2f, Zad2=%3.2f, c=%3.2f miejsca zerowe funkcji kwadratowej wynosz�:" %(a,b,c) +str(miejsca_zerowe(a, b, c))