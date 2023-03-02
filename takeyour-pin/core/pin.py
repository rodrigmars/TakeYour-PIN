from random import choices, choice
from string import ascii_lowercase, ascii_uppercase


def pin(user: str): 

    emails = ['isadorarosangelanogueira@gtx.ag',
             'tatianejenniferdacruz@construtoracostanorte.com.br',
             'maya-goncalves79@candello.abv.br',
             'teresinha.sabrina.brito@ramiresmotors.com.br',
             'thiago-vieira86@mls.com.br']

    def generate() -> str | None:

        if [] != list(filter(lambda u: u == user, emails)):
            letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            return ''.join(choice(letters) for _ in range(6))
            # return ''.join(choices(ascii_uppercase + ascii_lowercase, k=6))

    return generate
