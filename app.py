## This is the main python API
import os 
import logging 
import connexion
from connexion.resolver import RestyResolver
from flask_cors import CORS
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


logging.basicConfig(level = logging.INFO)

app = connexion.FlaskApp(__name__, specification_dir = "openapi/")
app.add_api("api.yaml", resolver = RestyResolver('api.v1'))
app.app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
CORS(app.app)

app.run(port = int (os.environ["PORT"]), server = 'gevent')