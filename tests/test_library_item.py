"""
Description: Unit tests for the LibraryItem class.
Author: Apurba Khan
Date: 2024-09-14
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_item.py
"""

# Importing the necessary modules for testing.
import unittest
from library_item import LibraryItem  # Importing the LibraryItem class to be tested.
from genre import Genre  # Importing the Genre enum for assigning genres to LibraryItem.

# Defining the TestLibraryItem class that inherits from unittest.TestCase.
# This class will contain all the unit tests for the LibraryItem class.
class TestLibraryItem(unittest.TestCase):

    def test_init_valid(self):
        """Test valid LibraryItem creation"""
        # Create a valid LibraryItem and check if all attributes are correctly assigned.
        item = LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
        # Assert that each attribute has been properly set.
        self.assertEqual(item.item_id, 1)
        self.assertEqual(item.title, "The Great Gatsby")
        self.assertEqual(item.author, "F. Scott Fitzgerald")
        self.assertEqual(item.publication_year, 1925)
        self.assertEqual(item.genre, Genre.FICTION)
        self.assertFalse(item.is_borrowed)

    def test_init_invalid_item_id_raises_exception(self):
        """Test that ValueError is raised for non-integer item_id"""
        # Test that a non-integer item_id raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryItem("one", "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Item Id must be numeric.")

    def test_init_blank_title_raises_exception(self):
        """Test that ValueError is raised for blank title"""
        # Test that an empty string for the title raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Title cannot be blank.")

    def test_init_blank_author_raises_exception(self):
        """Test that ValueError is raised for blank author"""
        # Test that an empty string for the author raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "The Great Gatsby", "", 1925, Genre.FICTION, False)
        self.assertEqual(str(context.exception), "Author cannot be blank.")

    def test_init_invalid_genre_raises_exception(self):
        """Test that ValueError is raised for invalid genre"""
        # Test that an invalid genre (not part of the Genre enum) raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "InvalidGenre", False)
        self.assertEqual(str(context.exception), "Invalid Genre.")

    def test_init_invalid_is_borrowed_raises_exception(self):
        """Test that ValueError is raised for non-boolean is_borrowed"""
        # Test that a non-boolean value for is_borrowed raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, "yes")
        self.assertEqual(str(context.exception), "Is Borrowed must be a boolean value.")

    def test_str_method(self):
        """Test the __str__ method of LibraryItem"""
        # Create a valid LibraryItem and test if the string representation matches the expected output.
        item = LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
        self.assertEqual(str(item), "The Great Gatsby by F. Scott Fitzgerald, 1925 (Fiction)")

# The entry point for the script that runs the tests.
if __name__ == '__main__':
    unittest.main()