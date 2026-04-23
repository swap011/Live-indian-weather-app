from __future__ import annotations

import requests
import pandas as pd
import streamlit as st

INDIAN_CITIES: dict[str, tuple[float, float]] = {
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Pune": (18.5204, 73.8567),
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
}

@st.cache_data(show_spinner=False, ttl=60)
def _fetch_weather(lat: float, lon: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": str(lat),
        "longitude": str(lon),
        "current": "temperature_2m,weather_code,relative_humidity_2m,wind_speed_10m",
        "temperature_unit": "celsius",
        "timezone": "auto",
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        status_code = resp.status_code
        try:
            payload = resp.json()
        except Exception:
            payload = {"message": "Non-JSON response from weather API"}
    except requests.exceptions.RequestException as e:
        return {"status_code": 500, "payload": {"message": f"Network Error: {str(e)}" }}

    return {"status_code": status_code, "payload": payload}

def _weather_code_to_text(code: int | None) -> str:
    mapping = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Rime fog", 51: "Light drizzle", 53: "Moderate drizzle",
        55: "Dense drizzle", 56: "Light freezing drizzle", 57: "Dense freezing drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        66: "Light freezing rain", 67: "Heavy freezing rain",
        71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
        77: "Snow grains", 80: "Slight rain showers", 81: "Moderate rain showers",
        82: "Violent rain showers", 85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm (slight hail)", 99: "Thunderstorm (heavy hail)",
    }
    if code is None: return "—"
    try: return mapping.get(int(code), f"Code {code}")
    except Exception: return "—"

def main() -> None:
    st.set_page_config(page_title="Live Indian Weather", page_icon="🌤️", layout="centered")

    st.title("🌤️ Live Indian Weather")
    st.caption("Powered by Open-Meteo (no API key required).")

    city_name = st.selectbox("Select a city:", list(INDIAN_CITIES.keys()))

    if city_name:
        lat, lon = INDIAN_CITIES[city_name]
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}), zoom=10, use_container_width=True)

        if st.button("Get Weather Info", type="primary"):
            with st.spinner("Fetching weather…"):
                result = _fetch_weather(lat, lon)

            status_code = int(result.get("status_code", 0))
            data = result.get("payload") or {}

            if status_code == 200 and isinstance(data, dict):
                current = data.get("current") or {}
                units = data.get("current_units") or {}

                temp = current.get("temperature_2m")
                temp_unit = units.get("temperature_2m", "°C")
                weather_desc = _weather_code_to_text(current.get("weather_code"))

                humidity = current.get("relative_humidity_2m")
                wind_speed = current.get("wind_speed_10m")
                wind_unit = units.get("wind_speed_10m", "km/h")

                st.success(f"Weather Info for {city_name}")

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("🌡️ Temp", f"{temp} {temp_unit}" if temp is not None else "—")
                col2.metric("☁️ Condition", weather_desc)
                col3.metric("💧 Humidity", f"{humidity}%" if humidity is not None else "—")
                col4.metric("💨 Wind", f"{wind_speed} {wind_unit}" if wind_speed is not None else "—")
            else:
                msg = data.get("message") if isinstance(data, dict) else None
                st.error(f"❌ Error fetching data ({status_code}). {msg or 'Please try again.'}")

if __name__ == "__main__":
    main()
