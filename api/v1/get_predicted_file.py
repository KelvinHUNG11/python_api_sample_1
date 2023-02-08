import json
from datetime import datetime
import logging
import flask
import os
import time
import pathlib
from api.v1.main import *
from flask import request, jsonify, Response

def post():

    try:
        logging.info("The sample API server is called at: " + str(datetime.now()))

        response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        return response

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response