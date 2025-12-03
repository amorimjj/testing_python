import requests

url = 'http://localhost:8000'

def get_data():
    with requests.get(url) as response:
        data = response.json()
        # data = json.load(f)
        # emails = [item['email'] for item in data]
        return data
    

print(get_data())