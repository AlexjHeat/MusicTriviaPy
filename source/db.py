# This Python file uses the following encoding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
import datetime
from config import DEFAULT_CATEGORY as default

#initialize Base & Session objects
Base = declarative_base()
engine = create_engine('sqlite:///musictrivia.db', echo=False)
Session = sessionmaker(bind=engine, expire_on_commit=False)


#create association table for category/song many-to-many relationship
category_song_association = Table(
    "song_category",
    Base.metadata,
    Column('song_id', Integer, ForeignKey('song.id')),
    Column('category_id', Integer, ForeignKey('category.id')),
    UniqueConstraint('song_id', 'category_id')
)

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description:                Mapped[str] = mapped_column(nullable=True)
    nameColor:                  Mapped[str] = mapped_column(nullable=True)
    backgroundColor:            Mapped[str] = mapped_column(nullable=True)
    clockColor:                 Mapped[str] = mapped_column(nullable=True)
    nameFont:                   Mapped[str] = mapped_column(nullable=True)
    clockFont:                  Mapped[str] = mapped_column(nullable=True)
    clockImage:                 Mapped[str] = mapped_column(nullable=True)
    countdownBackgroundImage:   Mapped[str] = mapped_column(nullable=True)
    videoBackgroundImage:       Mapped[str] = mapped_column(nullable=True)
    transitionBackgroundImage:  Mapped[str] = mapped_column(nullable=True)
    songs:                      Mapped[List['Song']] = relationship(secondary=category_song_association, back_populates='categories')

class Song(Base):
    __tablename__ = "song"
    id:             Mapped[int] = mapped_column(primary_key=True)
    fileName:       Mapped[str] = mapped_column(unique=True, nullable=False)
    missingFile:    Mapped[bool] = mapped_column(default=False)
    group:          Mapped[str] = mapped_column(nullable=True, default="")
    anime:          Mapped[str] = mapped_column(nullable=True, default="")
    op:             Mapped[bool] = mapped_column(nullable=True, default=True)
    opNum:          Mapped[int] = mapped_column(nullable=True, default=0)
    artist:         Mapped[str] = mapped_column(nullable=True, default="")
    title:          Mapped[str] = mapped_column(nullable=True, default="")
    startTime:      Mapped[int] = mapped_column(nullable=True, default=0)
    difficulty:     Mapped[int] = mapped_column(nullable=True, default=0)
    volume:         Mapped[int] = mapped_column(nullable=True, default=90)
    categories:     Mapped[List['Category']] = relationship(secondary=category_song_association, back_populates='songs')
    records:        Mapped[List['Record']] = relationship(back_populates='song')

    def __str__(self):
        str = ""
        if self.anime:
            str = self.anime
            if self.op:
                if self.opNum:
                    str += f' - OP{self.opNum}'
            else:
                if self.opNum:
                    str += f' - ED{self.opNum}'
            if self.title:
                str += f' - {self.title}'
        else:
            str = self.fileName
        return str

class Record(Base):
    __tablename__ = "record"
    id:         Mapped[int] = mapped_column(primary_key=True)
    date:       Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    total:      Mapped[int] = mapped_column(nullable=True)
    correct:    Mapped[int] = mapped_column(nullable=True)
    song:       Mapped['Song'] = relationship(back_populates='records')
    song_id:    Mapped[int] = mapped_column(ForeignKey('song.id'))


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
