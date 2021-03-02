import json

import mariadb
from flask import Flask
from flask_cors import CORS

from .api_v1.routes.users import users
from .api_v1.routes.login import login
from .api_v1.routes.follows import follows
from .api_v1.routes.followers import followers


app = Flask(__name__)

app.config["CORS_HEADERS"] = "Content-Type"

app.register_blueprint(users)
app.register_blueprint(login)
app.register_blueprint(follows)
app.register_blueprint(followers)

app.debug = True

CORS(app)

if __name__ == "__main__":
    app.run()
