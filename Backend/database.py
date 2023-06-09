
from model import Todo

# MongoDB driver for asynchronous Python applications.
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb: //localhost:27017')

# create a database
database = client.TodoList

# create a collection/ table
collection = database.todo
