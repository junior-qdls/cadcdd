from core.google_api import get_places, get_place_details
from .clustering import group_places_by_distance

import itertools


def get_tours(suggest):
    longitude = suggest.location.longitude
    latitude = suggest.location.latitude

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

    # get details (addresses, schedules, images, etc)
    # from each place, after kmeans processing
    places_with_details = list(
        map(lambda item: get_place_details(item), group)
        for group in grouped_places
    )

    # response the itinerary plan per day
    return {
        "itinerary_plan": [
            {"day": index + 1, "places": list(places_with_details[index])}
            for index in range(0, len(places_with_details))
        ]
    }
