from fastapi import FastAPI, HTTPException, Depends, status
from models.hashing import Hash
from models.jwttoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from models.model import User
from routes.gameRoutes import game_router
from routes.ganimeRoutes import ganime_router
from routes.gameSpecsRoutes import gamespecs_router
from database.database import user_db
import uvicorn

app = FastAPI(title="Game API", description="Dalam API ini, Anda dapat melihat berbagai jenis game serta mendapat rekomendasi game berdasarkan Anime favorit Anda")

@app.get("/", tags=["Root"])
async def welcome_text():
	return {"Selamat datang di Game API, silakan login untuk dapat mengakses API ini"}


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

app.include_router(game_router, tags=['Games'], prefix='/games')
app.include_router(ganime_router, tags=['Game Recommendation Based on Anime'], prefix='/game-anime-recommendation')
app.include_router(gamespecs_router, tags=['Games Spec and PC Part Recommendation'], prefix='/game-specs')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)