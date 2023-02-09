import json
from datetime import datetime
import logging
import os
from api.v1.main import *
from flask import Response, send_file

def search():
    try:
        logging.info("The sample API server is called at: " + str(datetime.now()))

        existing_path = os.getcwd()
        
        os.chdir(os.getcwd() + '/dataset')

        ##response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        
        response = send_file(os.getcwd() + "/Date_Fruit_Datasets_test.csv", 
        mimetype='text/csv',
        as_attachment = True)

        os.chdir(existing_path)

        return response

    except Exception as e:
        
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response


# def post():

#     try:
#         logging.info("The sample API server is called at: " + str(datetime.now()))
        
#         os.chdir(os.getcwd() + '/dataset')

#         ##response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        
#         ##response = send_from_directory(os.getcwd() , "Date_Fruit_Datasets_test", as_attachment=True)

#         return send_file(os.getcwd() + "/Date_Fruit_Datasets_test.csv", 
#         mimetype='text/csv',
#         as_attachment = True)
        
#         ##return send_from_directory(os.getcwd() , "Date_Fruit_Datasets_test.csv", as_attachment = True)

#     except Exception as e:
#         response = Response(json.dumps(
#         str(e)), 500, mimetype = 'application/json')
#         return response