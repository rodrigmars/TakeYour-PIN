
from utils import config_utils

from markdown import markdown

from pygments.formatters import HtmlFormatter

from bottle import Bottle, static_file

from utils.reponse_util import prime_response

from routes.pin_route import pin_routing

from controllers.pin_controller import pin_controller

from services.pin_service import pin_service

from services.user_service import user_service

config = config_utils.config()["environment"]

emails = ['isadora@gtx.ag',
          'tatiane@costanorte.com.br',
          'maya-goncalves79@candello.abv.br',
          'sabrina.brito@ramiresmotors.com.br',
          'thiago-86@mls.com.br']


# @app.hook('after_request')
# def enable_cors():
#     print("CHEGANDO AQUI")
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

app = Bottle()

@app.route('/')
def home():

    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"

    with open(config["markdown_api"], 'r') as f:
        md_template = md_css_string + \
            markdown(f.read(), extensions=["fenced_code"])

    return md_template


pin_routing(app, pin_controller(prime_response,
                                user_service(emails),
                                pin_service()))

if __name__ == "__main__":

    app.run(host='localhost',
            port=8085,
            reloader=True,
            debug=True)
