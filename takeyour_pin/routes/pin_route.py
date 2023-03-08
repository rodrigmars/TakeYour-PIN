from typing import Callable

def pin_routing(app, controllers: dict[str, Callable[[str], str]]):
    print("CHEGANDO AQUI>>>>>>>>")
    app.route('/pin/<email>', 'GET', controllers['generate'])
    

