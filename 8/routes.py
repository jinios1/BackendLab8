from fastapi import APIRouter, Query, Form, Header, Cookie
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse
from models import User, RegisterRequest
from typing import Optional, List

router = APIRouter()

@router.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@router.get("/search")
def search(query: str = Query(...)):
    return {"message": f"You searched for: {query}"}

@router.get("/json")
def get_json():
    return {"name": "Your Name", "age": 25, "hobbies": ["coding", "reading", "gaming"]}

@router.get("/file")
def get_file():
    file_path = "example.txt"
    with open(file_path, "w") as f:
        f.write("ALBEBRA.")
    return FileResponse(file_path, media_type="text/plain", filename="example.txt")

@router.get("/redirect")
def redirect():
    return RedirectResponse(url="/")

@router.get("/headers")
def get_headers(headers: dict = Header(...)):
    return {"headers": headers}

@router.get("/set-cookie")
def set_cookie(response: JSONResponse, username: str = "default_name"):
    response = JSONResponse(content={"message": "Cookie set"})
    response.set_cookie(key="username", value=username)
    return response

@router.get("/get-cookie")
def get_cookie(username: Optional[str] = Cookie(None)):
    if username:
        return {"username": username}
    return {"message": "No cookie found"}

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"message": f"Welcome, {username}!"}

@router.post("/register")
def register(user: RegisterRequest):
    return {"message": f"User {user.username} registered successfully!"}

users = [
    User(id=1, username="ANDREY", email="ANDREY@gmail.com", password="123"),
    User(id=2, username="ADRENALIN", email="ADRENALIN@yandex.ru", password="123"),
]

@router.get("/users", response_model=List[User])
def get_users():
    return users

@router.get("/users/{id}", response_model=User)
def get_user_by_id(id: int):
    user = next((user for user in users if user.id == id), None)
    if user:
        return user
    return JSONResponse(content={"error": "User not found"}, status_code=404)
