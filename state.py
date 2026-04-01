from typing import TypedDict


class BriefingState(TypedDict):
    # Inputs
    location: dict          # {"lat": float, "lon": float, "name": str}
    surf_spot: dict         # {"lat": float, "lon": float, "name": str}
    topics: list[str]       # e.g. ["AI", "tech", "python"]

    # Data gathered by nodes
    weather: str
    surf: str
    news: str
    fun_fact: str

    # Final output
    briefing: str
