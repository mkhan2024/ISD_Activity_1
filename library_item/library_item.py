"""
Description: A class to manage LibraryItem objects.
Author: Apurba Khan
Date: 2024-09-14
"""

# Import the LibraryItem class (although not needed here as we are defining it)
from library_item import LibraryItem

# Import the Genre enum to categorize the library item by genre.
from genre import Genre

class LibraryItem:
    """
    A class to represent a library item in a library.

    Attributes:
        item_id (int): The unique identifier for the library item.
        title (str): The title of the library item.
        author (str): The author of the library item.
        publication_year (int): The year the library item was published.
        genre (Genre): The genre of the library item.
        is_borrowed (bool): Identifies whether the library item is borrowed (True) or available (False).
    """
    
    def __init__(self, item_id, title, author, publication_year, genre, is_borrowed=False):
        """
        Initializes the LibraryItem with item_id, title, author, publication_year, genre, and is_borrowed.
        
        Args:
            item_id (int): The unique identifier for the library item.
            title (str): The title of the library item.
            author (str): The author of the library item.
            publication_year (int): The year the library item was published.
            genre (Genre): The genre of the library item.
            is_borrowed (bool, optional): Indicates if the item is currently borrowed. Defaults to False.

        Raises:
            ValueError: If item_id is not an integer, title or author is blank, genre is invalid, or is_borrowed is not a boolean.
        """
        # Check if item_id is an integer.
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")

        # Ensure item_id is greater than 99 (to avoid small or invalid IDs).
        if item_id <= 99:
            raise ValueError("Invalid Item Id.")

        # Validate that the title is not blank (after removing any surrounding whitespace).
        if not title.strip():
            raise ValueError("Title cannot be blank.")

        # Validate that the author is not blank (after removing any surrounding whitespace).
        if not author.strip():
            raise ValueError("Author cannot be blank.")

        # Validate that the genre is a valid Genre enum.
        if genre not in Genre:
            raise ValueError("Invalid Genre.")

        # Ensure that is_borrowed is a boolean value.
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")
        
        # If all validations pass, assign the values to the private attributes.
        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__genre = genre
        self.__is_borrowed = is_borrowed

    # Property to access the private item_id attribute.
    @property
    def item_id(self):
        return self.__item_id

    # Property to access the private title attribute.
    @property
    def title(self):
        return self.__title

    # Property to access the private author attribute.
    @property
    def author(self):
        return self.__author

    # Property to access the private publication_year attribute.
    @property
    def publication_year(self):
        return self.__publication_year

    # Property to access the private genre attribute.
    @property
    def genre(self):
        return self.__genre

    # Property to access the private is_borrowed attribute.
    @property
    def is_borrowed(self):
        return self.__is_borrowed
