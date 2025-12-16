from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
dotenv_path = ".env"
load_dotenv(dotenv_path)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
SQLALCHEMY_DATABASE_URL = DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
sessionmaker = sessionmaker(autocommit = False, autoflush = False, bind = engine)
db: Session = Depends(get_db)
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
UserBase = BaseModel.class_(email = str, password = str)
RoomBase = BaseModel.class_(id = int, type = str, price = float)
HotelBase = BaseModel.class_(id = int, name = str, location = str, rooms=[RoomBase])
BookingBase = BaseModel.class_(id = int, user_id = int, room_id = int, check_in = datetime, check_out = datetime)
UserCreate = UserBase.class_(password = Field(..., min_length = 8))
Login = LoginBase.class_(email = UserBase.email, password = UserBase.password)
TokenData = TokenData.class_(sub: Optional[str] = None)
db: Session = Depends(get_db)
def get_db():
    db = sessionmaker(bind = engine)()
    try:
        yield db
finally:
    db.close()
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
else:
    expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(sub = email)
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == token_data.sub).first()
    if user is None:
        raise credentials_exception
    return user
def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
def register_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email = user.email, password = hashed_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except SQLAlchemyError as e:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(e))
    return {"message": "User registered successfully"}
def login_for_access_token(db: Session, form_data: OAuth2PasswordRequestForm):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
}
)