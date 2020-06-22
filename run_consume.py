import json
from slack import WebClient

from app.init_message_queue import setup_mq
from app.scrapes import run_command

with open('./config.json') as config_file:
    config_values = json.load(config_file)

channel, connection = setup_mq(config_values)
slack_client = WebClient(config_values["SECRET_SIGNING_KEY"])


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
        command, *args = data['event']['text'].split(" ")[1:]
        run_command[command](slack_client, args)


channel.basic_consume(config_values['QUEUE_NAME'], callback, auto_ack=True)

print(' [*] Waiting for commands:')
channel.start_consuming()
connection.close()
