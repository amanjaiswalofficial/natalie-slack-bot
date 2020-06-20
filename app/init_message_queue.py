import pika


def setup_mq(config):
    """
    This method takes a config dict as input and
    initializes a message channel object
    returning a dict of channel, exchange_name and routing_key
    :param config: Dictionary of config values
    :return: Dict of channel, exchange and routing_key
    """
    url = config['CLOUDAMQP_URL']
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=config["QUEUE_NAME"])
    return channel, connection
