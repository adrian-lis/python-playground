print("Triangle vadidation")


def check(a, b, c):
    return not (a + b <= c or a + c <= b or b + c <= a)


while True:
    print()
    try:
        a = float(input("Enter a side: "))
    except ValueError:
        print("Invalid Input")
        continue
    try:
        b = float(input("Enter b side: "))
    except ValueError:
        print("Invalid Input")
        continue
    try:
        c = float(input("Enter c side: "))
    except ValueError:
        print("Invalid Input")
        continue

    if check(a, b, c):
        print()
        print("# ----- #")
        print("# Valid #")
        print("# ----- #")
    else:
        print()
        print("# ----------- #")
        print("# ! Invalid ! #")
        print("# ----------- #")
