#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Class represents a state/country.

    Attributes:
        name (str): Country or state name.
    """

    name = ""

