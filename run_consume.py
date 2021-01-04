import json
from slack import WebClient

from app.utils import setup_mq, validate_config
from app.parsers_scrapes import run_command

with open('./config.json') as config_file:
    config_values = json.load(config_file)

validate_config(config_values)

channel, connection = setup_mq(config_values)
slack_signing_key = config_values["SECRET_SIGNING_KEY"]


def callback(ch, method, properties, body):
    """
    Callback method to handle the message sent through the message queue and
    perform something
    :param ch:
    :param method:
    :param properties:
    :param body: The json object of the event, received from slack
    :return: None
    """
    data = json.loads(body)
    event_type = data['event']['type']
    if event_type == 'app_mention':
        # Example: find Breaking Bad, read DOG (for Den of Geek)
        command, *arguments = data['event']['text'].split(" ")[1:]
        run_command[command](slack_signing_key, arguments)


channel.basic_consume(config_values['QUEUE_NAME'],
                      callback, auto_ack=True)

print(' [*] Waiting for commands:')
channel.start_consuming()
connection.close()
