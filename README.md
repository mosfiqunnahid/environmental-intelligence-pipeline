# Urban Climate & Air Quality Intelligence System

## Overview
An end-to-end environmental data engineering project that collects real-time weather data from a REST API, transforms JSON into structured datasets, validates data quality, performs EDA, creates GIS maps, and provides an interactive dashboard.

## Real-World Problem
Urban areas face climate stress from rising temperatures, humidity, and changing weather patterns. This project builds a lightweight environmental intelligence system for monitoring climate conditions across German cities.

## Workflow
API Source → Python Extraction → JSON Parsing → Validation → Transformation → CSV Storage → EDA → GIS Map → Streamlit Dashboard

## Tools
Python, REST API, OpenWeather API, Pandas, Matplotlib, Plotly, Folium, Streamlit, GitHub

## Cities
Dortmund, Berlin, Hamburg, Munich, Cologne, Düsseldorf, Essen

## Variables
city, country, latitude, longitude, temperature_c, feels_like_c, humidity, pressure, wind_speed, weather_condition, weather_description, collected_at

## How to Run

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create API key file
Copy `.env.example` to `.env` and add your OpenWeather API key.

```bash
cp .env.example .env
```

### 4. Run ETL pipeline
```bash
python src/main.py
```

### 5. Run EDA script
```bash
python src/eda.py
```

### 6. Create GIS map
```bash
python src/create_map.py
```

### 7. Run dashboard
```bash
streamlit run dashboard/app.py
```

## Resume Description
Urban Climate & Air Quality Intelligence System — Developed an end-to-end environmental data engineering project using REST APIs, Python, and Pandas to collect, clean, validate, and analyze real-time weather data across German cities. Built automated ETL workflows, structured analytics-ready datasets, exploratory visualizations, and geospatial maps for urban climate intelligence.

## Future Improvements
Add OpenAQ air-quality data, PostgreSQL storage, Databricks/Spark version, scheduled execution, and predictive climate-risk scoring.
