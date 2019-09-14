from flask import Blueprint, Flask
from flask_restful import Api
from flask_cors import CORS
from .config import Config


from app.resources.Users.Users import Users
from app.resources.Users.UserId import UserId

#api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#app
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_bp, url_prefix='/api')
CORS(app, resources={r"/*": {"origins": "*"}}, headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'])


# Route
api.add_resource(Users, '/users')
api.add_resource(UserId, '/users/<user_id>')


