import json
import logging
from pathlib import Path
from .book import Book

CATALOG_FILE = Path("catalog.json")

class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_from_file()

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()

    def display_all(self):
        return self.books

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def save_to_file(self):
        try:
            data = [b.to_dict() for b in self.books]
            with open(CATALOG_FILE, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            logging.error(f"Error saving: {e}")

    def load_from_file(self):
        try:
            if not CATALOG_FILE.exists():
                self.save_to_file()
                return

            with open(CATALOG_FILE, "r") as file:
                data = json.load(file)

            self.books = [Book(**item) for item in data]

        except json.JSONDecodeError:
            logging.error("Corrupted file. Resetting.")
            self.books = []
            self.save_to_file()