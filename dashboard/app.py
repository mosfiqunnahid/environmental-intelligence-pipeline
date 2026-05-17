import os
import pandas as pd
import streamlit as st
import plotly.express as px

DATA_PATH = "data/processed/weather_data.csv"

st.set_page_config(page_title="Urban Climate Intelligence Dashboard", layout="wide")

st.title("Urban Climate Intelligence Dashboard")
st.write(
    "This dashboard visualizes real-time weather data collected from REST APIs "
    "and transformed through an ETL pipeline."
)

if not os.path.exists(DATA_PATH):
    st.error("No processed data found. Please run: python src/main.py")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["collected_at"] = pd.to_datetime(df["collected_at"])
latest_df = df.sort_values("collected_at").groupby("city").tail(1)

selected_city = st.selectbox("Select a city", sorted(latest_df["city"].unique()))
city_data = latest_df[latest_df["city"] == selected_city].iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", f"{city_data['temperature_c']} °C")
col2.metric("Humidity", f"{city_data['humidity']} %")
col3.metric("Wind Speed", f"{city_data['wind_speed']} m/s")
col4.metric("Pressure", f"{city_data['pressure']} hPa")

st.subheader("Average Temperature by City")
fig_temp = px.bar(
    latest_df.sort_values("temperature_c"),
    x="city",
    y="temperature_c",
    title="Latest Temperature Comparison",
    labels={"temperature_c": "Temperature °C", "city": "City"}
)
st.plotly_chart(fig_temp, use_container_width=True)

st.subheader("Humidity vs Temperature")
fig_scatter = px.scatter(
    latest_df,
    x="humidity",
    y="temperature_c",
    color="city",
    size="wind_speed",
    hover_name="city",
    title="Humidity and Temperature Relationship"
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("Latest Environmental Dataset")
st.dataframe(latest_df)
