from flask import Flask
from flask_cors import CORS
from os import getenv

app = Flask(__name__)

POSTGRES_USER = getenv('POSTGRES_USER')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
POSTGRES_HOSTNAME = getenv('POSTGRES_HOSTNAME')
POSTGRES_PORT = getenv('POSTGRES_PORT')
POSTGRES_DB = getenv('POSTGRES_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB}" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)