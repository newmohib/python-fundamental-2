
# Functions

def hello():
    print(user)


user = "Hello"

hello()


# argument and parameters


def add(x, y=3):
    result = x + y
    print(result)



# positional argument
add(3, 6)

# key word argument
add(y=5, x=3)

# combined but at first positional argument
add(10, y=5)


# Return

def add2(x, y=3):
    return x + y


result = add2(5, 6)
print(result)


def double(x):
    return x * 2


sequence = [1, 2, 3, 4]
doubled = [double(x) for x in sequence]
doubled2 = map(doubled, sequence)


