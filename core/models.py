from typing import List
from pydantic import BaseModel


class Location(BaseModel):
    latitude: str
    longitude: str


class Suggestion(BaseModel):
    total_days: int
    location: Location
    categories: List[str]
    start_date: str
