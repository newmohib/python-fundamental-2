
# Destructuring

friend_ages = {"rolf": 28, "adam": 30}

for friend, age in friend_ages.items():
    print(f"{friend}: {age}")


t = 5, 11
x, y = t


peoples = [("Bob", 42, "Mechanic"), ("Jems", 24, "Artist")]

for name, age, professions in peoples:
    print(name, age, professions)

# skip variable in Destructuring

for name, _, professions in peoples:
    print(name, professions)


# separate list in Destructuring

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(*head)
print(tail)



