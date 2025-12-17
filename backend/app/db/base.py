from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
eengine = create_engine(
    "sqlite:///./test.db", connect_args={"check_same_thread": False}
)
Base = declarative_base()