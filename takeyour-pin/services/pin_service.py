from random import choice  # choices
# from string import ascii_lowercase, ascii_uppercase


def pin_service() -> dict:

    def generate() -> str | None:

        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(choice(letters) for _ in range(6))
        # return ''.join(choices(ascii_uppercase + ascii_lowercase, k=6))

    return {"generate": generate}
