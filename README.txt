
This project automates the collection, processing, and storage of weather forecast data for specified locations. It retrieves forecast data using API calls, transforms it into structured dataframes, exports the results as CSV files, and updates a local SQLite database with the latest information.

- To build the database and obtain the data, execute the command: python main.py
- To run the API
	- Execute the command python api.py
	- In your browser, access localhost
- To get the desired data from the API, you can use the following endpoints: 
	- List locations: /locations 
	- Latest forecast per location per day: /latest_forecast
	- Top n locations (n varies from 1 to 3): /top_locations?n=3 



