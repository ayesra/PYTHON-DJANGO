import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-------------------------------------")


#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class




#! Everything in Python is class
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
        
# test = [122, "henry", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test)


#! Defining class
#! Difference between class attributes and instance attributes

# class Person:
#     company = "clarusway"
#     department = "IT"
    
    
    
# person1 = Person()
# person2 = Person()

# print(person1.company)

# Person.job = "developer"
# print(person1.job)

# person2.location = "Germany"




#! SELF keyword


# class Person:
#     company = "clarusway"
#     department = "IT"
    
#     def test(self):
#         print("test")
    
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age    
    
#     def get_details(self):
#         print(self.name, self.age)
    
    #! Static methods:
    
#     @staticmethod
#     def salute():
#         print("Hi there!")
    
    
# person1 = Person()
# person2 = Person()

# person1.test()
# Person.test(person1)

# person1.set_details("barry", 40)
# person2.set_details("henry", 35)

# print(person2.age)
# person2.get_details()

# person1.salute()
# person2.salute()

#! Special methods (init, str)
#!     Encapsulation  & Abstraction

# class Person:
#     company = "clarusway"
#     department = "IT"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._salary = 3000
#         self.__id = 35
        

#     def __str__(self):
#         return f"{self.name} - {self.age}"


# person1 = Person("Hasan", 20)


# print(person1)
# print(person1._salary)
# person1._salary = 4000
# print(person1._salary)
# # print(person1.__id)

# person1._Person__id = 23
# print(person1._Person__id)



# my_list = [3,4,1,5]
# my_list.sort()
# print(my_list)


#!     Inheritance

class Person:
    company = "Clarusway"
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} {self.age}"
    
    def get_details(self):
        return print(self.name, self.age)

class Lang:
    def __init__(self, lang):
        self.lang = lang
        
    def display_langs(self):
        print(self.lang)
        

class Employee(Person, Lang):
    
    def __init__(self, name, age, path, lang, location="Germany"):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.path = path
        Lang.__init__(self, lang)
        # self.lang = lang
        self.location = location

    def get_details(self):
        super().get_details()
        Lang.display_langs(self)
        print(self.path)


emp1 = Employee("victor", 33, ["fullstack", "devops"], ["python", "javascript"])

# emp1.get_details()


print(Employee.mro())
# print(help(Employee))
# print(emp1.__dict__)


# from django.db import models


# class Makale(models.Model):
#     adı = models.CharField(max_length=30)
#     yazarı = models.CharField(max_length=30)
    
#     class Meta:
#         ordering = ["yazarı"]
        
        






















print("-------------------------------------")