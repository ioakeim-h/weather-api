import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

queries_dir = "./Queries"
locations_path = os.path.join(queries_dir, "locations.txt")
latest_forecast_path = os.path.join(queries_dir, "latest_forecast.txt")
top_locations_path = os.path.join(queries_dir, "top_locations.txt")

with open(locations_path, "r") as file:
    locations_query = file.read()
with open(latest_forecast_path, "r") as file:
    latest_forecast_query = file.read()
with open(top_locations_path, "r") as file:
    top_locations_query = file.read()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(os.getcwd(), 'weather_forecasts.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Weather Forecast API!"}), 200

# List locations
@app.route("/locations", methods=["GET"])
def list_locations():
    locations = db.session.execute(text(locations_query)).fetchall()
    return jsonify([loc[0] for loc in locations]), 200 

# Latest forecast per location per day
@app.route("/latest_forecast", methods=["GET"])
def latest_forecast():
    latest_forecasts = db.session.execute(text(latest_forecast_query)).fetchall()
    return jsonify([{ "date": row[0], "temperature": row[1], "location": row[2] } for row in latest_forecasts]), 200 

# Top n locations
@app.route("/top_locations", methods=["GET"])
def top_locations():
    n = request.args.get("n", default=3, type=int)
    top_locations = db.session.execute(text(top_locations_query), {"n": n}).fetchall()
    return jsonify([{ "average_temperature": row[0], "location": row[1]  } for row in top_locations]), 200

def run_api():
    app.run(debug=True)

if __name__ == "__main__":
    run_api()
