## This is the main python API
import os 
import logging 
import connexion
from connexion.resolver import RestyResolver
from flask_cors import CORS

logging.basicConfig(level = logging.INFO)

UPLOAD_FOLDER = "/python_api_sample_1/dataset/"

app = connexion.FlaskApp(__name__, specification_dir = "openapi/")
app.add_api("api.yaml", resolver = RestyResolver('api.v1'))
app.app.config['UPLOAD_EXTENSIONS'] = ['.xlsx', '.csv']
app.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CORS(app.app)

app.run(port = int (os.environ["PORT"]), server = 'gevent')