import json
from datetime import datetime
import logging
import os
from api.v1.main import *
from flask import Response, send_file

def post():

    try:
        logging.info("The sample API server is called at: " + str(datetime.now()))
        
        os.chdir(os.getcwd() + '/dataset')

        ##response = Response(json.dumps({'Success':'true'}), 200, mimetype = 'application/json')
        
        ##response = send_from_directory(os.getcwd() , "Date_Fruit_Datasets_test", as_attachment=True)

        return send_file(os.getcwd() + "/Date_Fruit_Datasets_test.csv", 
        mimetype='file/csv',
        as_attachment = True)
        
        ##return send_from_directory(os.getcwd() , "Date_Fruit_Datasets_test.csv", as_attachment = True)

    except Exception as e:
        response = Response(json.dumps(
        str(e)), 500, mimetype = 'application/json')
        return response