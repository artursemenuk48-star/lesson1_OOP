
class Student:
    amount_of_students = 0

    def __init__(self, name, height):
        self.name = name
        self.height = height
        Student.amount_of_students += 1

    def grow(self, cm):
        self.height += cm

    def __str__(self):
        return f"{self.name}: {self.height} см"

bob = Student("bob", 150)
kate = Student("Kate", 142)
print(Student.amount_of_students)
print(bob)



# print(bob.name, bob.height)
# print(kate.name, kate.height)
# bob.grow(20)
# print(bob.name, bob.height)