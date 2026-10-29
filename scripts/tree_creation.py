while True:
    try:
        rows = int(input("Enter amount of rows: "))
    except ValueError:
        print("Invalid input! ")
        continue

    try:
        trunk_size = int(input("Enter how long the 'trunk' shall be: "))
    except ValueError:
        print("Invalid input! ")
        continue

    for i in range(rows):
        stars_count = i * 2 + 1
        spaces_count = rows - 1 - i
        print(" " * spaces_count + "*" * stars_count)

    rows -= 1

    for i in range(trunk_size):
        trunk_size -= 1

        print(" " * rows + "*")

    while True:
        user_contionue = str(input("Do you want do continue (y/N)?"))
        if user_contionue == "y":
            break
        elif user_contionue == "n":
            exit()
        else:
            print("Invalid input!")
            continue
