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
    raise HTTPException("404", "There is no todo item with this title {title}")


@app.post("/api/todo")
async def postTodo(todo):
    return 1


@app.put("/api/todo{id}")
async def putTodo(id, data):
    return 1


@app.delete("/api/todo{id}")
async def deleteTodo(id):
    return 1
