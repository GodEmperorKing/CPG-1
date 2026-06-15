# adder.py
# A super simple program that adds two numbers.
# Great for learning input, numbers, and math in Python!

print("Let's add two numbers together!")
print("This is like using your fingers to count.")

num1 = input("Type the first number and press Enter: ")
num2 = input("Type the second number and press Enter: ")

# Convert the words (strings) into numbers so we can add them
result = int(num1) + int(num2)

print(num1 + " plus " + num2 + " equals " + str(result))

# Bonus: also subtract the numbers (learning more math!)
difference = int(num1) - int(num2)
print(num1 + " minus " + num2 + " equals " + str(difference))

print("Great job adding and subtracting!")