from fastapi import APIRouter
from . import users, login

api_router = APIRouter()
endpoints = [users, login]

for endpoint in endpoints:
    api_router.include_router(endpoint.router)
