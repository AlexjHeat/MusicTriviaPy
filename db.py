# This Python file uses the following encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config import DEFAULT_CATEGORY as default

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
    nameColor = Column(String)
    backgroundColor = Column(String)
    clockColor = Column(String)
    nameFont = Column(String)
    clockFont = Column(String)
    clockImage = Column(String)
    countdownBackgroundImage = Column(String)
    videoBackgroundImage = Column(String)
    transitionBackgroundImage = Column(String)
    songs = relationship('Song', secondary=category_song_association, back_populates='categories')

class Song(Base):
    __tablename__ = "Songs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fileName = Column(String, unique=True, nullable=False)
    group = Column(String, default='')
    anime = Column(String, default='')
    opNum = Column(Integer, default=0)
    artist = Column(String, default='')
    title = Column(String, default='')
    startTime = Column(Integer)
    categories = relationship('Category', secondary=category_song_association, back_populates='songs')
    missingFile = Column(Boolean, default=False)

    def __str__(self):
        str = ""
        if self.anime:
            str = self.anime
            if self.opNum:
                str += f' - OP{self.opNum}'
            if self.title:
                str += f' - {self.title}'
        else:
            str = self.fileName
        return str


def updateSong(id, data):
        session = Session()
        song = session.query(Song).filter(Song.id == id).one()
        song.group = data.group
        song.anime = data.anime
        song.opNum = data.opNum
        song.title = data.title
        song.artist = data.artist
        song.startTime = data.startTime
        session.commit()
        session.close()
        return song

def updateCategory(id, data):
        session = Session()
        category = session.query(Category).filter(Category.id == id).one()
        category.name = data.name
        category.description = data.description
        category.nameColor = data.nameColor
        category.backgroundColor = data.backgroundColor
        category.clockColor = data.clockColor
        category.nameFont = data.nameFont
        category.clockFont = data.clockFont
        session.commit()
        session.expunge(category)
        session.close()
        return category

def createDefaultCategory():
    session = Session()
    cat = Category( name=default,
                    description='All songs are added to this category by default.'
                    )
    #add all songs to category
    session.add(cat)
    session.commit()

def createTables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    createDefaultCategory()
