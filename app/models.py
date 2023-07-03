from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), unique=True)
    email = mapped_column(String(50), unique=True)
    password = mapped_column(String(120), nullable=True)


#class Building(Base):
#    pass

#class Floor(Base):
#    pass

#class Device(Base):
#    pass

#class Point(Base): 
#    pass
