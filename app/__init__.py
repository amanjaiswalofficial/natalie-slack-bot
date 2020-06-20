from flask import Flask

app = Flask(__name__, instance_relative_config=False)
app.config.from_json("../config.json")

from .init_message_queue import setup_mq
channel, connection = setup_mq(app.config)
