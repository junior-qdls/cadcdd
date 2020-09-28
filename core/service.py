from core.google_api import get_places, get_place_details
from .clustering import group_places_by_distance
from .optimization import apply_ga
import datetime as dt
import json

import itertools


def get_tours(suggest):
    longitude = suggest.location.longitude
    latitude = suggest.location.latitude

    start_date = dt.datetime.strptime(suggest.start_date, "%Y-%m-%dT%H:%M:%S")

    # get places from google places api given current_location
    # and user's preferences
    places = list(
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

    # kmeans group all the places by its distance,
    # the number of clusters is the total_days
    grouped_places = group_places_by_distance(suggest.total_days, places)

    print(f"grouped_places => {json.dumps(grouped_places)}")

    # get details (addresses, schedules, images, etc)
    # from each place, after kmeans processing
    places_with_details = list(
        map(lambda item: get_place_details(item["place_id"]), group)
        for group in grouped_places
    )

    optimized_tours = list(
        apply_ga(
            pois=list(pwd),
            travel_date=start_date + dt.timedelta(days=ix),
        )
        for ix, pwd in enumerate(places_with_details)
    )

    return {
        "itinerary_plan": [
            {"day": index + 1, "places": optimized_tours[index]}
            for index in range(0, len(optimized_tours))
        ]
    }


def test():
    return get_route(
        "place_id:ChIJrXGUIIuZ1ZER3pr6zhCXFlg",
        "place_id:ChIJ11Ju5iOa1ZER4qOyQTtGyVk",
    )
