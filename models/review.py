#!/usr/bin/python3
"""The Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class represents a review.

    Attributes:
        place_id (str): The Place id from Place Class.
        user_id (str): The User id from User Class.
        text (str): The review text.
    """

    place_id = ""
    user_id = ""
    text = ""

