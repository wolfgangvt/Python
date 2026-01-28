#This file is used just for me to learn math and modulo operands as reference for other project
#I haven't coded in a while sorry chat :)

def add(x, y):
     #Addition of two numbers

     return x + y

def subtract(x, y):
     #Subtraction of two numbers

     return x - y

def mult(x, y):
     #Multiplication of two numbers

     return x * y

def divide(x, y):
     #Division of two numbers

     return x / y

def modulus(x, y):
     #Modulus of two numbers

     return x % y

def expo(x, y):
     #Exponentiation of two numbers

     return x ** y

def floordiv(x, y):
     #Floor division of two numbers

     return x // y


print("Select operation you wish to calculate:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponent")
print("7. Floor Divide")

choice = input("Enter choide (1,2,3,4,5,6,7): ")

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

if choice == '1':
     print(num1, "+" ,num2, "=", add(num1, num2))

elif choice == '2':
     print(num1, "-" ,num2, "=", subtract(num1, num2))

elif choice == '3':
     print(num1, "*" ,num2, "=", mult(num1, num2))

elif choice == '4':
     print(num1, "/" ,num2, "=", divide(num1, num2))

elif choice == '5':
     print(num1, "%" ,num2, "=", modulus(num1, num2))

elif choice == '6':
     print(num1, "**" ,num2, "=", expo(num1, num2))

elif choice == '7':
     print(num1, "//" ,num2, "=", floordiv(num1, num2))

else:
     print("Error, please try again")