import googlemaps
from cachetools import cached

google_photo_url = (
    "https://maps.googleapis.com/maps/api/place/photo?"
    "maxwidth=500&maxheight=300&photoreference="
)


google_api_key = "AIzaSyAZy_JFLtPlqp7P1jEKbtzvXwMOx_fQK9s"


@cached(cache={})
def get_places(latitude, longitude, preference, radius=3000):
    return googlemaps.Client(key=google_api_key).places_nearby(
        location=f"{latitude},{longitude}",
        radius=radius,
        language="es",
        type=preference,
        name=preference,
    )["results"]


@cached(cache={})
def get_place_details(place_id):
    place_details = googlemaps.Client(key=google_api_key).place(
        place_id, language="es"
    )["result"]
    return {
        "formatted_address": place_details.get("formatted_address"),
        "formatted_phone_number": place_details.get("formatted_phone_number"),
        "lat": place_details.get("geometry").get("location").get("lat"),
        "lng": place_details.get("geometry").get("location").get("lng"),
        "name": place_details.get("name"),
        "icon": place_details.get("icon"),
        "vicinity": place_details.get("vicinity"),
        "photos": list(
            map(
                lambda photo: f"{google_photo_url}"
                + f"{photo.get('photo_reference')}"
                + f"&key={google_api_key}",
                place_details.get("photos"),
            )
        )
        if place_details.get("photos")
        else [],
    }
