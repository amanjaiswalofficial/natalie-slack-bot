import json
from flask import Response
from slackeventsapi import SlackEventAdapter

from app import app
from app import channel, connection


slack_events_adapter = \
    SlackEventAdapter(app.config["SLACK_SIGNING_SECRET"], "/", app)


@slack_events_adapter.on("app_mention")
def handle_app_mention(event_data):
    channel.basic_publish(exchange=app.config["EXCHANGE"],
                          routing_key=app.config["ROUTING_KEY"],
                          body=json.dumps(event_data))

    # connection.close()
    response = Response(status=200)
    response.headers['X-Slack-No-Retry'] = 1
    print("Sent Response")
    return response



