
import datetime

# Loop

number = 7


while True:
    user_input = input("Enter 'y' if tou would like to play? (Y/n)")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))

    if user_number == number:
        print("You guessed correctly!")
        break
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")


# for loop

friends = ["Mohib", "Bob", "Rof", "Anne"]

for friend in friends:
    print(friend)

# skip the loop

grades = [35, 68, 52, 22, 42]
total = sum(grades)
amount = len(grades)
print(total/amount)

# the loop for total and average spent time


while True:
    again_try = input("Can you check start/again? (Y/n) ")
    if again_try == "n":
        break
    total_loop = int(input("Maximum Loop number Test for spent time. "))

    date_time = datetime.datetime.now()
    m_second = date_time.strftime("%f")

    for number in range(total_loop):
        if False:
            print("completed")

    date_time_2 = datetime.datetime.now()
    m_second_2 = date_time_2.strftime("%f")

    spent_time = int(m_second_2) - int(m_second)

    print("Total time for loop", spent_time)
    if spent_time != 0:
        print("Average time for loop", total_loop/spent_time)
    else:
        print("Spent Time is", spent_time)

