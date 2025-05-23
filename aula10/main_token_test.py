from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": "teste_token", "token_type": "bearer"}
