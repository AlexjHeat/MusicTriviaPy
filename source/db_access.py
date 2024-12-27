# This Python file uses the following encoding: utf-8
from source.db import Session, Song, Category, Record
from config import DEFAULT_CATEGORY

#   ~~~CATEGORIES<->SONGS~~~
def getSongsInCategory(id: int) -> [Song]:
    session = Session()
    songs = session.query(Song).filter(Song.categories.any(Category.id == id), Song.missingFile == False).all()
    session.close()
    return songs

def getSongsOutOfCategory(id: int) -> [Song]:
    session = Session()
    songs = session.query(Song).filter(~Song.categories.any(Category.id == id), Song.missingFile == False).all()
    session.close()
    return songs

def addSongToCategory(cat_id: int, song_id: int):
    session = Session()
    cat = session.query(Category).filter(Category.id == cat_id).one()
    song = session.query(Song).filter(Song.id == song_id).one()
    cat.songs.append(song)
    session.commit()
    session.close()

def removeSongFromCategory(cat_id: int, song_id: int):
    session = Session()
    cat = session.query(Category).filter(Category.id == cat_id).one()
    song = session.query(Song).filter(Song.id == song_id).one()
    cat.songs.remove(song)
    session.commit()
    session.close()

#   ~~~CATEGORIES~~~
def getCategories() -> [Category]:
    session = Session()
    categories = session.query(Category).all()
    session.close()
    return categories

def addCategory(cat: Category):
    session = Session()
    session.add(cat)
    session.commit()
    session.close()

def updateCategory(id: int, data: Category) -> Category:
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

def deleteCategory(id: int):
    session = Session()
    cat = session.query(Category).filter(Category.id == id).one()
    session.delete(cat)
    session.commit()

#   ~~~SONGS~~~
def verifySongFiles(song_files: [str]):
    session = Session()
    song_db = session.query(Song).all()
    for song in song_db:
        if song.fileName in song_files:
            song.missingFile = False
        else:
            song.missingFile = True
    session.commit()
    session.close()


def addSongsFromFile(song_files: [str]):
    session = Session()
    default_cat = session.query(Category).filter(Category.name == DEFAULT_CATEGORY).one()
    for file in song_files:
        if session.query(Song).filter(Song.fileName == file).first() is None:
            song = Song(fileName=file)
            song.categories.append(default_cat)
            session.add(song)
    session.commit()
    session.close()


def updateSong(id: int, data: Song):
        session = Session()
        song = session.query(Song).filter(Song.id == id).one()
        song.group = data.group
        song.anime = data.anime
        song.op = data.op
        song.opNum = data.opNum
        song.title = data.title
        song.artist = data.artist
        song.startTime = data.startTime
        song.difficulty = data.difficulty
        session.commit()
        session.close()
        return song

def updateGroup(oldName: str, newName: str):
    session = Session()
    songs = session.query(Song).filter(Song.group == oldName).all()
    for song in songs:
        song.group = newName
        session.commit()
    session.close()

#   ~~~RECORDS~~~
def createRecord(record: Record):
    session = Session()
    session.add(record)
    session.commit()
    session.close()
