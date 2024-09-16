"""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Apurba Khan
Date: 2024-09-14
"""

# Importing necessary classes, enumerations, and test modules.
from library_item import LibraryItem
from library_user import LibraryUser
from genre import Genre
from borrower_status import BorrowerStatus
from tests import test_library_item, test_library_user

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # Ensure all statements that could result in an exception are handled.
    # Any caught exceptions will print the exception message to the console.

    # 1. Create an instance of the LibraryItem class with valid inputs.
    try:
        item = LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
    except ValueError as e:
        # Print the exception message if invalid inputs are provided.
        print(e)

    # 2. Print each of the attributes of the valid LibraryItem instance using accessors.
    try:
        print(f"Item ID: {item.item_id}")
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Publication Year: {item.publication_year}")
        print(f"Genre: {item.genre.value}")  # Using .value to get the string value of the enum.
        print(f"Is Borrowed: {item.is_borrowed}")
    except NameError:
        # Handle the case where the LibraryItem instance wasn't created.
        print("LibraryItem instance not created due to previous error.")

    # 3. Attempt to create instances of LibraryItem with invalid inputs and catch exceptions.
    # Example of invalid item_id (non-integer).
    try:
        invalid_item = LibraryItem("one", "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
    except ValueError as e:
        print(e)

    # Example of blank title.
    try:
        invalid_item = LibraryItem(2, "", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
    except ValueError as e:
        print(e)

    # Example of blank author.
    try:
        invalid_item = LibraryItem(3, "The Great Gatsby", "", 1925, Genre.FICTION, False)
    except ValueError as e:
        print(e)

    # Example of invalid genre.
    try:
        invalid_item = LibraryItem(4, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "InvalidGenre", False)
    except ValueError as e:
        print(e)

    # Example of invalid is_borrowed (non-boolean value).
    try:
        invalid_item = LibraryItem(5, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, "yes")
    except ValueError as e:
        print(e)

    # 4. Create a valid LibraryUser and test borrowing and returning items.
    try:
        user = LibraryUser(100, "apurba Khan", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
        print(f"User ID: {user.user_id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Status: {user.status.value}")
        print(user.borrow_item(item))  # Borrow the item.
        print(user.return_item())  # Return the item.
    except ValueError as e:
        # Catch any validation errors during user creation.
        print(e)
    except Exception as e:
        # Catch any other exceptions during borrowing/returning.
        print(e)

    # 5. Attempt to create LibraryUser instances with invalid inputs.
    # Example of non-integer user_id.
    try:
        user = LibraryUser("one", "apurba khan", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
    except ValueError as e:
        print(e)

    # Example of blank name.
    try:
        user = LibraryUser(100, "", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
    except ValueError as e:
        print(e)

    # Example of invalid email.
    try:
        user = LibraryUser(100, "apurba khan", "invalid-email", BorrowerStatus.ACTIVE)
    except ValueError as e:
        print(e)

    # Example of invalid borrower status.
    try:
        user = LibraryUser(100, "apurba khan", "apurba.khan@hotmail.com", "InvalidStatus")
    except ValueError as e:
        print(e)

# Entry point of the script to run the main function.
if __name__ == "__main__":
    main()