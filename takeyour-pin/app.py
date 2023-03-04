from bottle import Bottle, response

from routes.pin_route import pin_routing

from controllers.pin_controller import pin_controller

from services.pin_service import pin_service

from services.user_service import user_service


if __name__ == "__main__":

    emails = ['isadora@gtx.ag',
              'tatiane@costanorte.com.br',
              'maya-goncalves79@candello.abv.br',
              'sabrina.brito@ramiresmotors.com.br',
              'thiago-86@mls.com.br']

    app = Bottle()

    @app.hook('after_request')
    def enable_cors():
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    pin_routing(app, pin_controller(user_service(emails), pin_service()))

    app.run(debug=True, reloader=True, host='localhost', port=8080)
    # app.run(host='localhost', port=8080)
