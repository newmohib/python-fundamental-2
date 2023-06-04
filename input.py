# input

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} squre feet is {square_metres:.2f} square metres.")

age = int(input("Enter your age: "))
months = age * 12
print(f"Your age, {age}. is equal to {months} months. ")
minutes = age * 12 * 30 * 24 * 60

second = age * 12 * 30 * 24 * 60 * 60
print(f"Your age, {age}. is equal to {months} months. is equal to {minutes} minutes. is equal to {second} second")


