from typing import Callable, Any

from bottle import response

import json


def prime_response(f: Callable) -> Callable:

    def shown(*args: Any, **kwargs: Any):

        # print('Calling', f.__name__)

        code, data = f(*args, **kwargs)

        response.status = code

        return json.dumps(data, ensure_ascii=False)

    return shown
