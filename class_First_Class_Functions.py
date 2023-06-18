
from operator import itemgetter


# First-Class Functions

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


try:
    result = calculate(20, 0, operator=divide)
    print(result)

except ZeroDivisionError as e:
    print(e)


# search

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 20},
    {"name": "Rolf Smith", "age": 20},
    {"name": "Rolf Smith", "age": 20}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))


# lambda function

print("lamda function: ", search(friends, "Rolf Smith", lambda friend: friend["name"]))

# python self module , pass an object and return a value form object

print("lamda function: ", search(friends, "Rolf Smith", itemgetter("name")))


