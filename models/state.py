#!/user/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    # class attributes
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
