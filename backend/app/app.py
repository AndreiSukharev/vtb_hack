from flask import Blueprint, Flask
from flask_restful import Api
# from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from .config import Config, mail_settings
import os

from app.resources.Common.Base import Base
from app.resources.Users.Users import Users
from app.resources.Users.UserId import UserId
from .resources.loginPage.SignIn import SignIn
from .resources.loginPage.LogOut import LogOut
from app.resources.Docs.Doc import Doc
from app.resources.Docs.Docs import Docs
from app.resources.Docs.Email import Email
from app.resources.Chat.Messages import Messages
from app.resources.Votes.Votes import Vote


from app.resources.Chat.Chats import Chats
from app.resources.Chat.ChatId import ChatId
from app.resources.Chat.ChatSocket import ChatSocket

#api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#app
template_dir = os.path.abspath('front_test')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)
app.register_blueprint(api_bp, url_prefix='/api')
app.config.update(mail_settings)
CORS(app, resources={r"/*": {"origins": "*"}}, headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
# jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins='*', cors_credentials=True)

# Route
api.add_resource(SignIn, '/signin')
api.add_resource(LogOut, '/logout/<user_id>')
api.add_resource(Users, '/users')
api.add_resource(UserId, '/users/<user_id>')
api.add_resource(Docs, '/docs')
api.add_resource(Email, '/email')
api.add_resource(Doc, '/docs/<doc_id>')
api.add_resource(Vote, '/votes')
api.add_resource(Messages, '/messages')
api.add_resource(Chats, '/chats')
api.add_resource(ChatId, '/chats/<chat_id>')

# chat
socketio.on_namespace(ChatSocket('/api/socket'))

# token revoke
# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     jti = decrypted_token['jti']
#     sql = "SELECT token FROM token_revokes WHERE token = %s;"
#     record = (jti,)
#     token = Base.base_get_one(sql, record)
#     if not token:
#         return False
#     return True
#
