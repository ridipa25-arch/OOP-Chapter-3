items = ["apple", "banana", "mango", "orange", "grapes"]

try:
    index = int(input("Enter an index (0-4): "))
    print("Item:", items[index])

except IndexError:
    print("Error: Index is out of range.")