def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return 'Error, division by zero'

print('simple calculator')
a=int(input("enter first number: "))
b=int(input('enter second number: '))
print("Addition:",add(a,b))
print("subtraction:",subtract(a,b))
print("multiplication:",multiply(a,b))
print("Division:",divide(a,b))
