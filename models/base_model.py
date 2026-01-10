#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    """ this is the parent class that handles id create timestamp"""

    def __init__(self, *args, **kwargs):
        """initalize the base model"""

        if kwargs:
            for key, value in kwargs.items():
             if key != "__class__":
                if key == "created_at" or key == "updated_at":
                   value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        
    def __str__(self):
        """returns the string representation of the BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
       
       self.updated_at = datetime.now()
       models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()    
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
    
    