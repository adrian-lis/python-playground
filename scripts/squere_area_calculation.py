print("This is a squere area calculation")

while True:
    print()
    try:
        a = float(input("Enter squere side: "))
    except ValueError:
        print("Invalid Input")

    sum = a * a
    print(f"Squere area is: {sum}")