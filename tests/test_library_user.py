"""
Description: Unit tests for the LibraryUser class.
Author: Apurba Khan
Date: 2024-09-02
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_user.py
"""

# Importing necessary modules for unit testing.
import unittest
from library_user import LibraryUser  # Import the LibraryUser class to be tested.
from borrower_status import BorrowerStatus  # Import BorrowerStatus for assigning user statuses.
from library_item import LibraryItem  # Import LibraryItem class to test borrowing functionality.
from genre import Genre  # Import Genre enum for associating genres with LibraryItem.

# Defining the test class for LibraryUser, inheriting from unittest.TestCase.
class TestLibraryUser(unittest.TestCase):

    def test_init_valid(self):
        """Test valid LibraryUser creation"""
        # Create a valid LibraryUser and check if all attributes are correctly assigned.
        user = LibraryUser(100, "apurba khan", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(user.user_id, 100)
        self.assertEqual(user.name, "apurba khan")
        self.assertEqual(user.email, "apurba.khan@hotmail.com")
        self.assertEqual(user.status, BorrowerStatus.ACTIVE)

    def test_init_invalid_user_id_raises_exception(self):
        """Test that ValueError is raised for non-integer user_id"""
        # Test that a non-integer user_id raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryUser("one", "apurba khan", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "User Id must be numeric.")

    def test_init_user_id_less_than_100_raises_exception(self):
        """Test that ValueError is raised for user_id less than 100"""
        # Test that a user_id less than 100 raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryUser(99, "apurba khan", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "Invalid User Id.")

    def test_init_blank_name_raises_exception(self):
        """Test that ValueError is raised for blank name"""
        # Test that a blank name raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryUser(100, "", "apurba.khan@hotmail.com", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "Name cannot be blank.")

    def test_init_invalid_email_raises_exception(self):
        """Test that ValueError is raised for invalid email"""
        # Test that an invalid email format raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryUser(100, "apurba khan", "invalid-email", BorrowerStatus.ACTIVE)
        self.assertEqual(str(context.exception), "Invalid email address.")

    def test_init_invalid_status_raises_exception(self):
        """Test that ValueError is raised for invalid status"""
        # Test that an invalid status (not in BorrowerStatus) raises a ValueError with the appropriate message.
        with self.assertRaises(ValueError) as context:
            LibraryUser(100, "apurba khan", "apurba.khan@hotmail.com", "InvalidStatus")
        self.assertEqual(str(context.exception), "Invalid Borrower Status.")

    def test_borrow_item_delinquent(self):
        """Test that delinquent user cannot borrow items"""
        # A DELINQUENT user should not be able to borrow items.
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.DELINQUENT)
        # Assert that an exception is raised when a delinquent user tries to borrow an item.
        with self.assertRaises(Exception) as context:
            user.borrow_item(LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False))
        self.assertEqual(str(context.exception), "John Doe cannot borrow the item.")

    def test_borrow_item_active(self):
        """Test that active user can borrow items"""
        # An ACTIVE user should be able to borrow an item.
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.ACTIVE)
        item = LibraryItem(1, "The Great Gatsby", "F. Scott Fitzgerald", 1925, Genre.FICTION, False)
        self.assertEqual(user.borrow_item(item), "John Doe is eligible to borrow the item.")

    def test_return_item_delinquent(self):
        """Test that returning an item changes status from delinquent to active"""
        # A DELINQUENT user returning an item should have their status changed to ACTIVE.
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.DELINQUENT)
        self.assertEqual(user.return_item(), "Item successfully returned. John Doe has returned the item, status now changed to: Active.")
        self.assertEqual(user.status, BorrowerStatus.ACTIVE)

    def test_return_item_active(self):
        """Test that returning an item does not change status if not delinquent"""
        # An ACTIVE user returning an item should remain ACTIVE.
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.ACTIVE)
        self.assertEqual(user.return_item(), "Item successfully returned.")

# The entry point for running the tests when the script is executed.
if __name__ == '__main__':
    unittest.main()