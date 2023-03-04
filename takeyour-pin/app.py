from bottle import Bottle

from routes.pin_route import pin_routing

from controllers.pin_controller import pin_controller

from services.pin_service import pin_service

from services.user_service import user_service

if __name__ == "__main__":

    app = Bottle()

    pin_routing(app, pin_controller(user_service(), pin_service()))

    app.run(debug=True, reloader=True, host='localhost', port=8080)
    # app.run(host='localhost', port=8080)
