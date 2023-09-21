import time

from mqqt import connect_mqtt, publish


def test_publisher():
    received_data = []

    def on_message(client, userdata, msg):
        nonlocal received_data

        payload = msg.payload.decode()
        topic = msg.topic
        try:
            payload = float(payload)
        except ValueError:
            pass

        print(f'Received `{payload}` from `{topic}` topic')

        received_data += [(topic, payload)]

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
    time.sleep(2)
    assert received_data == data
