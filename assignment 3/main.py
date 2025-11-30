import logging
from library_manager.book import Book
from library_manager.inventory import LibraryInventory

logging.basicConfig(level=logging.INFO)

def menu():
    print("\n===== Assignment 3 — Library Inventory Manager =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book by Title")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid number.")
            continue

        if choice == 1:
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added.")

        elif choice == 2:
            isbn = input("ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                if book.is_available():
                    book.issue()
                    inventory.save_to_file()
                    print("Issued.")
                else:
                    print("Already issued.")
            else:
                print("Book not found.")

        elif choice == 3:
            isbn = input("ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                if not book.is_available():
                    book.return_book()
                    inventory.save_to_file()
                    print("Returned.")
                else:
                    print("Book is already available.")
            else:
                print("Book not found.")

        elif choice == 4:
            for b in inventory.display_all():
                print(b)

        elif choice == 5:
            title = input("Enter title: ")
            results = inventory.search_by_title(title)
            if results:
                for r in results:
                    print(r)
            else:
                print("No match found.")

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()