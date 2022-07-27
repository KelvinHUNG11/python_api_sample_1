import json
from datetime import datetime
import logging
import flask
from flask import request, jsonify, Response

def post():
    try:
        startTime = datetime.now()
        logging.info("The sample API server is called at: " + str(startTime))

        ##proceed your tasks

        endTime = datetime.now()
        logging.info("Completion time at: " + str(endTime))
        response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        return response

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response
