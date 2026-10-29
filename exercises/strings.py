text = str(input("Enter a string: "))

x = len(text)

print()
print(f"Number of leters in string: {x}")
print()

print("Each character typed from first to last:")
print()

while x > 0:
    print(text[-x])
    x = x - 1
