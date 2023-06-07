# if Statement

day_of_week = input("what day of the week is it today? ").lower()

day_list = {"saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"}

if day_of_week in day_list:
    print("Have a great start to your week")
else:
    print("Invalid input!")


# in keyword

friends = ["Rolf", "Bob"]
print("Bob" in friends)

# Magic

number = 7
user_input = input("Enter 'y' if tou would like to play")
if user_input == "y" or user_input in ("y", "Y"):
    user_number = int(input("Enter 'y' if tou would like to play"))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

