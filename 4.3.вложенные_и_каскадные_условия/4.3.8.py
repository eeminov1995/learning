# Самописный калькулятор
num1 = int(input())
num2 = int(input())
operation = input()
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
elif operation != "+" or operation != "-" or operation != "*" or operation != "/":
    print("Неверная операция")