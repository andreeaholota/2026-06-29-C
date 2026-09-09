from database.DB_connect import DBConnect
from model.Artist import Artist


class DAO():

    @staticmethod
    def getAllArtists():
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
            SELECT DISTINCT ar.ArtistId AS id, ar.Name AS name
            FROM artist ar, album al, track t 
            WHERE ar.artistId = al.ArtistId
                AND al.AlbumId = t.AlbumId
        """

        cursor.execute(query)
        for row in cursor:
            results.append(Artist(row["id"], row["name"]))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllTracks(artistId):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
            SELECT t.TrackId AS id, t.Name AS name
            FROM track t, album al 
            WHERE t.AlbumID = al.AlbumId
                AND al.ArtistId = %s
        """

        cursor.execute(query, (artistId,))

        for row in cursor:
            results.append(row["name"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllPlaylists(artistId):
        conn = DBConnect.get_connection()
        results = set()

        cursor = conn.cursor(dictionary=True)
        query = """ 
            SELECT p.PlaylistId AS id, p.Name AS name
            FROM album al, track t, playlisttrack pt, playlist p
            WHERE p.PlaylistId = pt.PlaylistId
                AND pt.TrackId = t.TrackId
                AND t.AlbumId = al.AlbumId
                AND al.ArtistId = %s
        """

        cursor.execute(query, (artistId,))

        for row in cursor:
            results.add(row["id"])

        cursor.close()
        conn.close()
        return results

