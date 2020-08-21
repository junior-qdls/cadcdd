from fastapi import FastAPI, Query
from typing import List
from core.models import Suggestion
from core.google_api import get_places, get_place_details
from sklearn.cluster import KMeans
import itertools
import numpy as np

app = FastAPI()


@app.post("/tours/suggest")
def suggest_tours(suggest: Suggestion):
    longitude = suggest.location.longitude
    latitude = suggest.location.latitude
    result = list(
        map(
            lambda item: {
                **item,
                "x": item["geometry"]["location"]["lat"],
                "y": item["geometry"]["location"]["lng"],
            },
            itertools.chain(
                *[
                    get_places(latitude, longitude, category)
                    for category in suggest.categories
                ]
            ),
        )
    )

    places = list(map(lambda place: place["place_id"], result))
    np_array = np.array(list(map(lambda poi: [poi["x"], poi["y"]], result)))

    kmeans = KMeans(n_clusters=suggest.total_days, random_state=0).fit(
        np_array
    )

    labels = kmeans.labels_.tolist()

    clustered_places_sorted = sorted(zip(places, labels), key=lambda x: x[1])

    places_grouped_by_cluster = list(
        [place[0] for place in group]
        for key, group in itertools.groupby(
            clustered_places_sorted, lambda cps: cps[1],
        )
    )

    result = [
        list(map(lambda item: get_place_details(item), group))
        for group in places_grouped_by_cluster
    ]

    return result


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
