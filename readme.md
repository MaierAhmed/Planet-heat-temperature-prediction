# PlanetHeat – AI-Powered Climate Prediction

PlanetHeat is a **Next-Gen Intelligent Solution** that uses **Artificial Intelligence (AI)** and **Machine Learning (ML)** to predict Earth's surface temperature trends.  
It processes historical climate data, identifies long-term patterns, and provides **actionable insights** for climate adaptation, mitigation, and disaster preparedness.

---

##  Background
Climate change is a critical global challenge, with rising temperatures impacting ecosystems, agriculture, weather patterns, and human communities.  
Accurate temperature prediction is essential for understanding climate trends and preparing for extreme weather events.  
PlanetHeat offers a **user-friendly web application** that delivers real-time climate forecasts without requiring expert technical skills.

---

##  Features
### Functional
- **Data Collection** – Uses the Berkeley Earth Surface Temperature dataset.
- **Data Preprocessing** – Handles missing values, removes outliers, and normalizes data.
- **Model Training** – Supports multiple ML algorithms (Linear Regression, Decision Trees, Neural Networks).
- **Model Evaluation** – Measures performance using MAE, RMSE, and R².
- **Real-Time Prediction** – Generates temperature forecasts for a given location and date.
- **Visualization** – Displays interactive charts comparing historical and predicted data.

### Non-Functional
- **Secure** – Prevents unauthorized data access.
- **Scalable** – Can handle large datasets.
- **Accurate** – Provides high prediction accuracy.
- **Robust** – Handles a wide range of input values.
- **Consistent** – Produces stable results across multiple runs.

---

##  Dataset
**Source:** [Berkeley Earth Surface Temperature Dataset – Kaggle](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)  
**Key Fields:**
- Date
- LandAverageTemperature (°C)
- LandMaxTemperature / LandMinTemperature (°C)
- LandAndOceanAverageTemperature (°C)
- Uncertainty measurements for each value

---

##  Tech Stack
- **Frontend:** HTML5, CSS3, Bootstrap 5, Select2, Plotly.js
- **Backend:** Flask (Python)
- **Machine Learning:** scikit-learn, pandas, numpy, matplotlib
- **Data Visualization:** Plotly, Matplotlib
- **Development Tools:** Jupyter Notebook, Google Colab

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/planetheat.git
   cd planetheat


Create virtual environment

python -m venv venv


Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies

pip install -r requirements.txt


Run the application

flask run


Open in your browser:
http://localhost:5000

Usage

Select Country, City, and Date from the homepage.

Click Predict.

View:

Predicted average temperature.
Hello how are you
Historical temperature trend vs predicted data.

Optionally, click Predict Again to run another forecast.

 Project Structure
planetheat/
│
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── static/                 # CSS, JS, and images
├── templates/              # HTML templates
├── notebooks/              # Jupyter notebooks for ML model
├── data/                   # Dataset files

└── README.md               # Project documentation

