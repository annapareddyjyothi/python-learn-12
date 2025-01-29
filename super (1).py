class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        super().show()  # Calls the show() method of Parent
        print("This is the Child class")

obj = Child()
obj.show()
