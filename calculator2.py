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
