class book:
    def __init__(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Pub Year: ")
        self.genre = input("genre: ")
        availability_input = input("Is the book available? (yes/no): ").lower()
        self.availability = availability_input == "yes"

    def borrow(self):
        if self.availability == True:
            print("Book Borrowed.")
            self.availability = False
        else:
            print("Book unavailable")

    
    def return_book(self):
        print("Book Returned.")
        self.availability = True

    def get_info(self):
        availability_status = "Available" if self.availability else "Not Available"

        print(f"{self.title}\n {self.author}\n {self.publication_year}\n {self.genre}\n {self.availability}")

book1 = book()

    