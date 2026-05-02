
This project is a Weather Data Pipeline and REST API that automates the collection, processing, and sharing of local weather forecasts. It uses the Meteomatics API to fetch weather data for locations in Greece, including Marathonas, Chalandri, and Kallimarmaro. The data is cleaned, organized into Pandas DataFrames, converted to the Europe/Athens timezone, and stored both as CSV files and in a central SQLite database.

The project also includes a Flask API that gives access to the processed data through different endpoints. Users can view monitored locations, get the latest hourly temperature forecasts, and compare locations based on average temperatures.

Usage:
- To build the database and obtain the data, execute the command: python main.py
- To run the API
	- Execute the command python api.py
	- In your browser, access localhost
- To get the desired data from the API, you can use the following endpoints: 
	- List locations: /locations 
	- Latest forecast per location per day: /latest_forecast
	- Top n locations (n varies from 1 to 3): /top_locations?n=3 



