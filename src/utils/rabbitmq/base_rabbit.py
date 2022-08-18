from typing import Callable

import pika


class BaseConnection:
    QUEUE = None

    def __init__(self, dsn: str):
        self.channel = None
        self.connection = None
        self.parameters = pika.URLParameters(dsn)

    def connect(self):
        self.connection = pika.BlockingConnection(parameters=self.parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(self.QUEUE, durable=True)
        # self.channel.queue_bind(self.QUEUE, exchange='')

    def publish(self, body, exchange: str = '', routing_key: str | None = None):
        if not routing_key:
            routing_key = self.QUEUE
        self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)

    def consume(self, callback: Callable, auto_ack: bool = False):
        self.channel.basic_consume(queue=self.QUEUE, auto_ack=auto_ack, on_message_callback=callback)

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def start_consume(self):
        self.channel.start_consuming()
