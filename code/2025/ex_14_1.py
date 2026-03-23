class Book():
    """Book class defines books in a library"""

    def __init__(self,
                title="Nasreddin Hoca Fıkraları",
                author="Memet Fuat",
                category="Philosophy",
                language="TR",
                id="AB-14",
                n_available=0,
                n_total=3,
                ):
        self.title = title
        self.author = author
        self.category = category
        self.language = language
        self.id = id
        self.n_total = n_total
        self.n_available = n_available

    # Methods of the class
    def print_info(self):
        print(f"'{self.title}' by {self.author}")

    def borrow_book(self):
        if self.n_available > 0:
            self.n_available -= 1
            print(f"You borrowed: ")
            self.print_info()
        else:
            print("This book is not available at the moment.")


if __name__ == "__main__":
    library = []
    def_book = Book()
    print("The first default book is:")
    def_book.print_info()
    library.append(def_book)
    my_favorite_book = Book(
        title="Alice in Wonderland",
        author="Lewis Carroll",
        category="novel",
        language="EN",
        id="A-01")
    library.append(my_favorite_book)
    # Print all the books in the library list
    print("The list of books in the library:")
    for book in library:
        book.print_info()

    my_favorite_book.n_available = 2
    my_favorite_book.borrow_book()

