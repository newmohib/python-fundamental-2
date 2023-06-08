
# List Comprehensions

numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]
print(doubled)

# List Comprehensions with conditions

friends = ["Bob", "Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(friends, starts_s)
print("friends: ", id(friends), "starts_s", id(starts_s))