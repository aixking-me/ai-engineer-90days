import requests

url = "https://httpbin.org/get"


params = {
    "name": "Tom",
    "age" : 18
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

print(data["url"])
print(data["args"])
