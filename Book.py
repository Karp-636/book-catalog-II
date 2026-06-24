class Book:
    total_books = 0
    

    def __init__(self, title, author, page_count, genre, status="On shelf"):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre
        Book.total_books += 1
        self.id = Book.total_books
        self.status = status
        self.borrower = None

    def describe(self):
        print(f'"{self.title}" by {self.author} - {self.page_count} pages ({self.genre})')
        print(f'{self.id} out of {self.total_books}')
        print(f'Status: {self.status}')
        if self.borrower:
            print(f'Borrowed by: {self.borrower}')


    def check_out(self, borrower):
        if self.status == "On shelf":  
            self.status = "Checked out"
            self.borrower = borrower 
            print(f'{self.title} Status: On shelf')
            return
        else: 
            print(f'{self.title} Status: Checked Out by {borrower}')
            return



book1 = Book("Nineteen Eighty-Four", "George Orwell", 328, "fiction")
book2 = Book("Marked - The House of Night", "P.C. Cast and Kristin Cast", 304, "paranormal fantasy" )
book3 = Book("Evermore - The Immortals", "Alyson Noel", 320, "paranormal fantasy")
book4 = Book("The Lightning Thief - Percy Jackson & the Olympians", "Rick Riordan", 377, "greek mythology fantasy")



book1.describe()

book3.describe()
book4.describe()

book2.check_out("Allie")
book2.describe()

#return_book() method that marks (no borrower)
#Add a class variable that stores
# every book currently checked out across the entire catalog.