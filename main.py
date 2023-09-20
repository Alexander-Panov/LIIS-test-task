from mqqt import connect_mqtt, publish
from parsing import get_json_data, get_topics

if __name__ == '__main__':
    json = get_json_data()
    data = get_topics(json)

    client = connect_mqtt()
    publish(client, data)
    
