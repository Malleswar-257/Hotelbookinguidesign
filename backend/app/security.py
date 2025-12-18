from datetime import timedelta
from jose import JWTError, jwt
time_to_live = 15
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"\
ACCESS_TOKEN_EXPIRE_MINUTES = time_to_live\
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):    to_encode = data.copy()    if expires_delta:
    expire = datetime.utcnow() + expires_delta
else:
    expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt\
def verify_password(plain_password: str, hashed_password: str):    return pwd_context.verify(plain_password, hashed_password)\
def get_password_hash(password: str):    return pwd_context.hash(password)\
def authenticate_user(email: str, password: str, db: Session):    user = crud.get_user_by_email(email = email, db = db)    if not user or not verify_password(password, user.password):        return None    return user\

    pass  # TODO: Complete implementation