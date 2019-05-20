from getpass import getpass

import pika
from pika.exceptions import ProbableAccessDeniedError, ConnectionClosedByBroker


def del_queue(q, vhost, username, password, host='localhost'):
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(
        host=host,
        virtual_host=vhost,
        credentials=credentials
    )
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_delete(queue=q)
        connection.close()
    except ConnectionClosedByBroker:
        print('Invalid username or password')
    except ProbableAccessDeniedError:
        print('Access denied')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    username = input('username: ')
    password = getpass('password: ')
    q = input('queue: ')
    vhost = input('virtual host: ')
    del_queue(q, vhost, username, password)
