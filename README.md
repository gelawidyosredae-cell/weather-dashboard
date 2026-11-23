# Atmos Weather Dashboard

A responsive weather dashboard built with Python and FastAPI. Search for a city to see current weather and a five-day forecast. The app uses Open-Meteo weather and geocoding data.

## Features

- Search for cities, including Addis Ababa and Mek’ele
- View current temperature, humidity, and wind speed
- See a five-day forecast with weather icons
- Switch between Celsius and Fahrenheit
- View the chance of precipitation for each forecast day
- Responsive layout for desktop and mobile screens

## Built With

- Python 3.14
- FastAPI
- HTML
- CSS
- JavaScript
- Open-Meteo API

## Run Locally

### Requirements

- Python 3.14 or a compatible Python version
- Internet connection

### Setup

Open a terminal in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the app:

```powershell
.\.venv\Scripts\python.exe -m fastapi dev main.py
```

Open **http://127.0.0.1:8000/** in your browser.

## Project Structure

```text
weather-dashboard/
├── main.py
├── requirements.txt
├── README.md
└── static/
    └── index.html
```

## Weather Data

Weather and location data come from [Open-Meteo](https://open-meteo.com/). The app requests updated weather data when a city is searched. It does not store weather readings in a database.

## Deployment

This repository can be hosted on GitHub as a project showcase. GitHub Pages can publish static HTML, CSS, and JavaScript, but it cannot run the Python FastAPI backend. To make the complete app available online, deploy the Python backend to a Python-compatible hosting service and connect the webpage to that hosted backend. See [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Portfolio Summary

**Atmos Weather Dashboard** is a responsive weather app built with Python, FastAPI, HTML, CSS, and JavaScript. It retrieves live weather data from Open-Meteo, supports city searches including Ethiopian cities, and displays current conditions and a five-day forecast.

## Acknowledgements

Weather and geocoding data provided by [Open-Meteo](https://open-meteo.com/).