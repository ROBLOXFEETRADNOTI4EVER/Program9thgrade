import threading
from time import sleep
import os

class Library:
    def __init__(self, bookList, name, databaseName):
        self.bookList = bookList
        self.name = name
        self.lendDict = {}
        self.databaseName = databaseName

    def displayBooks(self):
        print(f"We have the following books in our library '{self.name}':")
        for book in self.bookList:
            print(book.strip())
    def addBook(self, book):
        if book in self.bookList:
            print("Book already exists.")
        else:
            self.bookList.append(book)
            with open(self.databaseName, 'a') as bookDatabase:
                bookDatabase.write(book + '\n')
            print(f"'{book}' has been added to the library.")
    def lendBook(self, book, user):
        if book not in self.bookList:
            print(f"Apologies! We don't have the book '{book}' in our library YET!")
        elif book in self.lendDict:
            print(f"Sorry, the book '{book}' is already being used by {self.lendDict[book]}.")
        else:
            self.lendDict[book] = user
            print(f"The book '{book}' has been lent to {user}. Database updated.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"The book '{book}' has been returned successfully.")
        else:
            print("The book does not exist in the lending database.")
def main():
    os.system('clear')
    while True:
        print(f"Welcome to the {library.name} library. Following are the options:")
        choice = """
        1. Display Books
        2. Lend a Book
        3. Add a Book
        4. Return a Book
        """
        print(choice)
        userInput = input("Press 'Q' to quit or 'C' to continue\n> ").strip().upper()
        if userInput == "C":
            try:
                userChoice = int(input("Select an option to continue\n> "))
                if userChoice == 1:
                    library.displayBooks()
                elif userChoice == 2:
                    book = input("Enter the name of the book you want to lend\n> ")
                    user = input("Enter the name of the user\n> ")
                    library.lendBook(book, user)
                elif userChoice == 3:
                    book = input("Enter the name of the book you want to add\n> ")
                    library.addBook(book)
                elif userChoice == 4:
                    book = input("Enter the name of the book you want to return\n> ")
                    library.returnBook(book)
                else:
                    print("Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a valid option number.")
        elif userInput == 'Q':
            print("Thank you for using the library system. Goodbye!")
            break
        else:
            print("Please enter a valid option.")



            
if __name__ == '__main__':
    bookList = []
    databaseName = input("Enter the name of the database file with extension\n> ")
    try:
        with open(databaseName, "r") as bookDatabase:
            for book in bookDatabase:
                bookList.append(book.strip())
    except FileNotFoundError:
        print(f"The file '{databaseName}' does not exist. Creating a new one.")
        open(databaseName, 'w').close()

    library = Library(bookList, "Balazsloveslavesz", databaseName)
    main()
