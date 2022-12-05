from fastapi import APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from models.auth import LoginItem, SingUpItem
from fastapi.encoders import jsonable_encoder
from decouple import config
import jwt
import re

from config.db import conn

auth = APIRouter()

test_user = {
    "username": "temitope",
    "password": "temipassword",
}


@auth.post("/login")
async def user_login(loginitem: LoginItem):

    data = jsonable_encoder(loginitem)

    db_find = conn["authentication"].find_one({"email": data["email"]})
    print("➡ data :", data)

    if data["email"] == db_find["email"] and data["password"] == db_find["password"]:

        encoded_jwt = jwt.encode(data, config("SECRET_KEY"), algorithm=config("ALGORITHM"))
        return JSONResponse(status_code=status.HTTP_200_OK, content={"token": encoded_jwt})

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Login failed")


@auth.post("/singup")
async def user_singup(singupitem: SingUpItem):
    data = jsonable_encoder(singupitem)

    if not re.match("^[a-zA-Z]+$", data["firstname"]):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="First name contains invalid characters")

    if not re.match("^[a-zA-Z]+$", data["lastname"]):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Last name contains invalid characters")

    if len(data["password"]) <= 8:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Password must be at least 8 characters")

    user_id = conn["authentication"].insert_one(data).inserted_id

    return HTMLResponse(status_code=status.HTTP_204_NO_CONTENT)
