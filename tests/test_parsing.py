import json

from parsing import get_topics


def test_get_topics():
    with open('test_data.json', 'r') as test_file:
        json_file = json.loads(test_file.read())
        assert get_topics(json_file) == [('/api/status', 'healthy'),
                                         ('/api/temperature/S50', 24.7),
                                         ('/api/temperature/S107', 26.9)]
