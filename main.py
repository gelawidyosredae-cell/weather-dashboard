from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import httpx

app = FastAPI()


@app.get("/")
def show_page():
    return FileResponse("static/index.html")


@app.get("/weather/{city}")
async def get_weather(city: str):
    async with httpx.AsyncClient(timeout=20.0) as client:
        # Find the city's latitude and longitude
        places = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
        )
        places.raise_for_status()
        place_data = places.json()

        if not place_data.get("results"):
            raise HTTPException(status_code=404, detail="City not found")

        place = place_data["results"][0]

        # Get current weather and a five-day forecast
        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "daily": (
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "weather_code,"
                    "precipitation_probability_max"
                ),
                "forecast_days": 5,
                "timezone": "auto",
            },
        )
        response.raise_for_status()
        weather_data = response.json()

    return {
        "city": place["name"],
        "country": place.get("country"),
        "weather": weather_data["current"],
        "forecast": weather_data["daily"],
    }