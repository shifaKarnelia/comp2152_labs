from Person import Person

class Student(Person):
    def __init__(self,name,age,height,major):
        super().__init__(name,age, height)
        self.major = major
        print("this time its student object")

    def __del__(self):
        print("deleting the student object")

s1 = Student("marie",22,6,"computer Science")

print(s1.name)