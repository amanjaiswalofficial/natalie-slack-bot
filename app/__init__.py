import json

from flask import Flask

from app.utils import validate_config

app = Flask(__name__, instance_relative_config=False)

with open('./config.json') as config_file:
    config_values = json.load(config_file)
validate_config(config_values)

app.config.from_json("../config.json")
