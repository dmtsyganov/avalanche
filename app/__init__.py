from flask import Flask
__author__ = 'dtsyganov'

app = Flask(__name__)
# import routes here to avoid cyclic dependencies
from app import routes
