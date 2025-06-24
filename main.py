
import os
import pytz
import pandas as pd
from datetime import datetime

from utils import prepare_export_dir, get_forecast_data, build_forecasts_dataframe
from sql_operations import connect_to_sql, createSQL_locations_forecasts, updateSQL_locations_forecasts

username = "..." # Too lazy to add these as system variables :/
password = "..."

export_dir = "./Exports"
queries_dir = "./Queries"
database = "./weather_forecasts.db"

athens = pytz.timezone("Europe/Athens")
start_date = datetime(2024, 11, 7, tzinfo=athens).strftime("%Y-%m-%dT00:00:00Z")
end_date = datetime(2024, 11, 14, tzinfo=athens).strftime("%Y-%m-%dT00:00:00Z")

locations = pd.DataFrame({
    "id": [1,2,3],
    "name": ["Marathonas","Chalandri","Kallimarmaro"],
    "latitude": [38.155258,38.0214,37.9681],
    "longitude": [23.960960,23.7988,23.7416]
})

def main():
    prepare_export_dir(export_dir)
    conn, cursor = connect_to_sql(database)

    for row in locations.itertuples(index=False):
        if data := get_forecast_data(row.name, row.latitude, row.longitude, start_date, end_date, username, password):
            
            df = build_forecasts_dataframe(data, row.name, row.id)
            if not df.empty:
                export_path = os.path.join(export_dir, f"{row.name}.csv")
                df.to_csv(export_path, index=False)
        
    createSQL_locations_forecasts(cursor, queries_dir)
    updateSQL_locations_forecasts(cursor, locations, export_dir)

    conn.commit()
    conn.close()
    print("All processes completed successfully!")


if __name__ == "__main__":
    main()
