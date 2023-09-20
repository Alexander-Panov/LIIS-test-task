import requests

API = 'https://api.data.gov.sg/v1/environment/air-temperature'
NEEDED_IDS = {'S50', 'S107'}


def get_json_data() -> dict:
    r = requests.get(API)
    return r.json()


def get_topics(json: dict) -> list[tuple[str, str]]:
    # topic /api/status
    result = [('/api/status', json['api_info']['status'])]
    # topics /api/temperature/id
    stations = json['items'][0]['readings']
    for station in stations:
        station_id, value = station.values()
        if station_id in NEEDED_IDS:
            result += [(f'/api/temperature/{station_id}', value)]
    return result
