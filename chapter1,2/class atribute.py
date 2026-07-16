class School:
    school_name = "Nilkantha School"   

    def __init__(self, student_name, grade):
        self.student_name = student_name
        self.grade = grade

s1 = School("Deepa", "10")
s2 = School("Binita", "9")

print(s1.school_name)
print(s2.school_name)

s1.school_name = "Children Park School"

print("s1:", s1.school_name)
print("s2:", s2.school_name)
print("Class:", School.school_name)