class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print(f"Average marks of {self.name}: {avg}")


s1 = Student("deepa", 80, 70, 90)
s1.average()