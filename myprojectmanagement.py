import json
import os

class Library:
    def _init_(self):
        self.file = "library.json"
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, name):
        data = self.load()
        if name in data:
            print("Book already exists in liberary .")
        else:
            data[name] = "Available"
            self.save(data)
            print("Book added in liberary .")

    def borrow_book(self, name):
        data = self.load()
        if name in data and data[name] == "Available":
            data[name] = "Borrowed"
            self.save(data)
            print("Book borrowed.")
        else:
            print("Book  is not available in liberary.")

    def return_book(self, name):
        data = self.load()
        if name in data and data[name] == "Borrowed":
            data[name] = "Available"
            self.save(data)
            print("Book returned.")
        else:
            print(" you Cannot return this book.")

lib = Library()

while True:
    print("\n1. Add Book in liberary :")
    print("2. Borrow Book from liberay :")
    print("3. Return Book in liberary :")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.add_book(input("Enter the book name you want to add in liberary : "))
    elif choice == "2":
        lib.borrow_book(input("Enter the book name you want to borrown: "))
    elif choice == "3":
        lib.return_book(input("Enter the book name you want to return : "))
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please input valid choice :")