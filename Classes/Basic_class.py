#!/usr/bin/env python


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def SayName(self):
        print(f"Hey my name is {self.name} and I'm {self.age} years old")


person1 = Human("Augustine", 20)
person1.SayName()

print(type(Human))

"""
This is a basic Class in python and i log the type of class to the standard output
"""
