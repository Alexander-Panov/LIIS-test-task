import logging
import ssl
import random
import time

import paho.mqtt.client as mqtt

PORT = 8885
USERNAME = "wo"
PASSWORD = "writeonly"
TEST_SERVER = 'test.mosquitto.org'
CLIENT_ID = f'python-liis-test-task-{random.randint(0, 1000)}'

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    level=logging.DEBUG)


def _on_connect(mqttc, obj, flags, rc):
    if rc == 0 and mqttc.is_connected():
        print("Connected to MQTT Broker!")
    else:
        print(f'Failed to connect, return code {rc}')
        return


def connect_mqtt() -> mqtt:
    # connect to mqtt
    client = mqtt.Client(CLIENT_ID)

    client.on_connect = _on_connect

    client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(TEST_SERVER, PORT, keepalive=120)

    client.loop_start()
    time.sleep(1)
    return client


def publish(client, data: list[tuple[str, str]]):
    for (topic, payload) in data:
        info = client.publish(topic, payload)
        try:
            info.wait_for_publish()
            print(f'Send `{payload}` to topic `{topic}`')
        except (ValueError, RuntimeError) as exception:
            print(f'Failed to send message to topic "{topic}": {exception}')
