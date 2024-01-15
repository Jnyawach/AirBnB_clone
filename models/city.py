#!/usr/bin/python3
"""Define City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class represents a city.

    Attributes:
        state_id (str): The state/country id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

