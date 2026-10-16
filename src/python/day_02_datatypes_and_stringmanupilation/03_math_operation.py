"""
Day: 2
Concept: mathamatical operations
Summary:
"""

print(123 + 456)
print(789 - 456)
print(123 * 456)

print(789 / 456)
print(type(789 / 456))
# implicit type casting is done when we perform division operation, the result is a float even if both operands are integers.

print(789 // 456)
# // is used for floor division, which returns the largest integer less than or equal to the result of the division. In this case, 789 // 456 equals 1 because 789 divided by 456 is approximately 1.728, and the largest integer less than or equal to 1.728 is 1.

print(789 % 456)
# % is used for modulus, which returns the remainder of the division. In this case, 789 % 456 equals 333 because when 789 is divided by 456, the quotient is 1 and the remainder is 333.

print(2**3)
# ** is used for exponentiation, which raises a number to the power of another number. In this case, 2 ** 3 equals 8 because 2 raised to the power of 3 is 2 * 2 * 2 = 8.

# pemdaslr
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction left to right

weight = 80
height = 1.75

bmi = weight / height**2

print("Your BMI is: " + str(round(bmi, 2)))

# round function is used to round a number to a specified number of decimal places. In this case, it rounds the BMI value to 2 decimal places before converting it to a string and concatenating it with the message "Your BMI is: ".

score = 0
# += operator is used to add a value to a variable and assign the result back to the same variable.
score += 1
print(score)


# -= operator is used to subtract a value from a variable and assign the result back to the same variable.
score -= 9
print(score)

# *= operator is used to multiply a variable by a value and assign the result back to the same variable.
score *= 6
print(score)

# /= operator is used to divide a variable by a value and assign the result back to the same variable.
score /= 3
print(score)

# %= operator is used to find the remainder of a variable divided by a value and assign the result back to the same variable.
score %= 3
print(score)

# **= operator is used to raise a variable to the power of a value and assign the result back to the same variable.
score **= 3
print(score)

# //= operator is used to perform floor division on a variable and assign the result back to the same variable.
score //= 2
print(score)

# f string
# f-strings are a way to embed expressions inside string literals, using a special syntax that starts with an 'f' before the opening quote.
print(f"Your final score is: {score}")
