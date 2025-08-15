import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# ------------------------------
# File Paths
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")

# ------------------------------
# Load Models & Encoders
# ------------------------------
model = joblib.load(os.path.join(MODELS_DIR, "random_forest_planetheat.pkl"))
country_encoder = joblib.load(os.path.join(MODELS_DIR, "country_encoder.pkl"))
city_encoder = joblib.load(os.path.join(MODELS_DIR, "city_encoder.pkl"))

# ------------------------------
# Load CSV Files
# ------------------------------
location_df = pd.read_csv(os.path.join(DATA_DIR, "city_country_latlon.csv"))
historical_df = pd.read_csv(os.path.join(DATA_DIR, "GlobalLandTemperaturesByCity.csv"))

# ------------------------------
# Routes
# ------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    countries = sorted(location_df['Country'].unique())

    if request.method == "POST":
        country = request.form["country"]
        city = request.form["city"]
        date = request.form["date"]

        year, month, day = map(int, date.split("-"))

        # Get lat/lon for city
        location_row = location_df[(location_df['City'] == city) & (location_df['Country'] == country)]
        latitude = location_row.iloc[0]['Latitude']
        longitude = location_row.iloc[0]['Longitude']

        # Encode country & city
        country_code = country_encoder.transform([country])[0]
        city_code = city_encoder.transform([city])[0]

        # Prepare input for model
        input_data = pd.DataFrame([{
            "year": year,
            "month": month,
            "day": day,
            "season": (month % 12 + 3) // 3,
            "Latitude": latitude,
            "Longitude": longitude,
            "Country": country_code,
            "City": city_code,
            "AverageTemperatureUncertainty": 0.5
        }])

        predicted_temp = model.predict(input_data)[0]

        # Get historical data
        hist_data = historical_df[
            (historical_df["City"] == city) &
            (historical_df["Country"] == country)
        ][["dt", "AverageTemperature"]].dropna()

        hist_data["dt"] = pd.to_datetime(hist_data["dt"])
        hist_data = hist_data.sort_values("dt")

        years = hist_data["dt"].dt.year.tolist()
        temps = hist_data["AverageTemperature"].tolist()

        return render_template(
            "result.html",
            city=city,
            country=country,
            date=date,
            temperature=round(predicted_temp, 2),
            years=years,
            temps=temps
        )

    return render_template("index.html", countries=countries)


@app.route("/get_cities/<country>")
def get_cities(country):
    cities = sorted(location_df[location_df["Country"] == country]["City"].unique())
    return jsonify(cities)


if __name__ == "__main__":
    app.run(debug=True)
