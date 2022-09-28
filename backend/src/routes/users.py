from email.policy import default
from fastapi import APIRouter

user = APIRouter()

@user.get('/users/{name}')
async def user_get(name: str):
    return {f"Hello, {name}"}

@user.get('/users/{name}/{salary}')
async def user_salary(name: str, salary: float):
    return {f"Hello {name} your salary is {salary}"}