class A:
    def show(self):
        print("This is class A")

class B:
    def show(self):
        print("This is class B")

class C(A, B):
    pass

c = C()

c.show()

print(C.mro())