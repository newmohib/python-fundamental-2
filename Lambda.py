
# Lambda functions


add = lambda x, y: x+y


print(add(5, 6))

sequence = [1, 2, 3, 4]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled2 = list(map(lambda x: x * 2, sequence))

print(doubled)
print(doubled2)

