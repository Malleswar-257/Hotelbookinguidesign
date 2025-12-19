from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
echo = True if database_url.startswith('sqlite') else False
engine = create_engine(
    database_url,
    connect_args={'check_same_thread': False} if database_url.startswith('sqlite') else {},
    echo = echo,
)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()
def create_tables(engine):
    Base.metadata.create_all(bind = engine)