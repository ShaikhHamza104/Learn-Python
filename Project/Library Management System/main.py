class LibraryManagementSystem:
    python_books = {
    "Automate the Boring Stuff with Python": 25.99,
    "Python Crash Course": 34.95,
    "Learning Python": 45.99,
    "Effective Python": 38.50,
    "Fluent Python": 55.00,
    "Python Cookbook": 49.99,
    "Python Tricks": 29.99,
    "Head-First Python": 35.00,
    "Think Python": 26.99,
    "Python for Data Analysis": 40.00
}


    def __init__(self):
        while True:
            user=int(input('''
Welcome to Library Management System
1.Display Book and Prize  
2.add Book     
3.Buy book
4.Search Book
5.Exit to Library Management System
'''))
            if user==1:
                self.displayAllBook()

            elif user==2:
                self.addBook()

            elif user==3:
                self.buyBook()

            elif user==4:
                self.searchbook()

            elif user==5:
                print("Tank you for using this service\nHave a nice day a head")
                break

            else:
                print("Invalid input")
    
    def addBook(self):
        try:
            bookname=input("Enter book name : ")
            prize=float(input("Enter prize of book "))
        except ValueError:
            print("Please check your book name and esure that prize has number not a string ")
        if bookname not in LibraryManagementSystem.python_books:
            print(f"{bookname} and {prize} is added successfully")
            LibraryManagementSystem.python_books.update({bookname : prize})
        else:
            print(f"{bookname} is present in this libaray")


    def buyBook(self):
        try:
            bookname=input("Enter book name : ")
        except ValueError:
            print("please check your book name ")
        if bookname not in LibraryManagementSystem.python_books:
            print(f"Your{bookname} is not present in this libary")
        else:
            del LibraryManagementSystem.python_books[bookname]
            print(f"{bookname} is purchess succsfully ")

    def searchbook(self):
        try:
            bookname=input("Enter book name : ")
        except ValueError:
            print("Check for your book name")
        if bookname not in LibraryManagementSystem.python_books:
            print(f"Your {bookname} is not present in this libary")
        else:
            print("Your book is present in this libary and prize is ")
            print(LibraryManagementSystem.python_books[bookname])

    @staticmethod
    def displayAllBook():
        for book ,prize in LibraryManagementSystem.python_books.items():
            print("{} : {}$".format(book,prize))
obj=LibraryManagementSystem()