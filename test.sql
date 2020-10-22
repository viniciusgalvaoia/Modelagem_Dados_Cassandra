-- Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4

SELECT artist, song, length 
FROM session_activity 
WHERE sessionId = 338 
AND itemInSession = 4
;

-- Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

SELECT artist, song, firstname, lastname 
FROM user_activity 
WHERE userId = 10 
AND sessionId = 182
;


-- Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

SELECT firstname, lastname 
FROM song_event 
WHERE song='All Hands Against His Own'
;