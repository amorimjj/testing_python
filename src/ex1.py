import json
from datetime import datetime

data = { "key1": 'value1', "key2": "value2"}

for key, value in data.items():
    print(f"{key}: {value}")

print(datetime.now())

format_string = "%Y-%m-%d %H:%M:%S"

compare = datetime(2025, 10, 4, 0, 0, 0)

def get_data():
    with open('data.json') as f:
        data = json.load(f)
        filtered = [item for item in data if item['isClient'] == True]
        # print(data)
        # print(filtered)

        # f1 = filter(lambda item: item['isClient'] == False, data)
        # filtered = list(f1)

        # print(filtered)

        f1 = filter(lambda item: datetime.strptime(item['sent'], format_string) < compare, data)
        filtered = list(f1)

        print(filtered)

        # emails = list(map(lambda item: item['email'], data))
        # print(emails)

        emails = [item['email'] for item in data]
        # print(emails)
        return emails
    

print(get_data())