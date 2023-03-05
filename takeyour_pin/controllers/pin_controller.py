from typing import Callable


def pin_controller(user_service: dict[str, Callable[[str], bool]],
                   pin_service: dict[str, Callable[[], str]]) -> dict:

    def generate(email: str) -> dict:

        response: dict[str, int | str] = {}
        exists: bool = False

        try:

            exists = user_service["email_exists"](email)

        except Exception:
            response = {"status": 500,
                        "message": "Erro interno ao tentar processar requisição"}
        else:

            response = {"status": 200, "pin": pin_service["generate"]()} if exists \
                else {"status": 404, "message": "Email não encontrado"}

        finally:

            return response

    return {"generate": generate}
