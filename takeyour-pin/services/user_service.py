def user_service() -> dict:

    emails = ['isadorarosangelanogueira@gtx.ag',
              'tatianejenniferdacruz@construtoracostanorte.com.br',
              'maya-goncalves79@candello.abv.br',
              'teresinha.sabrina.brito@ramiresmotors.com.br',
              'thiago-vieira86@mls.com.br']

    def email_exists(email: str) -> bool:

        return True if [] != list(filter(lambda u: u == email, emails)) else False

    return {"email_exists": email_exists}
