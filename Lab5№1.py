class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
    def get_info(self):
        return f"Название книги: {self.__title}, Автор: {self.__author}, Год издания: {self.__year}"

book1 = Book("Горе от ума","Грибоедов","1824")
print(book1.get_info())
# print(book1.title)