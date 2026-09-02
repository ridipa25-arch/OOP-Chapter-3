import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print("Roll No:", student["Roll no"])
        print("Name:", student["Name"])
        print("Address:", student["Address"])
        print()