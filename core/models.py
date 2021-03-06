from typing import List
from pydantic import BaseModel


class Location(BaseModel):
    latitud: str
    longitud: str


class Suggestion(BaseModel):
    total_days: int
    location: Location
    categories: List[str]
    start_date: str
