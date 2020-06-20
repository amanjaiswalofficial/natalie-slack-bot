from app import app
from app.event_handler import slack_events_adapter

if __name__ == "__main__":
    app.run(port=5000)
