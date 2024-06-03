import requests
import allure
import pytest


@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify the create Booking")
@pytest.mark.crud
def test_create_booking_positive():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
}
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify the create Booking with Negative data ")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking"
    URL = base_url + path_url
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response.status_code == 500
