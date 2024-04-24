import os

# Define a class representating a book
class Book:

    GENRE_NAMES = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
# Constructor to set a book
    def __init__(self, isbn, title, author, genre, available):
        
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available
        
   # Getters to access private attributes
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre_id(self):
        return self.__genre

    def get_genre_name(self):
        return self.GENRE_NAMES.get(self.__genre, "Unknown")

    def get_availability(self):
        return "Available" if self.__available else "Borrowed"
    
    # Setters to update private attributes 
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre
    
    # Methods for borrowing and returning a book
    def borrow_it(self):
        self.__available = False

    def return_it(self):
        self.__available = True
    
    # String representation of a Book object
    def __str__(self):
        return f"{self.get_isbn()},\t{self.get_title()},\t{self.get_author()},\t{self.get_genre_name()},\t{self.get_availability()}"

import os
# Function to load books from a file into a list
def load_books(book_list, file_path):
    while True:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    attributes = line.strip().split(',')
                    isbn, title, author, genre, available = attributes
                    genre = int(genre)
                    available = available.lower() == 'true'
                    book_list.append(Book(isbn, title, author, genre, available))
            print("Book catalog has been loaded.")
            return len(book_list)
        else:
            file_path = input("File not found. Re-enter book catalog filename: ")
# Function to print a menu with options and get user's selection
def print_menu(heading, options):
    print("\n" + heading)
    print("=" * len(heading))
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = True
    while choice:
        choice = input("Enter your selection: ").strip()
        if choice in options:
            return choice
        elif PASSCODE and choice == PASSCODE:
            return choice
        else:
            print("Invalid option")
# Function searching for books based on a search string
def search_books(book_list, search_string):
    search_result = []
    for book in book_list:
        if search_string.lower() in book.get_isbn().lower() or \
                search_string.lower() in book.get_title().lower() or \
                search_string.lower() in book.get_author().lower() or \
                search_string.lower() in book.get_genre_name().lower():
            search_result.append(book)
    return search_result
# Function for borrowing a book
def borrow_book(book_list):
    isbn = True
    while isbn:
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

        for book in book_list:
            if book.get_isbn() == isbn:
                if book.get_availability() == 'Available':
                    print(f"{book.get_title()} with ISBN {isbn} successfully borrowed.")
                    book.borrow_it()  # Update availability to 'Borrowed'
                    return
                else:
                    print(f"'{book.get_title()}' with ISBN {isbn} is not currently available.")
                    return
    
        print("No book found with that ISBN.")
        break  # Exit the loop after checking all books

def find_book_by_isbn(book_list, isbn):
    for book in book_list:
        if book.get_isbn() == isbn:
            return book
    return None
  # Function for returning a book  
def return_book(book_list):
    isbn = True
    while isbn:
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

        for book in book_list:
            if book.get_isbn() == isbn:
                if book.get_availability() == 'Borrowed':
                    print(f"{book.get_title()} with ISBN {isbn} successfully returned.")
                    book.return_it()  # Update availability to 'Available'
                    return
                else:
                    print(f"{book.get_title()} with ISBN {isbn} is not currently borrowed.")
                    return
        print("No book found with that ISBN.")
        break  # Exit the loop after checking all books

# Function for getting the genre ID based on genre name        
def get_genre_code(genre_name):
    for genre_id, name in Book.GENRE_NAMES.items():
        if name.lower() == genre_name.lower():
            return genre_id
    return None

# Function for adding a book to the book list
def add_book(book_list):
    print("\n-- Add a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    # Loop until a valid genre is entered
    genre_name = True
    while genre_name:
        genre_name = input("Enter genre: ").strip()
        genre = get_genre_code(genre_name)
        if genre is not None:
            break  # Valid genre, break out of the loop
        else:
            print(f"Invalid genre. Choices are: {', '.join(Book.GENRE_NAMES.values())}")

    new_book = Book(isbn, title, author, genre, True)
    book_list.append(new_book)
    print(f"'{title}' with ISBN {isbn} successfully added.")

# Function for removing a book from the book list
def remove_book(book_list):
    print("\n-- Remove a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()
    book_to_remove = None
    # Iterate book list to find the book with the given ISBN
    for book in book_list:
        if book.get_isbn() == isbn:
            book_to_remove = book
            break
    # remove the book from the list if does not found.
    if book_to_remove:
        book_list.remove(book_to_remove)
        print(f"Book with ISBN {isbn} successfully removed.")
    else:
        print("No book found with that ISBN.")
# Function for printing the book catalog
def print_books(book_list):
    # Check if the book list is empty
    if not book_list:
        print("No matching books found.")
        return
    # Header for the catalog
    print("\n-- Print book catalog --:")
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:s}".format(
        "ISBN", "Title", "Author", "Genre", "Availability"))
    print("-" * 14, "-" * 25, "-" * 25, "-" * 20, "-" * 12)
     # Print each book's information
    for book in book_list:
        print("{:<14s} {:<25s} {:<25s} {:<20s} {:s}".format(
            book.get_isbn(), book.get_title(), book.get_author(), book.get_genre_name(), book.get_availability()))

# Function to save the books from the list to a file
def save_books(book_list, file_path):
    with open(file_path, 'w') as file:
         # Write each book's information to the file in CSV format
        for book in book_list:
            file.write(f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre_id()},{book.get_availability()}\n")

# Passcode for accessing library menu.
PASSCODE = "2130"

# Function to handle library menu options
def library_menu(book_list, file_path):
    users_menu_options = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "4": "Add a book",
        "5": "Remove a book",
        "6": "Print catalog",
        "0": "Exit to main menu"
    }
    library_menu_choice = True
    while library_menu_choice:
        library_menu_choice = print_menu("Reader's Guild Library - Librarian Menu", users_menu_options)
        # Handle library menu options based on user input
        if library_menu_choice == "1":
            search_books()
        elif library_menu_choice == "2":
            borrow_book(book_list)
        elif library_menu_choice == "3":
            return_book(book_list)
        elif library_menu_choice == "4":
            add_book(book_list)
        elif library_menu_choice == "5":
            remove_book(book_list)
        elif library_menu_choice == "6":
            print_books(book_list)
        elif library_menu_choice == "0":
            save_books(book_list, file_path)
            print("-- Exit the system --")
            print("Book catalog has been saved.")
            print("Good Bye!")
            break
        else:
            print("Invalid option")
        
# Main function to run the program
def main():
    print("Starting the system ...")
    book_list = []
    file_path = input("Enter book catalog filename: ")
    
    # Load books from the provided file
    if not load_books(book_list, file_path):
        print("Loading books failed.")
        return

    # Define the options for the main menu
    menu = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "0": "Exit the system"
    }

    while True:
        # Display the main menu and get user's selection
        choice = print_menu("Reader's Guild Library - Main Menu", menu)
        
        # Handle the user's selection
        if choice == "1":
            print("\n-- Search for book --")
            search_string = input("Enter search value: ")
            search_result = search_books(book_list, search_string)
            print_books(search_result)
        elif choice == "2":
            print("\n-- Borrow a book --")
            borrow_book(book_list)
        elif choice == "3":
            print("\n-- Return a book --")
            return_book(book_list)
        elif choice == "0":
            print("\n-- Exit the system --")
            # Save the books to the file and exit the system
            save_books(book_list, file_path)
            print("Book catalog has been saved.\nGoodbye!")
            break
        elif choice == PASSCODE:
            # Enter the library menu if the passcode is correct
            library_menu(book_list, file_path)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()

