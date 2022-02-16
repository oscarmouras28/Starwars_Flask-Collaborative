import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import d
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASEDIR, "app.db")
Migrate(app,d)
d.init_app(app)
CORS(app)



app.run(host="0.0.0.0")
