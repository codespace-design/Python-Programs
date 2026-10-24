class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display(self):
        print(f"Name: {self.name}")
        print(f"Mark: {self.mark}")


student = Student("Gouri", 85)
student.display()