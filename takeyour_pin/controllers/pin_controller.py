from typing import Callable


def pin_controller(prime_response: Callable,
                   user_service: dict[str, Callable],
                   pin_service: dict[str, Callable]) -> dict:

    @prime_response
    def generate(email: str) -> tuple | None:

        data: tuple | None = None
        exists: bool = False

        try:
            exists = user_service["email_exists"](email)

        except Exception as ex:

            # TODO:Implemente aqui uma rotina para log

            data = 500, {
                "message": "Erro interno ao tentar processar requisição"}
        else:

            data = (200, {"pin": pin_service["generate"]()}) if exists \
                else (404, {"message": "Email não encontrado"})

        finally:
            return data

    return {"generate": generate}
