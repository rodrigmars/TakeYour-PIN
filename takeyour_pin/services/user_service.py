def user_service(emails: list) -> dict:

    def email_exists(email: str) -> bool:

        return True if [] != list(filter(lambda u: u == email, emails)) else False

    return {"email_exists": email_exists}
