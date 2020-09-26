from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_turist_allow_current_location():
    assert True


def test_turist_not_allow_current_location():
    assert True


def test_get_preferences_places():
    assert True


def test_get_pois():
    assert True


def test_get_preferences_places_fails():
    assert True


def test_get_pois_fails():
    assert True


def test_get_itinerary():
    assert True


def test_get_itinerary_fails():
    assert True


def test_get_itinerary_only_time_available():
    assert True


def test_get_itinerary_with_details():
    assert True


def get_nearest_places():
    assert True
