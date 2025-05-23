import json


def load_bot_info(messages):
    with open(messages, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def save_bot_info(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
