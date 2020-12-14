from common.utils import get_env

DEBUG = get_env('FLASK_DEBUG', True)
ENV = get_env('FLASK_ENV', 'development')

HOST = get_env('HOST', '0.0.0.0')
PORT = get_env('PORT', 5000)

LOG_LEVEL = get_env('LOG_LEVEL', 'DEBUG')

MONGO_DB_CONNECTION_URI = get_env('MONGO_DB_CONNECTION_URI', f'mongodb://{HOST}:27017')
MONGO_DB_DEFAULT = get_env('MONGO_DB_DEFAULT', 'task_db')

SERVICE_URL_CONTACT_TYPE_CLASSIFICATION = get_env('SERVICE_URL_CONTACT_TYPE_CLASSIFICATION', f'http://{HOST}:5001/predict')
SERVICE_URL_TAGGER = get_env('SERVICE_URL_TAGGER', f'http://{HOST}:5002/predict')