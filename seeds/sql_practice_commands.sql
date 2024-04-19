
SELECT albums.id AS album_id, title 
	FROM albums
	JOIN artists
	ON albums.artist_id = artists.id
	WHERE artists.name = 'Nina Simone'
	AND albums.release_year > 1975;

