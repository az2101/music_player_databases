from lib.album import *

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, album_id):
        row = self._connection.execute('SELECT * from albums WHERE id = %s', (album_id,))
        row = row[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    

    