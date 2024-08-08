# This Python file uses the following encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint, Integer, String
from sqlalchemy.orm import relationship
from config import defaultCategory

#initialize Base & Session objects
Base = declarative_base()
engine = create_engine('sqlite:///musictrivia.db', echo=False)
Session = sessionmaker(bind=engine, expire_on_commit=False)


#create association table for category/song many-to-many relationship
category_song_association = Table(
    "song_category",
    Base.metadata,
    Column('song_id', Integer, ForeignKey('Songs.id')),
    Column('category_name', Integer, ForeignKey('Categories.name')),
    UniqueConstraint('song_id', 'category_name')
)

class Category(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    songs = relationship('Song', secondary=category_song_association, back_populates='categories')

class Song(Base):
    __tablename__ = "Songs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fileName = Column(String, unique=True, nullable=False)
    anime = Column(String)
    opNum = Column(Integer, default=0)
    artist = Column(String)
    title = Column(String)
    startTime = Column(Integer)
    categories = relationship('Category', secondary=category_song_association, back_populates='songs')

    def __str__(self):
        str = ""
        if self.anime:
            str = str + self.anime
            if self.title:
                str = str + " - " + self.title
        else:
            str = self.fileName
        return str

class FilePath(Base):
    __tablename__ = "FilePaths"
    path = Column(String, primary_key=True)

def createTables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    createDefaultCategory()

def createDefaultCategory():
    session = Session()
    cat = Category(name=defaultCategory, description='All songs are added to this category by default.')
    #add all songs to category
    session.add(cat)
    session.commit()
