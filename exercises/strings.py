while True:
    text = str(input("Enter a string: "))
    if text == "":
        print("Invalid input!")
        continue

    x = len(text)

    print(f"\nNumber of leters in string: {x}")

    print("\nEach character typed from first to last:\n")

    while x > 0:
        print(text[-x])
        x = x - 1

    print("\nPrint first three chars from string:")
    print("\t" + text[0:3])

    print("\nPrint last three chars from string:")
    print("\t" + text[-3:])

    print("\nPrint string in reverse")
    print("\t" + text[::-1])

    while True:
        user_contionue = str(input("Do you want do continue (y/N)?"))
        if user_contionue == "y":
            break
        elif user_contionue == "n":
            exit()
        else:
            print("Invalid input!")
            continue
