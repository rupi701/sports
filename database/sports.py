from sqlalchemy import Column, Integer, String, Float
from database.database import Base

class Sport(Base):
    __tablename__="sports"
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String, index=True)
    Game = Column(String, nullable=True)
    time = Column(Float)
    Category = Column(Float)


