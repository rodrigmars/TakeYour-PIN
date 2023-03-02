def response_builder(code: int, data: dict) -> dict:
    return {'status': code, 'body': data}
