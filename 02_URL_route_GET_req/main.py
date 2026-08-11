from fastapi import FastAPI

test = FastAPI()

# Home page
@test.get('/')
def home():
    return {"msg" : "Home Page!!"}

# About page
@test.get('/about/')
def about():
    return {"msg" : "About Page!!"}

# Users page
@test.get('/users/')
def users():
    return {
        "users" : [
            "Charan",
            "Tej",
            "Avvaru"
        ]
    }
