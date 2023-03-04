from random import choice  # choices
# from string import ascii_lowercase, ascii_uppercase


def pin_service() -> dict:

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def generate() -> str | None:
        return ''.join(choice(letters) for _ in range(6))

    # def generate() -> str | None:
    #     return ''.join(choices(ascii_uppercase + ascii_lowercase, k=6))

    return {"generate": generate}
