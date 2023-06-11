
# Dictionary Comprehension

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "865"),
    (2, "Jose", "4566"),
    (4, "username", "1234")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("Enter tour Username: ")


if username_mapping.get(username_input):
    password_input = input("Enter tour Password: ")
    _, username, password = username_mapping.get(username_input)

    if password_input == password:
        print("Your details are correct.")
    else:
        print("Your details are incorrect.")
else:
    print("Your Username is Incorrect")