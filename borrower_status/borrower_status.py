"""
Description: An enumeration containing valid Borrower Statuses.
Author: Ace Faculty
Date: 2024
"""

# Importing the Enum class from the enum module.
# Enum allows us to create enumerations, which are a set of symbolic names bound to unique, constant values.
from enum import Enum

# Defining the BorrowerStatus class, which is a subclass of Enum.
# This will allow us to represent different statuses a borrower can have in the system.
class BorrowerStatus(Enum):
    """
    An enumeration listing each of the available borrower statuses.

    To use:  BorrowerStatus.STATUS_NAME.  
    Example: BorrowerStatus.MINOR

    Descriptions:
    - ACTIVE: A borrower in good standing that has borrowed materials in the last year.
    - INACTIVE: A borrower in good standing that has not borrowed materials in the last year.
    - DELINQUENT: A borrower with overdue items.
    - MINOR: A borrower below the age of 18.
    """
    
    # ACTIVE status is assigned a value of 0.
    # This indicates the borrower has borrowed materials within the last year and is in good standing.
    ACTIVE = 0

    # INACTIVE status is assigned a value of 1.
    # This status means the borrower is in good standing but has not borrowed any items in the last year.
    INACTIVE = 1

    # DELINQUENT status is assigned a value of 2.
    # A DELINQUENT borrower has overdue items and cannot borrow more items until they are returned.
    DELINQUENT = 2

    # MINOR status is assigned a value of 3.
    # A MINOR borrower is below the age of 18 and might have borrowing restrictions based on the library’s policies.
    MINOR = 3