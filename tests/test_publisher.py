from mqqt import connect_mqtt, publish


def test_publisher():
    received_data = []

    def on_message(client, userdata, msg):
        nonlocal received_data
        print(f'Received `{msg.payload.decode()}` from `{msg.topic}` topic')
        received_data += [(msg.topic, msg.payload.decode())]

    data = [('/api/status', 'healthy'),
            ('/api/temperature/S50', 24.7),
            ('/api/temperature/S107', 26.9)]

    topics = '/api/#'

    # create client
    client = connect_mqtt()

    # subscribe settings
    client.on_message = on_message
    client.subscribe(topics)

    publish(client, data)

    assert received_data == data
