import requests
from state import BriefingState


def fetch_weather(state: BriefingState) -> dict:
    """Fetch today's weather from Open-Meteo (free, no API key needed)."""
    lat = state["location"]["lat"]
    lon = state["location"]["lon"]

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,weathercode",
            "current_weather": True,
            "timezone": "auto",
            "forecast_days": 1,
        },
    )
    data = response.json()

    current = data.get("current_weather", {})
    daily = data.get("daily", {})

    weather_summary = (
        f"Location: {state['location']['name']}\n"
        f"Current temp: {current.get('temperature', 'N/A')}°C\n"
        f"Wind: {current.get('windspeed', 'N/A')} km/h\n"
        f"High: {daily.get('temperature_2m_max', ['N/A'])[0]}°C\n"
        f"Low: {daily.get('temperature_2m_min', ['N/A'])[0]}°C\n"
        f"Rain: {daily.get('precipitation_sum', ['N/A'])[0]} mm\n"
    )

    return {"weather": weather_summary}


def fetch_surf(state: BriefingState) -> dict:
    """Fetch surf conditions from Open-Meteo Marine API (free, no API key needed)."""
    lat = state["surf_spot"]["lat"]
    lon = state["surf_spot"]["lon"]

    response = requests.get(
        "https://marine-api.open-meteo.com/v1/marine",
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": "wave_height_max,wave_period_max,wave_direction_dominant",
            "current": "wave_height,wave_period,wave_direction",
            "timezone": "auto",
            "forecast_days": 1,
        },
    )
    data = response.json()

    current = data.get("current", {})
    daily = data.get("daily", {})

    surf_summary = (
        f"Surf spot: {state['surf_spot']['name']}\n"
        f"Current wave height: {current.get('wave_height', 'N/A')} m\n"
        f"Current wave period: {current.get('wave_period', 'N/A')} s\n"
        f"Current wave direction: {current.get('wave_direction', 'N/A')}°\n"
        f"Max wave height today: {daily.get('wave_height_max', ['N/A'])[0]} m\n"
        f"Max wave period today: {daily.get('wave_period_max', ['N/A'])[0]} s\n"
        f"Dominant direction: {daily.get('wave_direction_dominant', ['N/A'])[0]}°\n"
    )

    return {"surf": surf_summary}


def fetch_news(state: BriefingState) -> dict:
    """Fetch top headlines for your topics from NewsAPI.

    Requires a free API key from https://newsapi.org
    Set it as NEWSAPI_KEY in your .env file.
    """
    import os

    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        return {"news": "NewsAPI key not set. Get one free at https://newsapi.org"}

    all_articles = []
    for topic in state["topics"]:
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q": topic,
                "sortBy": "publishedAt",
                "pageSize": 3,
                "language": "en",
                "apiKey": api_key,
            },
        )
        data = response.json()
        articles = data.get("articles", [])

        for article in articles:
            all_articles.append(
                f"[{topic.upper()}] {article.get('title', 'No title')}\n"
                f"  {article.get('description', 'No description')}\n"
                f"  Source: {article.get('source', {}).get('name', 'Unknown')}"
            )

    news_summary = "\n\n".join(all_articles) if all_articles else "No news found."
    return {"news": news_summary}


def fetch_fun_fact(state: BriefingState) -> dict:
    """Fetch an inspirational quote from ZenQuotes (free, no API key needed)."""
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()

    if data and len(data) > 0:
        quote = data[0]
        fact = f'"{quote.get("q", "")}" — {quote.get("a", "Unknown")}'
    else:
        fact = "Stay curious."

    return {"fun_fact": fact}
