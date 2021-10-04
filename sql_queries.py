# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGPLAYS(
        songplay_id SERIAL PRIMARY KEY, 
        start_time TIMESTAMP NOT NULL, 
        user_id INT NOT NULL, 
        level VARCHAR(10), 
        song_id VARCHAR(25), 
        artist_id VARCHAR(25), 
        session_id INT NOT NULL, 
        location VARCHAR(100), 
        user_agent VARCHAR(150))
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS USERS(
        user_id INT PRIMARY KEY, 
        first_name VARCHAR(50), 
        last_name VARCHAR(50), 
        gender VARCHAR(1), 
        level VARCHAR(10))
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS(
        song_id VARCHAR(25) PRIMARY KEY, 
        title VARCHAR(100) NOT NULL, 
        artist_id VARCHAR(25), 
        year INT, 
        duration NUMERIC CHECK(duration > 0))
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS ARTISTS(
        artist_id VARCHAR(25) PRIMARY KEY, 
        name VARCHAR(100) NOT NULL, 
        location VARCHAR(100), 
        latitude FLOAT(5), 
        longitude FLOAT(5))
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS TIME(
        start_time TIMESTAMP PRIMARY KEY,
        hour INTEGER,
        day INTEGER,
        week INTEGER,
        month INTEGER,
        year INTEGER,
        weekday INTEGER)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

user_table_insert = ("""INSERT INTO USERS (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO SONGS (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""INSERT INTO ARTISTS (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")


time_table_insert = ("""INSERT INTO TIME (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    select 
        s.song_id,
        s.artist_id
    from
        songs s
    inner join
        artists a
    on
        s.artist_id = a.artist_id
    where
        s.title = %s
        and a.name= %s
        and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]