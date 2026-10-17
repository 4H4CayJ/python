"""
Day: 3
Concept:
Summary:if elif else
"""

print("welcome to the amusement part!!")

height = int(input("what is your height?\n"))

if height >= 120:
    print("you can ride the rollercoster")

    age = int(input("what is your age?\n"))

    if age >= 18:
        print("you pay 18$ for the ride")

    elif age <= 8:
        print("you pay 4$")

    else:
        print("you pay 7$")


else:
    print("because of your hight it is unsafe for you to ride the rollercoster")
