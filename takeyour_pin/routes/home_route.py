from typing import Callable


def home_routing(app, controllers: dict[str, Callable]):
    app.route('/', 'GET', controllers['home'])
