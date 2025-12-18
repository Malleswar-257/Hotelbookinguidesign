from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
def get_db():
    db = Database(Settings().DATABASE_URL)
    yield db
def create_tables(db: Database):
    await db.execute(users_table.create()
    await db.execute(hotels_table.create()
    await db.execute(rooms_table.create()
    await db.execute(bookings_table.create()
class User:
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    email = Column(String, unique = True, index = True)
    password = Column(String)
    role = Column(String)
class Hotel:
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    city = Column(String, index = True)
description = Column(String)
rating = Column(Float)
class Room:
    id = Column(Integer, primary_key = True, index = True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
type = Column(String)
price = Column(Float)
capacity = Column(Integer)
availability_count = Column(Integer)
class Booking:
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
room_id = Column(Integer, ForeignKey("rooms.id"))
check_in = Column(DateTime)
check_out = Column(DateTime)
price = Column(Float)
status = Column(String)
))))