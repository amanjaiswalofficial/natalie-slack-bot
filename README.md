# Natalie
Natalie, is a slack-bot who has only one job, to follow the damn train. 

Kidding, it is a slack-bot that gets information from different websites and returns in specified channels.

This is a repository containing web-scraping of various websites, to ease fetching information and supplying as messages via a slack bot

## Introduction
The project is an integration of Flask-App, powered with message queues (Rabbit MQ), communicating with [Slack Events API](https://api.slack.com/events-api) via real-time sockets, to receive
events taking place in a connected workplace and do something with the connected bot based on those events and commands.

## Requirements
- Python 3.6
- A Slack Bot with permission to post messages and capture events
- Website Hosting to redirect events to your defined URL (can refer to [ngrok](https://ngrok.com/) for development purposes)

## Setup
1. After logging in, go to [Create App](https://api.slack.com/apps?new_app=1) to create a bot.
2. Choose name and workspace where this app(`bot`) can post.
3. From **Basic Information**, get the value for `Signing Secret` (**SLACK_SIGNING_SECRET**).
4. In **Event Subscriptions**, set the redirect URL where the flask app
 (using *run_produce.py* ) is hosted. Slack will validate this url in first run, 
 and then notify it each time any expected event takes place.
5. Update the events bot is subscribed to, i.e. *app_mention*, *message.im* etc.
 For each event, enable the required scope in **OAuth & Permissions**.
6. In **OAuth & Permissions**, install the app to the desired workspace. 
 This will activate the token for workspace communication.
 The `Bot User OAuth Access Token` acts as **SECRET_SIGNING_KEY**.
7. In **OAuth & Permissions**, Add required scopes as necessary.
8. Save all the changes.
9. Using the **SECRET_SIGNING_KEY**, python communicates with Slack to post message.
 Using the **SLACK_SIGNING_SECRET**, the event subscription events thrown by the Slack
 are handled by the flask application.
 
Read more on Slack Events API, click [here](https://api.slack.com/events-api).

Read more on Python Slack Events API, click [here](https://github.com/slackapi/python-slack-events-api).

## Workflow
* After setting up the slack app(`bot`), the slack app communicates 
with the hosted flask app (`run_produce.py`) on every event.
* The flask app will capture the event and return success response (`200 OK`).
* It will also push an event in the message queue as a producer, 
 with content of message.
* The python application (`run_consume.py`) which is running simultaneously
 as a consumer (*on a terminal/host*), captures the message from the queue.
* On receiving the message, the consumer grabs the event information and 
 handles the action by calling the appropriate handler.
* The handler acts and posts message on behalf of app(`bot`).
