from fastapi import FastAPI, Query
from typing import List
from core.models import Suggestion
from core.service import get_tours, test
from core.google_api import get_places
import itertools

app = FastAPI()


@app.post("/tours/suggest")
def suggest_tours(suggest: Suggestion):
    return get_tours(suggest)


@app.get("/tours/pois")
def get_pois(latitude, longitude, categories: List[str] = Query(None)):
    return list(
        map(
            lambda item: {
                "latitude": item["geometry"]["location"]["lat"],
                "longitude": item["geometry"]["location"]["lng"],
            },
            itertools.chain(
                *[
                    get_places(latitude, longitude, category)
                    for category in categories
                ]
            ),
        )
    )


@app.get("/test")
def images():
    return test()
