from sqlalchemy import create_engine, ForeignKey, Boolean, String, Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from main import db


class User(db.Model):
    __tablename__ = "user"
    Id = Column("Id", Integer, primary_key=True, autoincrement=True)
    Name = Column("Name", String(50))
    Nationality = Column("Nationality", String(30))
    def __init__(self, Name, Nationality):
        self.Name = Name
        self.Nationality = Nationality

    def __repr__(self):
        return f"Name : {self.Name}\n Id: {self.Id}\n Nationality: {self.Nationality}\n"
