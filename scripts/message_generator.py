import config, datetime, getpass, pika, sys

password = getpass.getpass(f"Enter password for user '{config.user}': ")

credentials = pika.PlainCredentials(config.user, password)

parameters = pika.ConnectionParameters(host=config.host, virtual_host=config.vhost, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

if len(sys.argv) < 2:
    print("Usage: python send_messages.py \"First message\" \"Second message, and mroe if you need\" ...")
    sys.exit(1)

messages = sys.argv[1:]

expiration_time = datetime.datetime.now() + datetime.timedelta(milliseconds=config.ttl)
expiration_stamp = expiration_time.strftime("This message expires at %Y-%m-%d %H:%M:%S")

for msg in messages:
    message = f"{msg} ### {expiration_stamp}"
    channel.basic_publish(exchange=config.exchange, routing_key=config.routing_key, body=message)
    print(f"Message published: {message}")

connection.close()
