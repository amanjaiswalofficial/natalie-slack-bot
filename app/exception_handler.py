"""Global error handler"""
import json

from slackeventsapi.server import SlackEventAdapterException


def init_error_handler(app):
    """
    Function to initial global error handler
    :arg app : Application reference
    """
    @app.errorhandler(SlackEventAdapterException)
    def handle_invalid_secret_signing(err: SlackEventAdapterException) -> None:
        """
        This method will handle error for invalid secret signing key for slack.
        :param err: Any kind of exception
        :return: Error object describing the error
        information and an error message
        """
        print(json.dumps({
            "error": "Invalid signing secret key, please fix config"
        }))
        raise ConnectionError("Invalid signing secret, please fix config")

    @app.errorhandler(Exception)
    def handle_all_error(err: Exception) -> None:
        """
        This method will handle the exceptions which are raised
        and not caught anywhere else in the code
        :param err: Any kind of exception
        :return: Error object describing the error
        information and an error message
        """
        print(json.dumps({
            "error": str(err)
        }))
        raise Exception(err)
