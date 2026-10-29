def empty_function():
    pass


def is_even(n):
    if n % 2 == 0:
        return True  # return stops further execution of the function, similar to break
    return False


print(is_even(10))  # True
print(is_even(7))  # False


def add(num1, num2):
    return num1 + num2


print(add(10, 10))


def greet(name):
    name = name.capitalize()
    return f"Hello! {name}"


print(greet(str(input("Enter name: "))))
