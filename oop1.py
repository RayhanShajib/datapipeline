'''
Store a personal information
Define each person with data:

 first name
 last name
 age
 occupation

Create a new person called Matti and assign personal details

'''

class Person:
    def __init__(self, firstName, lastName, age, occupation):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.occupation = occupation

    def person_details(self):
        print("First Name:", self.firstName)
        print("Last Name:", self.lastName)
        print("Age:", self.age)
        print("Occupation:", self.occupation)

matti = Person("Matti", "Rayhan", 22, "student")
matti.person_details()
