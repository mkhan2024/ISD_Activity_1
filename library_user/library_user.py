"""
Description: A class to manage LibraryUser objects.
Author: Apurba Khan
Date: 2024-09-14
"""

# Importing necessary modules and enumerations.
# re: Used for validating email addresses.
# Genre: To define genres for items the user may borrow.
# BorrowerStatus: To track the user's borrowing status.
import re
from genre import Genre
from borrower_status import BorrowerStatus

class LibraryUser:
    """
    A class to represent a library user.

    Attributes:
        user_id (int): The unique identifier for the library user.
        name (str): The name of the library user.
        email (str): The email of the library user.
        status (BorrowerStatus): The status of the library user (e.g., ACTIVE, DELINQUENT).
    """
    
    def __init__(self, user_id, name, email, status):
        """
        Initializes the LibraryUser with user_id, name, email, and status.
        
        Args:
            user_id (int): Unique identifier for the library user.
            name (str): The name of the library user.
            email (str): The email address of the library user.
            status (BorrowerStatus): The current borrowing status of the library user.

        Raises:
            ValueError: If user_id is not an integer, user_id is not greater than 99, name or email is blank, email is invalid, or status is invalid.
        """
        # Ensure user_id is numeric.
        if not isinstance(user_id, int):
            raise ValueError("User Id must be numeric.")
        
        # Validate that user_id is greater than 99.
        if user_id <= 99:
            raise ValueError("Invalid User Id.")

        # Check that the name is not empty or just spaces.
        if not name.strip():
            raise ValueError("Name cannot be blank.")
        
        # Validate the email address using a regular expression pattern.
        if not email.strip() or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address.")

        # Check if the status is a valid BorrowerStatus enum value.
        if status not in BorrowerStatus:
            raise ValueError("Invalid Borrower Status.")
        
        # Assign validated values to private attributes.
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__status = status

    # Property for accessing user_id.
    @property
    def user_id(self):
        return self.__user_id

    # Property for accessing name.
    @property
    def name(self):
        return self.__name

    # Property for accessing email.
    @property
    def email(self):
        return self.__email

    # Property for accessing status.
    @property
    def status(self):
        return self.__status

    def borrow_item(self, item):
        """
        Determines if the user can borrow an item.

        Args:
            item (LibraryItem): The item to be borrowed.

        Raises:
            Exception: If the user cannot borrow the item due to a delinquent status or if the item is already borrowed.
        
        Returns:
            str: A message indicating the borrowing status.
        """
        # Check if the user is allowed to borrow the item.
        if not self.can_borrow(item):
            raise Exception(f"{self.__name} cannot borrow the item.")
        
        # Mark the item as borrowed.
        item.is_borrowed = True
        return f"{self.__name} is eligible to borrow the item."

    def return_item(self):
        """
        Processes the return of an item.

        Returns:
            str: A message indicating the return status and whether the user's status has changed.
        """
        # If the user is delinquent, change their status to ACTIVE upon return.
        if self.__status == BorrowerStatus.DELINQUENT:
            self.__status = BorrowerStatus.ACTIVE
            return f"Item successfully returned. {self.__name} has returned the item, status now changed to: {self.__status.value}."
        
        # If the user was not delinquent, simply return a success message.
        return "Item successfully returned."

    def can_borrow(self, item):
        """
        Checks if the user can borrow the given item.

        Args:
            item (LibraryItem): The item to be borrowed.

        Returns:
            bool: True if the user can borrow the item, False otherwise.
        """
        # User cannot borrow if their status is DELINQUENT or if the item is already borrowed.
        if self.__status == BorrowerStatus.DELINQUENT:
            return False
        if item.is_borrowed:
            return False
        
        # Otherwise, the user is eligible to borrow the item.
        return True