from typing import Callable


def pin_controller(user_service: dict[str, Callable[[str], bool]],
                   pin_service: dict[str, Callable[[], str]]) -> dict:

    def generate(email: str) -> dict:

        code: str | None = ""

        if user_service["email_exists"](email):

            code = pin_service["generate"]()

        # response.update(response_builder(200, {'pin': code}))

        return {"status_code": 200, "pin": code}

    return {"generate": generate}
