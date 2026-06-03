from fastapi import FastAPI
from calculator import add, multiply


app=FastAPI()

@app.get("/")
def home():
    return {
        "result": add(2, 3)
    }

@app.get("/multiply")
def mult():
    return {
        "result": multiply(4, 5)
    }