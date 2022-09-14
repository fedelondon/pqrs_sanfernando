from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def user_get():
    return "Hello"