# Project: Data Modeling with Postgres

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Project Description
In this project, We will create a Postgres database and build an ETL pipeline using Python to load the JSON data into the postgres database. 

## Data Model
### Fact Table
1. **songplays** - records in log data associated with song plays i.e. records with page NextSong
       * songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
### Dimension Tables
2. **users** - users in the app
       * user_id, first_name, last_name, gender, level
3. **songs** - songs in music database
       * song_id, title, artist_id, year, duration
4. **artists** - artists in music database
       * artist_id, name, location, latitude, longitude
5. **time** - timestamps of records in songplays broken down into specific units
       * start_time, hour, day, week, month, year, weekday

## Key Project Files
This project has three important python files.
1. sql_queries.py - All the sql queries used across this project are stored in this python file.
2. create_tables.py - Python code required to create the sparkify database and tables.
3. etl.py - Python code required to perform the ETL process and load the data in JSON files to Sparkify database.

## Steps to Run the Project
**Step 1:** Run the file create_tables.py. This file will create the database and tables required for this data model. 
**Step 2:** Run the file etl.py. This file will read the data from all the JSON files and load the data into database.
