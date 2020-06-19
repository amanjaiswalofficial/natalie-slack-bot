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
To setup the bot with [Slack Events API](https://api.slack.com/events-api), follow the steps [here](https://github.com/slackapi/python-slack-events-api).