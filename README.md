# Live-indian-weather-app
# 🌤️ Live Indian Weather Dashboard  A fast, interactive,  simple real-time weather dashboard built entirely in Python .  This application fetches live weather data for major Indian cities using the free Open-Meteo API. It displays current temperature, weather conditions, humidity, and wind speed, alongside an interactive map of the selected city.
## ✨ Features

- **🌍 Interactive Map:** Automatically displays the geographical location of the selected city.
- **⚡ Real-Time Data:** Fetches the latest weather metrics (Temperature, Humidity, Wind Speed, and Conditions).
- **🚀 High Performance:** Utilizes Streamlit's `@st.cache_data` to minimize API calls and ensure instant load times.
- **🔓 No API Key Required:** Powered by the open-source [Open-Meteo API](https://open-meteo.com/), meaning anyone can clone and run this without setting up developer accounts.
- **🛡️ Error Handling:** Built-in safeguards against network timeouts and API failures.

## 🛠️ Tech Stack

- **Python 3.x**
- **[Streamlit](https://streamlit.io/):** For the front-end UI and interactive map.
- **[Requests](https://pypi.org/project/requests/):** For fetching data from the Open-Meteo REST API.
- **[Pandas](https://pandas.pydata.org/):** For data structuring and map plotting.

## **🌐 Live Demo:** [Click here to try the app live!](https://live-indian-weather-app-5dgunmkukbll9krwxfwg2u.streamlit.app/)

## 🚀 How to Run Locally

Because this is a Streamlit application, it **cannot** be run inside a Jupyter Notebook cell. It must be run from your command line/terminal.

### 1. Clone the repository
```bash
git clone https://github.com/<Your_GitHub_Username>/<Your_Repository_Name>.git
cd <Your_Repository_Name>

1. copy the (app.py) file code and run it

2. Install the required dependencies
pip install streamlit pandas requests

3.Run the application
streamlit run app.py

Run it on your browser
example - http://localhost:8500
