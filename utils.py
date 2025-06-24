import os
import requests
import pandas as pd
from io import StringIO

def prepare_export_dir(export_dir):
    print("Preparing export directory")
    if os.path.exists(export_dir):
        # Empty dir: reduces potential for error
        for filename in os.listdir(export_dir):
            if filename.endswith(".csv"):
                file_path = os.path.join(export_dir, filename)
                os.remove(file_path)
    else: 
        os.makedirs(export_dir)
        
def get_forecast_data(name, lat, lng, start_date, end_date,  username, password):
    print(f"Fetching data for {name}")
    url = f"https://api.meteomatics.com/{start_date}--{end_date}:PT1H/t_2m:C/{lat},{lng}/csv"
    
    response_text = None
    try:
        response = requests.get(url, auth=(username, password))
        response.raise_for_status()
        response_text = response.text
    except Exception as e:
        print(f"An error occurred for location {name}: {e}\n{name} was skipped...")
    return response_text

def build_forecasts_dataframe(data, name, location_id):
    df = pd.read_csv(StringIO(data))

    # Check for empty data: 'validdate;t_2m:C' contains all info
    if ("validdate;t_2m:C" not in df.columns) or (len(df) == 0):
        print(f"No data obtained for {name}")
        return pd.DataFrame()

    df["location_id"] = location_id
    df[["date", "temperature"]] = df["validdate;t_2m:C"].str.split(";", expand=True)
    df["date"] = pd.to_datetime(df["date"])
    df = df.drop(columns=["validdate;t_2m:C"])
    return df