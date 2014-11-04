#-*- coding: utf-8 -*-
a="Ala ma kota"
b="abcd dcba"
def palindrom(b):
    b=b.replace(" ","")
    b1=b[::-1]
    if b==b1:
        print "Prawda"
    else:
        print "Fa�sz"

palindrom(b)