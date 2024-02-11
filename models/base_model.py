#!/usr/bin/python3
"""define the imported modules"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """this is the base class"""

    def __init__(self) -> None:
        """initializing function"""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self) -> str:
        """prints [<class name>] (<self.id>) <self.__dict__>"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
