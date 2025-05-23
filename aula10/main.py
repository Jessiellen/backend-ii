from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Form



app = FastAPI()

SECRET_KEY = "segredo-super-seguro"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_user = {
    "username": "admin",
    "hashed_password": "$2b$12$VNslH0Ov23C2w0BdnwXzseLB7z8LZJ0zZ43RxRbnYiQDU6CWZJZx2"  # senha: 1234
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    if username != fake_user["username"]:
        return False
    if not verify_password(password, fake_user["hashed_password"]):
        return False
    return {"username": username}

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/token")
async def login(username: str = Form(...), password: str = Form(...)):
    print(f"Recebido username={username}, password={password}")
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
async def root():
    return {"message": "API está rodando"}

