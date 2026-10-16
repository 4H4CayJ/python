print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100

per_person_ammount = total * tip_percent / people

print(f"each person will pay {per_person_ammount}")
