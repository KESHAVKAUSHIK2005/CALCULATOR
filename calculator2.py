# -*- coding: utf-8 -*-
"""calculator2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qOPfrnMpez6_NLdL2LXbfAz1JweVll57
"""

print("\t\t****Calculator*****")

a=input("Enter 1st number: ")
b=input("Enter 2nd number: ")

op=input("Enter operation to perform: (+,-,*,/,**,%)\n")
if (op=="+") :
    print(float(a)+float(b))
elif (op== "-"):
    print(float(a)-float(b))
elif (op=="*"):
    print(float(a)*float(b))
elif (op=="/"):
    print(float(a)/float(b))
elif (op== "**") :
    print(float(a)** float(b))
elif (op== "%") :
    print( float(a)% float(b))