# To autocreate json schemas from model
# pydantic -> used for data parsing and validation.
# BaseModel -> It acts as the base class for creating user defined models.
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
