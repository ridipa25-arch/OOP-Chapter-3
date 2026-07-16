
class Parent:
    def show_message(self):
        print("Hello! This is the parent class.")


class Child(Parent):
    def child_message(self):
        print("Hello! This is the child class.")

c = Child()
c.show_message()
c.child_message()