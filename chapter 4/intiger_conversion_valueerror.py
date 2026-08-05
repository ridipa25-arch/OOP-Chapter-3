try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Error: Please enter a valid integer, not letters.")