def add_Num(num1, num2):
    return num1 + num2

def div_Num(num1, num2):
    return num1 / num2

def avg_Num(num1, num2):
    return (num1+num2)/2

def sub_Num(num1, num2):
    return num1 - num2

def mul_Num(num1, num2):
    return num1 * num2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

opr = input("Enter the operation [%(avg), +(add), -(subtract), *(multiply), /(divide)): ")

if opr  == '%':
    result = avg_Num(num1, num2)
elif opr == '+':
    result = add_Num(num1, num2)
elif opr == '-':
    result = sub_Num(num1, num2)
elif opr == '*':
    result = mul_Num(num1, num2)
elif opr == '/':
    result = div_Num(num1, num2)
else:
    result = "Invalid operation"

print("The result is:", result)

