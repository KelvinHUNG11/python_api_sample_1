import json
from datetime import datetime
import logging
import flask
from api.v1.main import *
from flask import request, jsonify, Response

def post():

    body = request

    try:
        startTime = datetime.now()
        logging.info("The sample API server is called at: " + str(startTime))

        ##to receive uploaded file
        print("body:", body)

        if request.method == 'POST':
            f = request.files['file']
            f.save((f.filename))
            print("file:", f)

        ##proceed your tasks
        #ref_datetime = test_func(startTime)

        endTime = datetime.now()
        logging.info("Completion time at: " + str(endTime))
        response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        return response

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response