# from models.jwttoken import create_access_token, get_current_user
# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi import APIRouter, HTTPException, Depends, Request,status
# # from fastapi.middleware.cors import CORSMiddleware
# from models.hashing import Hash
# from models.model import (User, Login, Token, TokenData)
# from database.database import user_db

# user_router = APIRouter()

# @user_router.post('/register')
# def create_user(request:User):
# 	hashed_pass = Hash.bcrypt(request.password)
# 	user_object = dict(request)
# 	user_object["password"] = hashed_pass
# 	user_id = user_db["users"].insert_one(user_object)
# 	# print(user)
# 	return {"User":"created"}

# @user_router.post('/login')
# def login(request:OAuth2PasswordRequestForm = Depends()):
# 	user = user_db["users"].find_one({"username":request.username})
# 	if not user:
# 		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
# 	if not Hash.verify(user["password"],request.password):
# 		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
# 	access_token = create_access_token(data={"sub": user["username"] })
# 	return {"access_token": access_token, "token_type": "bearer"}