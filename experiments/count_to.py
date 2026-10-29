while True:
    try:
        numbers = int(input("Enter how much numbers you want: "))
    except ValueError:
        print("Invalid input!")
        continue

    if numbers <= 0:
        print("Enter a number larger than 0.")
        continue

    for i in range(numbers):
        print(i)
        numbers -= 1

    while True:
        user_contionue = str(input("Do you want do continue (y/n)?"))
        if user_contionue == "y":
            break
        elif user_contionue == "n":
            exit()
        else:
            print("Invalid input!")
            continue
