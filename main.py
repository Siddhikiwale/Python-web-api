from fastapi import FastAPI

app = FastAPI(
    title="Student API",
    description="Sample FastAPI with multiple endpoints",
    version="1.0.0"
)

# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }


# About Endpoint
@app.get("/about")
def about():
    return {
        "application": "FastAPI Demo",
        "developer": "Siddhi"
    }


# Student Endpoint
@app.get("/student")
def get_student():
    return {
        "id": 101,
        "name": "Rahul",
        "course": "Python"
    }


# Weather Endpoint
@app.get("/weather")
def weather(city: str):
    return {
        "city": city,
        "temperature": "30°C",
        "condition": "Sunny"
    }


# Addition Endpoint
@app.get("/add")
def add(a: int, b: int):
    return {
        "number1": a,
        "number2": b,
        "sum": a + b
    }


# Multiplication Endpoint
@app.get("/multiply")
def multiply(a: int, b: int):
    return {
        "number1": a,
        "number2": b,
        "result": a * b
    }


# User Endpoint
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "status": "Active"
    }