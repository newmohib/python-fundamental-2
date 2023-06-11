
# Unpacking Arguments

# 1
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 2, 3))

# 2
def add(x, y):
    return x + y


# its must item or arguments
nums = [5, 6]
print(add(*nums))

# 3

# dictionary
nums_dictionary = {"x": 5, "y": 4}
print(add(**nums_dictionary))


#4

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


nums3 = [4, 5, 6, 8, 9]
print(apply(*nums3, operator="+"))
print(apply(*nums3, operator="*"))
