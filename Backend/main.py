from fastapi import FastAPI
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
    return 1


@app.get("/api/todo{id}")
async def getTodoById(id):
    return 1


@app.post("/api/todo")
async def postTodo(todo):
    return 1


@app.put("/api/todo{id}")
async def putTodo(id, data):
    return 1


@app.delete("/api/todo{id}")
async def deleteTodo(id):
    return 1
