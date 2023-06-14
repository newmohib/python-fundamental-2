
# class Method and static methods

class ClassTest:
    def instnace_method(self):
        print(f"Called instance_method of {self}")

    # decorator
    @classmethod
    def calss_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


class_test = ClassTest()
class_test.instnace_method()

ClassTest.calss_method()

ClassTest.static_method()


# toople


class Book:
    TYPES = ("hardcover", "paperback")

    def __init(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return  f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight +100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)


book = Book("Harry Potter", "hardcover", 1500)

print(book.name)


book = Book.hardcover("Harry Potter", 1500)
print(book)

light = Book.paperback("Harry Potter", 600)
print(light)


