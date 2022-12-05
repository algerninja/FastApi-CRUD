from pydantic import BaseModel, EmailStr, Field
import re


class LoginItem(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@example.com",
                "password": "P4ssW0Rd.",
            }
        }


class SingUpItem(BaseModel):
    email: EmailStr
    firstname: str = Field(regex="^[a-zA-Z]+$")
    lastname: str = Field(regex="^[a-zA-Z]+$")
    password: str = Field(min_length=8)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@example.com",
                "firstname": "joe",
                "lastname": "Smith",
                "password": "P4ssW0Rd.",
            }
        }
