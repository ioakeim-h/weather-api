import os
import sqlite3
import pandas as pd

def connect_to_sql(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return conn, cursor

def createSQL_locations_forecasts(cursor, queries_dir):
    print("Building SQL tables")
    locations_path = os.path.join(queries_dir, "create_locations.txt")
    forecasts_path = os.path.join(queries_dir, "create_forecasts.txt")

    with open(locations_path, "r") as file:
        locations_query = file.read()
    with open(forecasts_path, "r") as file:
        forecasts_query = file.read()
    cursor.execute(locations_query)
    cursor.execute(forecasts_query)
    
def updateSQL_locations_forecasts(cursor, locations, forecasts_dir):
    print("Loading data to SQL")
    cursor.executemany("INSERT OR IGNORE INTO locations (id, name, latitude, longitude) VALUES (?, ?, ?, ?)", locations.values.tolist())

    for filename in os.listdir(forecasts_dir):
        if filename.endswith(".csv"):
            
            file_path = os.path.join(forecasts_dir, filename)
            forecasts = pd.read_csv(file_path)
            cursor.executemany("INSERT OR IGNORE INTO forecasts (location_id, date, temperature) VALUES (?, ?, ?)", forecasts.values.tolist())







