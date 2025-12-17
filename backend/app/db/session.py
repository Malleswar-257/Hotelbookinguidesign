from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
eengine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={
}
)