import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_PATH = os.path.join(BASE_DIR, 'logs')
LOG_FILE = os.path.join(LOG_PATH, 'api.log')

DATA_PATH = os.path.join(BASE_DIR, 'data')
DATA_POSTS = os.path.join(DATA_PATH, 'data.json')
DATA_COMMENTS = os.path.join(DATA_PATH, 'comments.json')

APP_SETTINGS = 'production'
