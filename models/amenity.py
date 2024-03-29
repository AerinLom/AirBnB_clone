#!/usr/bin/python3
"""Defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an Amenity.

    Args:
        name (str, optional): The name of the amenity. Defaults to "".
    """
    name = ""

    def __init__(self, **kwargs):
        """Starts a new Amenity instance."""
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")
