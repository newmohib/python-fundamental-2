
# Dictionary

friend_ages = {"rolf": 28, "adam": 30}
friend_ages["adam"]

friends = [{"name": "Rolf", "age": 20}, {"name": "Bolb", "age": 30}]
print(friends[1]["name"])

for friend in friend_ages:
    print(f"{friend}: {friend_ages[friend]}")

# same as

for friend, age in friend_ages.items():
    print(f"{friend}: {age}")

friend_ages_values = friend_ages.values()

print(sum(friend_ages_values) / len(friend_ages_values))

