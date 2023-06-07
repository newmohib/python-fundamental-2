
# List it's can add/update/delete and also access by index number/ has order like list[0]
list = ["Bob", "Rolf", "Anne"]

# Tuples it's can't add/update/delete and also can't access by index number like list[0]
tuple = ("Bob", "Rolf", "Anne")

# set it's can add/update/delete and has no duplicate elements and hasn't order/index number
sets = {"Bob", "Rolf", "Anne"}

# sample Data

friends = {"Mohib", "Bob", "Rof", "Anne"}

abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

# empty

local_friends = abroad.difference(friends)
print(local_friends)

# Total

total_friends = friends.union(abroad)
print(total_friends)

# intersection

art = {"Mohib", "Bob", "Rof", "Anne"}
science = {"Bob", "Anne"}

both = art.intersection(art);
print(both)


