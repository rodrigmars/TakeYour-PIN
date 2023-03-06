from typing import Callable

def pin_routing(app, controllers: dict[str, Callable[[str], str]]):
    app.route('/pin/<email>', 'GET', controllers['generate'])
    

