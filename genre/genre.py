"""
Description: An enumeration containing valid Genres for library items.
Author: Ace Faculty
Date: 2024
"""

# Importing the Enum class to create the Genre enumeration.
from enum import Enum

# Importing the LibraryItem class to associate the genres with items (though not directly used here).
from library_item import LibraryItem

# Defining the Genre enumeration which contains valid genres for library items.
class Genre(Enum):
    """
    An enumeration listing each of the available genres for a library item.

    To use: Genre.GENRE_NAME.
    Example: Genre.FICTION

    Descriptions:
    - FICTION: Items that are fictional stories.
    - NONFICTION: Items that are factual and based on real events or people.
    - MYSTERY: Items centered around suspense, crime, or detective stories.
    - SCIFI: Science fiction items with futuristic or advanced technological themes.
    - FANTASY: Items involving magical, fantastical, or supernatural elements.
    - BIOGRAPHY: Items about the life of a person, typically non-fictional.
    - HISTORY: Items focused on historical events, figures, and facts.
    - CHILDREN: Items aimed at or suitable for a children's audience.
    """

    # FICTION genre is assigned a string value of "Fiction".
    # Fiction includes literary works with imaginative storytelling.
    FICTION = "Fiction"

    # NONFICTION genre is assigned a string value of "Non-Fiction".
    # Non-fiction encompasses works based on facts and reality.
    NONFICTION = "Non-Fiction"

    # MYSTERY genre is assigned a string value of "Mystery".
    # Mystery works focus on suspense, crime, or solving puzzles.
    MYSTERY = "Mystery"

    # SCIFI genre is assigned a string value of "Science Fiction".
    # Science fiction often involves futuristic technology or space themes.
    SCIFI = "Science Fiction"

    # FANTASY genre is assigned a string value of "Fantasy".
    # Fantasy works contain magical or other supernatural elements.
    FANTASY = "Fantasy"

    # BIOGRAPHY genre is assigned a string value of "Biography".
    # Biography items tell the true story of a person's life.
    BIOGRAPHY = "Biography"

    # HISTORY genre is assigned a string value of "History".
    # History works focus on significant historical events and people.
    HISTORY = "History"

    # CHILDREN genre is assigned a string value of "Children".
    # Children's literature is tailored for younger readers.
    CHILDREN = "Children"
