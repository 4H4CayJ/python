"""
Day: 1
Concept: variables
Summary: Learning how to use variables in Python.
"""

name = input("What is your name? ")
print(f"Hello, {name}!")

# f strings allow you to embed expressions inside string literals, using curly braces {}.

name = "jack"
print(name)

name = "jill"
print(name)

print(len(name))

# len() is a built-in function that returns the number of items in an object. When the object is a string, len() returns the number of characters in the string.

print(len(input("What is your name? ")))

username = input("What is your username? ")
lenth = len(username)
print(f"Your username has {lenth} characters.")
