from takeyour_pin.controllers.pin_controller import pin_controller


def test_pin_code():

    expected_pin_code = "A08b15"

    mock_services = {"user_service": {"email_exists": lambda _: True},
                     "pin_service": {"generate": lambda: expected_pin_code}}

    controller = pin_controller(**mock_services)

    assert {"status_code": 200,
            "pin": expected_pin_code} == controller["generate"](None)
