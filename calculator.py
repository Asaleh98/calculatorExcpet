def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try :
        total = num1/ num2
    except ZeroDivisionError
        print("cant divide by 0")
        return None
    return total


i = 0
while i < 5
    numb1 = input(int("please enter value"))
    numb2 = input(int("please enter value"))

print(add(numb1, numb2))
print(add(numb1, numb2))
print(add(numb1, numb2))
print(add(numb1, numb2))
