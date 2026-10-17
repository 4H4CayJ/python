"""
Day: 3
Concept:
Summary:
"""

# odd even number detecter

number = int(input("what is your number\n"))

detection = 2 % number

if detection == 0:
    print("even")
else:
    print("odd")
