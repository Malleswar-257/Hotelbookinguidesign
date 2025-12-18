from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()

@app.post("/register", response_model=schemas.User)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db = db, user = user)

@app.get("/login", response_model=schemas.User)
async def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email = email)
    if not user or not crud.verify_password(password, user.password):
        raise HTTPException(status_code=404, detail="User not found")
    return user