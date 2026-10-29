def getNumbers_User():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return(num1, num2)

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def devide(num1, num2):
    if num2 == 0:
        return("Error. You can not devide by zero")
    else:
        return num1 / num2

def getOperation_User(num1, num2):
    while True:
        print()
        print("-------------------------------")
        print("Select 1 for addiction      (+)")
        print("Select 2 for substraction   (-)")
        print("Select 3 for multiplication (*)")
        print("Select 4 for devision       (/)")
        print("-------------------------------")
        print()

        selectedOperation = int(input("Select one operation (1-4): "))

        if selectedOperation == 1:
            return add(num1, num2)
        elif selectedOperation == 2:
            return substract(num1, num2)
        elif selectedOperation == 3:
            return multiply(num1, num2)
        elif selectedOperation == 4:
            return devide(num1, num2)
        else:
            print("Invalid operation!")
            continue


def Anwser(result):
    print(f"Result: {result}")

while True:
    num1, num2 = getNumbers_User()
    result = getOperation_User(num1, num2)
    Anwser(result)
