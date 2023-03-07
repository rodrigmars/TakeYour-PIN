from takeyour_pin.utils.reponse_util import prime_response

from takeyour_pin.controllers.pin_controller import pin_controller


def test_response_pin_code():

    expected = {"pin": "A08b15"}

    mock_services = {"user_service": {"email_exists": lambda _: True},
                     "pin_service": {"generate": lambda: expected.get("pin")}}

    controller = pin_controller(prime_response, **mock_services)

    assert expected == controller["generate"](None)


# def test_response_pin_code_email_not_found():

#     expected = {"message": "Email não encontrado"}

#     mock_services = {"user_service": {"email_exists": lambda _: False},
#                      "pin_service": {"generate": lambda: expected.get("pin")}}

#     controller = pin_controller(prime_response, **mock_services)

#     assert expected == controller["generate"](None)
