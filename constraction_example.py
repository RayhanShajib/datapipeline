'''
Use class-level attributes(root of the class) only for values that are the same for every object.

Examples:
- Number of weels on a car
- Pi contant
- Configuration shared by all instances
- version numbers....

'''

class Car:
    wheels = 4 # come for all cars as default;

'''
These attributes live on the class, not the object
 
Use constructor (__init__) for instance specific data. They are unique per object

Examples:
- Color color
- max speed
- current car
- registration number
'''

class Car:
    weels = 4 # come for all cars as default;

    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

'''
Every time you create a new object contractor (__init__) runs and give that specific object its own attributes

why not put object specific attributes in the root? Because attribute in the root are share unless overwritten.

For Example:
'''

class Person:
    hobbies = [] # share list

p1 = Person()
p2 = Person()

p1.hobbies.append("Coding")
p1.hobbies.append("Sleeping")
p2.hobbies.append("Reading")
print(p2.hobbies)

'''
If the list was inside the __init__ each would get its own list.
'''

class Student:
    def __init__(self):
        self.hobbies = []

s1 = Student()
s2 = Student()


s1.hobbies.append("Coding")
s1.hobbies.append("Sleeping")
s2.hobbies.append("Reading")

print(s1.hobbies)
print(s2.hobbies)
