#!/usr/bin/env python


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def SayName(self):  # Class Method
        print(f"Hey my name is {self.name} and I'm {self.age} years old")


class dev(Human):  # Inheritance in Python
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def Myself(self):
        super().SayName()
        print(f"And i'm a {self.job} developer")


person1 = dev("Augustine", 20, "python")
person1.Myself()

print(type(Human))

"""
This is a basic Class in python and i log the type of class to the standard output
"""
