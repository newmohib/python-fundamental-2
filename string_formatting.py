# String formatting/Templeting
# 1
name = "Mohib"
greeting = f"Hello, {name}"
print(f"Hello, {name}")

# 2
greeting = "Hi, {}"
with_name = greeting.format(name)
print(with_name)

# 3

longer_phrase = "Hello, {}. Today is {}."

formated = longer_phrase.format("Rahman", "Monday")

print(formated)

