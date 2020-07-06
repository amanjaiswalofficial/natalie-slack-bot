import json
from flask import Response
from slackeventsapi import SlackEventAdapter

from app import app
from .utils import setup_mq


slack_events_adapter = \
    SlackEventAdapter(app.config["SLACK_SIGNING_SECRET"], "/", app)


@slack_events_adapter.on("app_mention")
def handle_app_mention(event_data):
    """
    This method handles event, app_mention of the slack bot Natalie.
    It sends a message to the consumer via message queue and returns success
    response with a header to inform Slack to not retry anymore.
    :param event_data:
    :return: Success Response
    """

    channel, connection = setup_mq(app.config)
    channel.basic_publish(exchange=app.config["EXCHANGE"],
                          routing_key=app.config["ROUTING_KEY"],
                          body=json.dumps(event_data))

    response = Response(status=200)
    response.headers['X-Slack-No-Retry'] = 1
    print("Sent Response")
    connection.close()
    return response
