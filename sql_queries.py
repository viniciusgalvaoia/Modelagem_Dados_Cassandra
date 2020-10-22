# Drop Tables

session_activity_table_drop = "DROP TABLE IF EXISTS session_activity"
user_activity_table_drop = "DROP TABLE IF EXISTS user_activity"
song_event_table_drop = "DROP TABLE IF EXISTS song_event"

# Create Tables

session_activity_table_create = """
        CREATE TABLE  IF NOT EXISTS session_activity (
            sessionId INT,
            itemInSession INT,
            artist TEXT,
            song TEXT, 
            length FLOAT,
            PRIMARY KEY (sessionId, itemInSession)
        );
    """

user_activity_table_create = """
        CREATE TABLE IF NOT EXISTS user_activity (
            userId INT,
            sessionId INT,
            itemInSession INT,
            artist TEXT,
            song TEXT,
            firstname TEXT,
            lastname TEXT,
            PRIMARY KEY ((userId, sessionId), itemInSession)
        );
    """

song_event_table_create = """
        CREATE TABLE  IF NOT EXISTS song_event (
            song TEXT,
            firstname TEXT,
            lastname TEXT,
            PRIMARY KEY (song)
        );
    """

# Insert Records

session_activity_table_insert = "INSERT INTO session_activity (sessionId, itemInSession, artist, song, length) \
                                 VALUES (%s, %s, %s, %s, %s)"

user_activity_table_insert = "INSERT INTO user_activity (userId, sessionId, itemInSession, artist, song, firstname, lastname) \
                              VALUES (%s, %s, %s, %s, %s, %s, %s)"

song_event_table_insert = "INSERT INTO song_event (song, firstname, lastname) \
                           VALUES (%s, %s, %s)"


# QUERY LISTS

create_table_queries = [session_activity_table_create, user_activity_table_create, song_event_table_create]
drop_table_queries = [session_activity_table_drop, user_activity_table_drop, song_event_table_drop]
