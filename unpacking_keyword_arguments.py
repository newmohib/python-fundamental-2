
# Unpacking Keyword arguments

def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)

details = {"name": "Rony", "age": 25}
named(**details)


# 2

def print_nicely(**kwargs):
    named(**kwargs)
    for name, value in kwargs.items():
        print(f"{name}: {value}")


print_nicely(name="Hasan", age=50)


# 3

def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, name="foisal", age=62)


# 4

def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob") # Error, must be mapping
myfunction(**None) # Error


