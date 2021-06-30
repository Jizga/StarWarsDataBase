import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    password = Column(String, nullable=False)
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(10))
    skin_color = Column(String(10))
    eye_color = Column(String(10))
    birth_year = Column(String(250))
    gender = Column(String(6))
    created = Column(DateTime)
    edited = Column(DateTime)
    name = Column(String(250))
    homeworld = Column(String(250))
    url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(String(20))
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Integer)
    created = Column(DateTime)
    name = Column(String(250))
    url = Column(String(250))

class FavoriteCharacters(Base):
    __tablename__ = 'favoriteCharacters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

    def to_dict(self):
        return {}

class FavoritePlanets(Base):
    __tablename__ = 'favoritePlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')