# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute."

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Pease", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Cather in the Rye", "JD Salinger", 234, 29.95)

# # TODO: print the price of book1
# print(b1.getprice())
#
# # TODO: try setting the discount
# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)