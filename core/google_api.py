import googlemaps
from cachetools import cached


@cached(cache={})
def get_places(latitude, longitude, preference, radius=3000):
    return googlemaps.Client(
        key="AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s"
    ).places_nearby(
        location=f"{latitude},{longitude}",
        radius=radius,
        language="es",
        type=preference,
        name=preference,
    )[
        "results"
    ]


@cached(cache={})
def get_place_details(place_id):
    return googlemaps.Client(
        key="AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s"
    ).place(place_id, language="es")["result"]
