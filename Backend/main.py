from database import *
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Instantiating fastapi class by creating an object called "app"
app = FastAPI()

# To connect with react server
origins = ["https://localhost:3000"]

# Adding middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def readRoot():
    return {"Ping": "Pong"}


@app.get("/api/todo")
async def getTodo():
    response = await fetchAllTodos()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def getTodoById(title):
    response = await fetchOneTodo(title)
    if response:
        return response
    raise HTTPException(404, "There is no todo item with this title {title}")


@app.post("/api/todo", response_model=Todo)
async def postTodo(todo: Todo):
    # converting "todo" json to dictionary
    response = await createTodo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad request")


@app.put("/api/todo{title}/", response_model=Todo)
async def putTodo(title: str, description: str):
    response = await updateTodo(title, description)
    if response:
        return response
    raise HTTPException(404, f"There is no Todo item with this title {title}")


@app.delete("/api/todo{title}")
async def deleteTodo(title: str):
    response = await removeTodo(title)
    if response:
        return "Successfully deleted Todo item"
    raise HTTPException(404, f"There is no Todo item with this title {title}")
