import os
from flask import Flask

flashforward = Flask(__name__)
flashforward.config.from_object('config')

from flashforward import views
