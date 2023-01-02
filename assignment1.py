"""
Replace the contents of this module docstring with your own details
Name: Xinmeng Yang
Date started: 01/01/2023
GitHub URL: https://github.com/xm-y02/Assignment1
"""


def load_books():
    # Load the books from the CSV file
    books = []
    with open("books.csv") as f:
        for line in f:
            # Split the line on the comma and strip leading/trailing whitespace
            parts = line.split(",")
            title = parts[0].strip()
            author = parts[1].strip()
            pages = int(parts[2].strip())
            required = parts[3].strip() == "r"
            books.append([title, author, pages, required])
    return books


def save_books(books):
    # Save the books to the CSV file
    with open("books.csv", "w") as f:
        for book in books:
            title, author, pages, required = book
            required_str = "r" if required else "c"
            f.write(f"{title},{author},{pages},{required_str}\n")


def menu(books):
    # Display the menu and handle menu choices
    choice = ""
    while choice != "Q":
        print("""Menu:
L - List all books
A - Add new book
M - Mark a book as completed
Q - Quit""")
        choice = input(">>> ").upper()
        if choice == "L":
            list_books(books)
        elif choice == "A":
            add_book(books)
        elif choice == "M":
            mark_book_complete(books)
        elif choice == "Q":
            save_books(books)
            print(f"{len(books)} books saved to books.csv")
            print("So many books, so little time. Frank Zappa")
            break
        else:
            print("Invalid menu choice.")


def list_books(books):
    # List the books
    if not books:
        print("No books have been added yet.")
    else:
        # Calculate the maximum width of the title and author fields
        title_width = max(len(book[0]) for book in books)
        author_width = max(len(book[1]) for book in books)

        # Print each book
        for i, book in enumerate(books):
            title, author, pages, required = book
            if required:
                print(f"*{i + 1}.  {title:{title_width}}  by {author:{author_width}}  {pages:>6} pages  ")
            else:
                print(f"{i + 1:>2}.  {title:{title_width}}  by {author:{author_width}}  {pages:>6} pages  ")

    # Calculate the number of pages required to be read
    required_books = [book for book in books if book[3]]
    required_pages = sum(book[2] for book in required_books)
    required_count = len(required_books)
    if required_count == 0:
        print("No books left to read. Why not add a new book?")
        menu(books)
    else:
        print(f"You need to read {required_pages} pages in {required_count} books.")


def add_book(books):
    # Add a book
    # Prompt for the book's title, author, and pages
    title = input("Title: ")
    while not title:
        print("Input can not be blank")
        title = input("Title: ")
    author = input("Author: ")
    while not author:
        print("Input can not be blank")
        author = input("Author: ")
    pages = 0
    while True:
        pages_input = input("Pages: ")
        # Error-check the pages input
        try:
            pages = int(pages_input)
            if pages <= 0:
                print("Number must be > 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")

    # Add the book to the list
    books.append([title, author, pages, True])
    print(f"{title} by {author}, ({pages} pages) added to Reading Tracker")


def mark_book_complete(books):
    # Mark a book as complete
    if not books:
        print("No books have been added yet.")
    else:
        required_books = [book for book in books if book[3]]
        if not required_books:
            print("No required books!")
            menu(books)
        else:
            # Print the list of books
            list_books(books)

        while True:
            try:
                book_number = int(input("Enter the number of a book to mark as completed: "))
                if book_number < 1:
                    print("Number must be > 0")
                elif book_number > len(books):
                    print("Invalid book number")
                elif not books[book_number - 1][3]:
                    print("That book is already completed")
                    menu(books)
                else:
                    title = books[book_number - 1][0]
                    author = books[book_number - 1][1]
                    books[book_number - 1][3] = False
                    print(f"{title} by {author} completed!")
                    return
            except ValueError:
                print("Invalid input; enter a valid number")


def main():
    books = load_books()
    print(f"Reading Tracker 1.0 - by Xinmeng Yang")
    print(f"{len(books)} books loaded")
    menu(books)


if __name__ == "__main__":
    main()
