
# errors python

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
        # raise TypeError
        # raise ValueError
        # raise RuntimeError

    return dividend / divisor


grades = [20, 50, 40, 85]
# grades = []


print("Welcome to the average grade program.")


try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.", e)
except ValueError:
    print("Value Error")
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you")


students = [
    {"name": "Bob", "grades": [45, 65]},
    {"name": "Fof", "grades": []},
    {"name": "Rof", "grades": [45, 65]}
]


try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
    print(f"Error: {name} has no grades!", e)
except ValueError:
    print("Value Error")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculated --")


# Custom Error Class

class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.page_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.page_read + pages} pages, but this book only has {self.page_count} pages"
            )
        self.page_read += pages
        print(f"Your have now read {self.page_read} pages out of {self.page_count}")


python101 = Book("Python 101", 50)

try:
    python101.read(35)
    python101.read(50)

except TooManyPagesReadError as e:
    print(e)


