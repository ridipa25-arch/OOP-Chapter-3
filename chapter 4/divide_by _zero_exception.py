try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")