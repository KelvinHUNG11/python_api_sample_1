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

        ##Only file type == csv is accepted
        ACCEPTED_FILE_TYPE = ['.csv']

        if request.method == 'POST':

            ##Get the file sent from API calling
            f = request.files['file']

            ##Set the path to store the uploaded file
            os.chdir(os.getcwd() + '/dataset')

            ##Store the file locally
            f.save((f.filename))

            ##Check the extension of the uploaded file
            print("Checkpoint 0")
            file_path = pathlib.Path(f.filename)
            file_type = file_path.suffixes # ['.bar', '.tar', '.gz']

            print("Checkpoint 1")
            ##Check the size of the uploaded file
            path_string = str(os.getcwd()) + '/' + str(file_path)
            file_size = os.stat(path_string).st_size

            if (file_type[0] not in ACCEPTED_FILE_TYPE or file_size > 1000000):

                response = Response(json.dumps({'Response':'failed due to wrong file type or file size'}), 200, mimetype = 'application/json')
                
                return response

            ##proceed your tasks
            print("Checkpoint 2")
            ref_datetime = test_func(path_string)

        endTime = datetime.now()
        logging.info("Completion time at: " + str(endTime))
        response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        return response

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response