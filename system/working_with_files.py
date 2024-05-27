import json


def load_bot_info(messages):
    with open(messages, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
