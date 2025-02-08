import config, getpass, pika

password = getpass.getpass(f"Enter password for user '{config.user}': ")

credentials = pika.PlainCredentials(config.user, password)

parameters = pika.ConnectionParameters(host=config.host, virtual_host=config.vhost, credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange=config.exchange, exchange_type="direct", durable=True)

channel.queue_declare(queue=config.queue, durable=True, arguments={"x-message-ttl": config.ttl})

channel.queue_bind(exchange=config.exchange, queue=config.queue, routing_key=config.routing_key)

print(f"The Exchange '{config.exchange}' and queue '{config.queue}' were created on vhost '{config.vhost}'.")
connection.close()
