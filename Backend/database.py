
from model import Todo

# MongoDB driver for asynchronous Python applications.
# motor -> helps to connect database.py file with mongodb database
# find(), find_one(), insert_one() are mongodb methods.
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb: //localhost:27017')

# create a database
database = client.TodoList

# create a collection/ table
collection = database.todo


async def fetchOneTodo(title):
    document = await collection.find_one({"title": title})
    return document

# ** -> Used when we need to extract the key-value pairs of the dictionary and assign them to variables
# Key -> Argument name
# Value -> Argument value
# Example: document = {'title': 'Task 1', 'completed': False}
#          Todo(**document) = >  Todo(title='Task 1', completed=False)


async def fetchAllTodos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def createTodo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result


async def updateTodo(title, description):
    await collection.update_one({"title": title}, {"$set": {"description": description}})
    document = await collection.find_one({"title": title})
    return document


async def removeTodo(title):
    await collection.delete_one({"title": title})
    return True
