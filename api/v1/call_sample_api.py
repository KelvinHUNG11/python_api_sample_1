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

    body = request

    try:
        startTime = datetime.now()
        logging.info("The sample API server is called at: " + str(startTime))

        ACCEPTED_FILE_TYPE = ['.xlsx', '.csv']

        if request.method == 'POST':

            ##Get the file sent from API calling
            f = request.files['file']

            ##Set the path to store the uploaded file
            os.chdir(os.getcwd() + '/dataset')

            ##Check the extension of the uploaded file
            file_type = pathlib.Path(f.filename).suffixes # ['.bar', '.tar', '.gz']

            ##Check the size of the uploaded file
            file_size = os.stat(os.getcwd() + '/Date_Fruit_Datasets.xlsx').st_size

            if (file_type[0] not in ACCEPTED_FILE_TYPE or file_size > 1000000):

                response = Response(json.dumps({'Response':'failed due to wrong file type or file size'}), 200, mimetype = 'application/json')
                
                return response

            ##Store the file locally
            f.save((f.filename))

            ##proceed your tasks
            ##ref_datetime = test_func(startTime)

        endTime = datetime.now()
        logging.info("Completion time at: " + str(endTime))
        response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        return response

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response