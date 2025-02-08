# RabbitMQ task for Oxylabs
RabbitMQ community plugin for ansible:
```bash
ansible-galaxy collection install community.rabbitmq
```

### Vault password is stored in "password.txt" file.

Launching the playbook:
```bash
ansible-playbook -i x.x.x.x, -u root playbook/rabbitmq.yml --tags=rabbitmq --ask-vault-password
```

### Scripts to manipulate the exchange / queue / messages

Configuration is in "scripts/config.py" file

Creation of exchange, binding queue, setting the TTL:
```bash
python3 exchange_queue_creation.py
```

Pushing some messages to RabbitMQ queue:
```bash
python3 message_generator.py "Message one" "second message" "..." "Nth message"
```
