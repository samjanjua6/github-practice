#OOP is used for real world modeling. 
#It is a programming paradigm that uses objects and classes to structure code in a way that is more intuitive and easier to manage. In OOP, objects represent real-world entities, and classes define the blueprint for creating these objects. This approach allows for better organization of code, reusability, and scalability in software development.


# procedural programming -> functional programming -> object oriented programming

#creating class
class Student:

    #default constructors
    def __init__(self):
        pass
    
    #parameterized constructors
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("Creating new student in Database..")
    

#creating object (instance)
s1 = Student("Ali Raza",88)
print(s1.name,s1.marks)

s2 = Student("Hamza",40)
print(s2.name,s2.marks)

# s2 = Student()
# print(s2.name)


class Car:
    color="blue"
    brand="mercedes"

car1 = Car()
print(car1.color+" "+car1.brand)

car2 = Car()

