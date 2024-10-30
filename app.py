from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import mysql.connector

app = FastAPI()

# Подключение к базе данных
def get_connection():
    return mysql.connector.connect(
        host="junction.proxy.rlwy.net",
        user="root",
        password="aMtDZhaZeuBWVLjDSormcYrDsgmJuaEy",
        database="HTP_1",
        port="25232"
    )

# Модель запроса на логин
class LoginRequest(BaseModel):
    username: str
    password: str

# Эндпоинт для аутентификации
@app.post("/login")
def login(request: LoginRequest):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                   (request.username, request.password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user:
        return {"username": user["username"], "role": user["role"]}
    else:
        raise HTTPException(status_code=401, detail="Неверные логин или пароль")
