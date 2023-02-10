import json
from datetime import datetime
import logging
import os
import csv
import pathlib
from api.v1.main import *
from flask import request, jsonify, Response

def post():

    try:
        startTime = datetime.now()
        logging.info("The sample API server is called at: " + str(startTime))

        ##Only file type == csv is accepted
        ACCEPTED_FILE_TYPE = ['.csv']

        if request.method == 'POST':

            existing_path = os.getcwd()

            ##Get the file sent from API calling
            f = request.files['file']
            f_test = request.files['test_file']

            ##Set the path to store the uploaded file
            os.chdir(os.getcwd() + '/dataset')

            ##Store the files locally
            f.save((f.filename))
            f_test.save((f_test.filename))

            ##Check the extension of the uploaded file
            file_path = pathlib.Path(f.filename)
            f_test_path = pathlib.Path(f_test.filename)
            file_type = file_path.suffixes # ['.bar', '.tar', '.gz']
            f_test_type = f_test_path.suffixes # ['.bar', '.tar', '.gz']

            ##Alter the file upload path
            path_string = str(os.getcwd()) + '/' + str(file_path)
            path_string_test = str(os.getcwd()) + '/' + str(f_test_path)

            ##Check the size of the uploaded file
            file_size = os.stat(path_string).st_size
            file_size_test = os.stat(path_string_test).st_size

            if (file_type[0] not in ACCEPTED_FILE_TYPE or file_size > 1000000 
                or f_test_type[0] not in ACCEPTED_FILE_TYPE or file_size_test > 1000000):

                response = Response(json.dumps({'Response':'failed due to wrong file type or file size'}), 200, mimetype = 'application/json')

                ##Restore to original upload file path
                os.chdir(existing_path)
                
                return response

            ##Check the columns of the two uploaded files
            result = check_uploaded_files(path_string, path_string_test)

            if (result == 'mismatched'):

                response = Response(json.dumps({'Response':'Mismatch columns of traning and testing files are found'}), 200, mimetype = 'application/json')

                return response

            ##proceed model training session
            logging.info("Model training started at: " + str(datetime.now()))
            train_model(path_string)
            logging.info("Model training completed at: " + str(datetime.now()))

            ##proceed model classification session
            logging.info("Model classification started at: " + str(datetime.now()))
            test_model(path_string_test)
            logging.info("Model classification completed at: " + str(datetime.now()))

        logging.info("API call ending at: " + str(datetime.now()))

        ##Restore to original upload file path
        os.chdir(existing_path)

        response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')

        return response

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response