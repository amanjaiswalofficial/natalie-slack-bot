import json

from app.init_message_queue import setup_mq


with open('./config.json') as config_file:
    config_values = json.load(config_file)

channel, connection = setup_mq(config_values)


def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))


channel.basic_consume(config_values['QUEUE_NAME'],
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
