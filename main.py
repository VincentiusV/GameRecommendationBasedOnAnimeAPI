from fastapi import FastAPI, HTTPException, Depends, Request,status
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
from models.hashing import Hash
from models.jwttoken import create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
# from fastapi.middleware.cors import CORSMiddleware
import models.model as model
from models.model import User
from routes.gameRoutes import game_router
# from typing import Optional
from database.database import user_db

app = FastAPI()

@app.get("/", tags=["Root"])
async def welcome_text():
	return {"Selamat datang di Game API, silakan login untuk dapat mengakses API ini"}

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.post('/register', tags=["User"])
def create_user(request:User):
	hashed_pass = Hash.bcrypt(request.password)
	user_object = dict(request)
	user_object["password"] = hashed_pass
	user_id = user_db["users"].insert_one(user_object)
	# print(user)
	return {"User":"created"}

@app.post('/login', tags=["User"])
def login(request:OAuth2PasswordRequestForm = Depends()):
	user = user_db["users"].find_one({"username":request.username})
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
	if not Hash.verify(user["password"],request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
	access_token = create_access_token(data={"sub": user["username"] })
	return {"access_token": access_token, "token_type": "bearer"}

# @app.get("/tes")
# def read_root(current_user:model.User = Depends(get_current_user)):
# 	return {"data":"Ini udh terautentikasi"}

app.include_router(game_router, tags=['Games'], prefix='/games')

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)